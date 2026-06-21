"""claude-fm 命令行入口。

  claude-fm discover                      列出各源文章数与新文章
  claude-fm run [--source X] [--limit N] [--url URL]   端到端流水线
  claude-fm voices                        生成音色试听样品
  claude-fm status                        显示各篇进度
"""

import argparse
import sys

from . import config, episode, fetch, interpret, sources, state, tts


def cmd_discover(args) -> None:
    st = state.load()
    known = set(st["articles"].keys())
    all_refs = sources.discover_all()
    print(f"{'源':<14}{'总数':>6}{'新文章':>8}")
    for name, refs in all_refs.items():
        new = [r for r in refs if r.url not in known]
        print(f"{name:<14}{len(refs):>6}{len(new):>8}")
        for r in new[: args.show]:
            print(f"    {r.url}")
        if len(new) > args.show:
            print(f"    ... 还有 {len(new) - args.show} 篇")


def _pipeline_one(ref: sources.ArticleRef, st: dict) -> None:
    """单篇文章走完 抓取→解读→TTS→上传包，幂等：完成的阶段跳过。"""
    art = state.get_article(st, ref.url)
    art["source"] = ref.source
    stages = art["stages"]

    # 1. 抓取
    if not stages.get("fetched"):
        print(f"  [1/4] 抓取原文 {ref.url}")
        data = fetch.fetch_article(ref)
        fetch.save_article(ref, data)
        art.update(slug=data["slug"], title=data["title"], published=data["published"])
        stages["fetched"] = True
        state.save(st)
    slug = art["slug"]

    article_path = config.article_path(ref.source, slug)
    meta, body = fetch.read_with_frontmatter(article_path)

    # 2. 解读
    if not stages.get("interpreted"):
        print(f"  [2/4] claude 生成解读稿（{config.CLAUDE_MODEL}，可能需要几分钟）...")
        result = interpret.interpret(meta, body, slug)
        print(f"        完成，{interpret.han_count(result['script'])} 个汉字")
        stages["interpreted"] = True
        state.save(st)

    script_path = config.script_path(ref.source, slug)
    script_meta, script_body = fetch.read_with_frontmatter(script_path)

    # 3. TTS
    audio_path = config.audio_path(ref.source, slug)
    if not stages.get("synthesized"):
        # 音色轮换：未合成过的文章按全局计数器交替选音色，并记到 state，重跑时沿用
        voice = art.get("voice")
        if not voice:
            idx = st.get("voice_rotation", 0)
            voice = config.TTS_VOICES[idx % len(config.TTS_VOICES)]
            st["voice_rotation"] = idx + 1
            art["voice"] = voice
        print(f"  [3/4] edge-tts 合成（{voice}）...")
        audio_path.parent.mkdir(parents=True, exist_ok=True)
        duration = tts.synthesize(tts.extract_script(script_body), audio_path, voice=voice)
        art["duration_sec"] = round(duration, 1)
        stages["synthesized"] = True
        state.save(st)
        mins = duration / 60
        flag = "" if config.DURATION_MIN <= mins <= config.DURATION_MAX else "  ⚠️ 超出 22-28 分钟目标"
        print(f"        完成，时长 {mins:.1f} 分钟{flag}")

    # 4. 上传包
    if not stages.get("packaged"):
        ep_no = state.assign_episode(st, ref.url)
        episode.write_episode(
            slug=slug,
            episode_no=ep_no,
            episode_title=script_meta.get("episode_title", art.get("title", slug)),
            shownotes=tts.extract_shownotes(script_body),
            article_meta=meta,
            duration_sec=art.get("duration_sec", 0),
        )
        stages["packaged"] = True
        state.save(st)
        ep_rel = config.episode_path(ref.source, slug).relative_to(config.ROOT)
        print(f"  [4/4] 上传包就绪: {ep_rel}（EP{ep_no}）")


def _collect_refs(st, source=None, limit=None, url=None) -> list:
    """收集待处理文章（未完成 packaged 的）。"""
    if url:
        src = next(
            (n for n, s in config.SOURCES.items()
             if url.startswith(s.get("prefix", s.get("url", "")))),
            "manual",
        )
        return [sources.ArticleRef(url=url, source=src)]

    all_refs = sources.discover_all()
    refs = []
    for name, source_refs in all_refs.items():
        if source and name != source:
            continue
        refs.extend(
            r for r in source_refs
            if not st["articles"].get(r.url, {}).get("stages", {}).get("packaged")
        )
    # sitemap 顺序大致按时间倒序（新文章在前），limit 取最前面的
    return refs[:limit] if limit else refs


def _run_batch(refs, st):
    """跑一批文章。返回 (完成数, 失败列表, 限额异常或 None)。
    撞限额时立即停止剩余文章并把 SessionLimitError 上报。"""
    ok, failed = 0, []
    for i, ref in enumerate(refs, 1):
        print(f"[{i}/{len(refs)}] {ref.url}")
        try:
            _pipeline_one(ref, st)
            ok += 1
        except interpret.SessionLimitError as e:
            kind = "周限额" if e.weekly else "会话限额"
            print(f"  ⏸ 撞{kind}，暂停（重置: {e.reset_raw or '未知'}）", file=sys.stderr)
            return ok, failed, e
        except Exception as e:
            failed.append((ref.url, str(e)))
            print(f"  ❌ 失败: {e}", file=sys.stderr)
    return ok, failed, None


def cmd_run(args) -> None:
    config.ensure_dirs()
    st = state.load()
    refs = _collect_refs(st, args.source, args.limit, args.url)
    if not refs:
        print("没有待处理的文章。")
        return
    print(f"待处理 {len(refs)} 篇：")
    ok, failed, limit_err = _run_batch(refs, st)
    print(f"\n完成 {ok} 篇，失败 {len(failed)} 篇。")
    if limit_err is not None:
        kind = "周限额" if limit_err.weekly else "会话限额"
        print(f"⏸ 已撞{kind}（重置: {limit_err.reset_raw or '未知'}），剩余未处理。用 autorun 可自动续跑。")
    for url, err in failed:
        print(f"  失败: {url}\n    {err}")


def _seconds_until_reset(reset_raw: str) -> int:
    """把 '4:50pm' / '7am' 这类重置时间换算成距现在的秒数（Asia/Shanghai）。
    解析不出来就回退 1 小时。额外加 3 分钟缓冲。"""
    import re as _re
    from datetime import datetime, timedelta
    from zoneinfo import ZoneInfo

    tz = ZoneInfo("Asia/Shanghai")
    now = datetime.now(tz)
    m = _re.match(r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", reset_raw.strip(), _re.I)
    if not m:
        return 3600
    hour = int(m.group(1)) % 12
    minute = int(m.group(2) or 0)
    ampm = (m.group(3) or "").lower()
    if ampm == "pm":
        hour += 12
    elif not ampm and hour < 8:  # 没标 am/pm 且是小时数，多为早晨重置
        pass
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return int((target - now).total_seconds()) + 180


def cmd_autorun(args) -> None:
    """无人值守：循环跑流水线，撞限额就自动睡到重置点再续，直到全部完成。"""
    import time
    from datetime import datetime

    config.ensure_dirs()
    round_no = 0
    while True:
        round_no += 1
        st = state.load()
        refs = _collect_refs(st, args.source, args.limit, None)
        if not refs:
            print(f"[autorun] 全部完成，没有待处理文章。共 {round_no - 1} 轮。")
            return
        print(f"[autorun] 第 {round_no} 轮，待处理 {len(refs)} 篇  "
              f"({datetime.now():%Y-%m-%d %H:%M})", flush=True)
        ok, failed, limit_err = _run_batch(refs, st)
        print(f"[autorun] 第 {round_no} 轮完成 {ok} 篇，失败 {len(failed)} 篇", flush=True)
        if limit_err is None:
            # 没撞限额：若本轮零进展，说明剩下的都是持续失败的，停止避免死循环
            if ok == 0:
                print(f"[autorun] 本轮无进展，剩余 {len(failed)} 篇均为持续失败，结束。")
                for url, err in failed:
                    print(f"  失败: {url}  |  {err[:80]}")
                return
            continue  # 有进展，继续下一轮把剩余的做完
        if limit_err.weekly:
            # 周限额重置在数天后，睡等没意义：停下提示换号/等重置
            print(f"[autorun] ⛔ 撞到【每周限额】（重置: {limit_err.reset_raw or '见错误信息'}）。"
                  f"睡等数天不现实，已停止。请换个账号后重新运行 autorun，会自动续传。", flush=True)
            return
        wait = _seconds_until_reset(limit_err.reset_raw)
        wake = datetime.now().timestamp() + wait
        print(f"[autorun] 撞会话限额，睡 {wait // 60} 分钟，{datetime.fromtimestamp(wake):%H:%M} "
              f"后自动续跑（重置标记: {limit_err.reset_raw or '未知'}）", flush=True)
        time.sleep(wait)


def cmd_news(args) -> None:
    """news 周报合集：按周（周日为周首）把上一周的 news 打包成一期，无人值守。
    撞会话限额自动等重置续跑，撞每周限额停下提示换号。"""
    import time
    from datetime import datetime
    from . import digest

    config.ensure_dirs()
    # 先同步新增 news 原文（发现→抓取），再按周聚合
    st = state.load()
    n = digest.sync_news(st)
    if n:
        print(f"[news] 同步到 {n} 篇新 news", flush=True)
    # 迟到文章落入已完成的周 → 重置该周以重做
    stale = digest.reset_stale_weeks(st, digest.group_news_weeks(st))
    if stale:
        print(f"[news] 检测到 {len(stale)} 周有新增文章，将重做: {', '.join(stale)}", flush=True)
    round_no = 0
    while True:
        round_no += 1
        st = state.load()
        weeks = digest.group_news_weeks(st)
        pending = [w for w in weeks
                   if not st.get("digests", {}).get(w["sunday"].isoformat(), {})
                   .get("stages", {}).get("packaged")]
        if args.limit:
            pending = pending[: args.limit]
        if not pending:
            print(f"[news] 全部完成，没有待处理周。共 {round_no - 1} 轮。")
            return
        print(f"[news] 第 {round_no} 轮，待处理 {len(pending)} 周  "
              f"({datetime.now():%Y-%m-%d %H:%M})", flush=True)
        ok, failed, limit_err = 0, [], None
        for i, w in enumerate(pending, 1):
            print(f"[{i}/{len(pending)}] {w['label']}（{len(w['items'])} 条）")
            try:
                digest.process_week(st, w)
                ok += 1
            except interpret.SessionLimitError as e:
                limit_err = e
                kind = "周限额" if e.weekly else "会话限额"
                print(f"  ⏸ 撞{kind}，暂停（重置: {e.reset_raw or '未知'}）", file=sys.stderr)
                break
            except Exception as e:
                failed.append((w["slug"], str(e)))
                print(f"  ❌ 失败: {e}", file=sys.stderr)
        print(f"[news] 第 {round_no} 轮完成 {ok} 周，失败 {len(failed)} 周", flush=True)
        if limit_err is None:
            if ok == 0:
                print(f"[news] 本轮无进展，剩余 {len(failed)} 周均为持续失败，结束。")
                return
            continue
        if limit_err.weekly:
            print(f"[news] ⛔ 撞到【每周限额】（重置: {limit_err.reset_raw or '见错误信息'}）。"
                  f"已停止，请换号后重新运行 news，会自动续传。", flush=True)
            return
        wait = _seconds_until_reset(limit_err.reset_raw)
        wake = datetime.now().timestamp() + wait
        print(f"[news] 撞会话限额，睡 {wait // 60} 分钟，{datetime.fromtimestamp(wake):%H:%M} "
              f"后自动续跑", flush=True)
        time.sleep(wait)


def cmd_voices(args) -> None:
    print("正在为各候选音色生成试听样品（同一段文本）...")
    for voice, desc, dur in tts.make_samples():
        print(f"  {voice:<24}{desc:<12}{dur:.0f}s  content/samples/{voice}.mp3")
    print(f"\n试听后把选中的音色写入 src/claude_fm/config.py 的 TTS_VOICE（当前: {config.TTS_VOICE}）")


def cmd_status(args) -> None:
    st = state.load()
    arts = st["articles"]
    if not arts:
        print("还没有处理过任何文章。先跑 claude-fm run --source engineering --limit 5")
        return
    rows = sorted(arts.items(), key=lambda kv: (kv[1].get("source", ""), kv[1].get("slug", "")))
    print(f"{'EP':<5}{'阶段':<6}{'时长':<8}{'源':<13}文件名")
    stage_names = ["fetched", "interpreted", "synthesized", "packaged"]
    for url, a in rows:
        done = sum(1 for s in stage_names if a.get("stages", {}).get(s))
        dur = a.get("duration_sec")
        dur_s = f"{dur / 60:.1f}m" if dur else "-"
        ep = f"EP{a['episode']}" if "episode" in a else "-"
        print(f"{ep:<5}{f'{done}/4':<6}{dur_s:<8}{a.get('source', '-'):<13}{a.get('slug', url)}")


def main() -> None:
    sys.stdout.reconfigure(line_buffering=True)  # 后台/管道运行时进度实时可见
    parser = argparse.ArgumentParser(prog="claude-fm", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("discover", help="列出各源文章数与新文章")
    p.add_argument("--show", type=int, default=5, help="每个源最多展示几篇新文章 URL")
    p.set_defaults(func=cmd_discover)

    p = sub.add_parser("run", help="端到端流水线：发现→抓取→解读→TTS→上传包")
    p.add_argument("--source", choices=list(config.SOURCES), help="只处理指定源")
    p.add_argument("--limit", type=int, help="最多处理几篇")
    p.add_argument("--url", help="只处理这一篇文章")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("autorun", help="无人值守循环：撞限额自动等重置再续，直到全部完成")
    p.add_argument("--source", choices=list(config.SOURCES), help="只处理指定源")
    p.add_argument("--limit", type=int, help="最多处理几篇")
    p.set_defaults(func=cmd_autorun)

    p = sub.add_parser("news", help="news 周报合集：按周打包 news，无人值守续跑")
    p.add_argument("--limit", type=int, help="最多处理几周")
    p.set_defaults(func=cmd_news)

    p = sub.add_parser("voices", help="生成音色试听样品")
    p.set_defaults(func=cmd_voices)

    p = sub.add_parser("status", help="显示各篇进度")
    p.set_defaults(func=cmd_status)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
