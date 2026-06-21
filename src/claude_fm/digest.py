"""news 周报合集：按周（周日为周首）把多篇 news 打包成一期「一周快讯」。

与单篇流水线（interpret.py）并行：news 不做单篇解读，而是按自然周聚合。
状态存在 state["digests"][<周日 ISO>]，与 state["articles"] 分开。
"""

import re
from datetime import date, datetime, timedelta

import yaml

from . import config, interpret, state, tts

PROMPT_FILE = config.ROOT / "prompts" / "news_digest.md"
BODY_CAP = 1500  # 每条 news 正文摘要上限，控制 prompt 体积


def week_sunday(d: str) -> date:
    """返回 <=d 的最近周日（周日为周首）。d 形如 'YYYY-MM-DD'。"""
    y, m, dd = map(int, d[:10].split("-"))
    dt = date(y, m, dd)
    return dt - timedelta(days=(dt.weekday() + 1) % 7)


def _cn_md(d: date) -> str:
    return f"{d.year}年{d.month}月{d.day}日"


def week_label(sunday: date) -> str:
    sat = sunday + timedelta(days=6)
    return f"{_cn_md(sunday)}–{_cn_md(sat)}"


def current_sunday() -> date:
    t = date.today()
    return t - timedelta(days=(t.weekday() + 1) % 7)


def group_news_weeks(st: dict) -> list[dict]:
    """把已抓取的 news 按周（周日起）分组，只返回已结束的周（排除当前进行中的周）。
    每项：{sunday, slug, label, items:[(meta, body)]}，按时间正序。"""
    from collections import defaultdict
    buckets: dict[date, list] = defaultdict(list)
    for url, a in st["articles"].items():
        if a.get("source") != "news" or not a.get("published"):
            continue
        buckets[week_sunday(a["published"])].append((a["published"], url))

    cur = current_sunday()
    weeks = []
    for sunday in sorted(buckets):
        if sunday >= cur:  # 当前及未来的周不做
            continue
        items = []
        for _pub, url in sorted(buckets[sunday]):
            meta, body = config_read_article(st["articles"][url])
            items.append((meta, body))
        weeks.append({
            "sunday": sunday,
            "slug": f"{sunday.isoformat()}-Anthropic一周快讯",
            "label": week_label(sunday),
            "items": items,
        })
    return weeks


def config_read_article(art: dict):
    from .fetch import read_with_frontmatter
    path = config.article_path("news", art["slug"])
    return read_with_frontmatter(path)


def build_prompt(label: str, items: list) -> str:
    template = PROMPT_FILE.read_text(encoding="utf-8")
    blocks = []
    for i, (meta, body) in enumerate(items, 1):
        excerpt = body.strip()
        if len(excerpt) > BODY_CAP:
            excerpt = excerpt[:BODY_CAP] + "……"
        blocks.append(
            f"【第{i}条 · 发表日期 {meta.get('published', '?')}】{meta.get('title', '')}\n"
            f"{excerpt}"
        )
    return (
        template.replace("{week_label}", label)
        .replace("{count}", str(len(items)))
        .replace("{today}", datetime.now().strftime("%Y-%m-%d"))
        .replace("{items}", "\n\n---\n\n".join(blocks))
    )


def _interpret_week(week: dict) -> dict:
    """调 claude 生成周报稿，带解析重试，写入 scripts/<slug>.md。"""
    prompt = build_prompt(week["label"], week["items"])
    result = last_err = None
    for _ in range(3):
        try:
            result = interpret.parse_output(interpret.run_claude(prompt))
            break
        except RuntimeError as e:
            if isinstance(e, interpret.SessionLimitError):
                raise
            last_err = e
    if result is None:
        raise last_err

    fm = {
        "episode_title": result["episode_title"],
        "week": week["label"],
        "item_count": len(week["items"]),
        "model": config.CLAUDE_MODEL,
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "han_chars": interpret.han_count(result["script"]),
    }
    fmt = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    path = config.script_path("news", week["slug"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\n{fmt}\n---\n\n## Shownotes\n\n{result['shownotes']}\n\n## Script\n\n{result['script']}\n",
        encoding="utf-8",
    )
    return result


def _write_episode(week: dict, episode_no: int, episode_title: str,
                   shownotes: str, duration_sec: float) -> None:
    minutes, seconds = divmod(int(duration_sec), 60)
    mp3 = config.audio_path("news", week["slug"])
    src_lines = []
    for meta, _ in week["items"]:
        src_lines.append(f"- {meta.get('published', '?')}  {meta.get('title', '')}\n  {meta.get('url', '')}")
    body = f"""# EP{episode_no} | {episode_title}

- 音频文件：`{mp3}`
- 时长：{minutes} 分 {seconds:02d} 秒
- 覆盖：{week['label']}（周日–周六），共 {len(week['items'])} 条

## Shownotes（复制到小宇宙）

{shownotes}

---

本期收录的原文：
{chr(10).join(src_lines)}

本期由 Claude（{config.CLAUDE_MODEL}）生成，音频由 edge-tts 合成。
"""
    out = config.episode_path("news", week["slug"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")


def process_week(st: dict, week: dict) -> None:
    """单周端到端：解读→TTS→上传包，幂等。状态存 st['digests'][周日]。"""
    key = week["sunday"].isoformat()
    d = st.setdefault("digests", {}).setdefault(key, {"slug": week["slug"], "stages": {}})
    stages = d["stages"]

    if not stages.get("interpreted"):
        print(f"  [1/3] claude 生成周报稿（{week['label']}，{len(week['items'])} 条）...")
        result = _interpret_week(week)
        print(f"        完成，{interpret.han_count(result['script'])} 个汉字")
        stages["interpreted"] = True
        state.save(st)

    from .fetch import read_with_frontmatter
    smeta, sbody = read_with_frontmatter(config.script_path("news", week["slug"]))

    audio = config.audio_path("news", week["slug"])
    if not stages.get("synthesized"):
        voice = d.get("voice")
        if not voice:
            idx = st.get("voice_rotation", 0)
            voice = config.TTS_VOICES[idx % len(config.TTS_VOICES)]
            st["voice_rotation"] = idx + 1
            d["voice"] = voice
        print(f"  [2/3] edge-tts 合成（{voice}）...")
        audio.parent.mkdir(parents=True, exist_ok=True)
        duration = tts.synthesize(tts.extract_script(sbody), audio, voice=voice)
        d["duration_sec"] = round(duration, 1)
        stages["synthesized"] = True
        state.save(st)
        print(f"        完成，时长 {duration / 60:.1f} 分钟")

    if not stages.get("packaged"):
        if "episode" not in d:
            d["episode"] = st["next_episode"]
            st["next_episode"] += 1
        _write_episode(week, d["episode"], smeta.get("episode_title", week["slug"]),
                       tts.extract_shownotes(sbody), d.get("duration_sec", 0))
        stages["packaged"] = True
        state.save(st)
        rel = config.episode_path("news", week["slug"]).relative_to(config.ROOT)
        print(f"  [3/3] 上传包就绪: {rel}（EP{d['episode']}）")
