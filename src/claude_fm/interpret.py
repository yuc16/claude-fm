"""调用 claude -p 无头模式生成中文解读稿（走订阅，不用 API key）。"""

import re
import subprocess
from datetime import datetime

import yaml

from . import config

_CN_NUMS = "〇一二三四五六七八九"


def _cn_date(iso: str) -> str:
    """'2024-12-19' -> '二〇二四年十二月十九日'，给 prompt 用，朗读更自然。"""
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", iso or "")
    if not m:
        return "未知（原文页面没有标注发表时间，开头请向听众说明这一点）"

    def cn_two(n: int) -> str:
        if n <= 10:
            return "十" if n == 10 else _CN_NUMS[n]
        tens, ones = divmod(n, 10)
        s = ("" if tens == 1 else _CN_NUMS[tens]) + "十"
        return s + (_CN_NUMS[ones] if ones else "")

    y = "".join(_CN_NUMS[int(c)] for c in m.group(1))
    return f"{iso}（{y}年{cn_two(int(m.group(2)))}月{cn_two(int(m.group(3)))}日）"


def build_prompt(title: str, url: str, source: str, published: str, article: str) -> str:
    template = config.PROMPT_FILE.read_text(encoding="utf-8")
    return (
        template.replace("{title}", title)
        .replace("{url}", url)
        .replace("{source}", source)
        .replace("{published}", _cn_date(published))
        .replace("{today}", datetime.now().strftime("%Y-%m-%d"))
        .replace("{article}", article)
    )


class SessionLimitError(RuntimeError):
    """claude 订阅限额耗尽。reset_raw 是原始重置时间文本（如 '4:50pm'）；
    weekly=True 表示是周限额（重置在数天后，不该睡等，应停下提示换号）。"""

    def __init__(self, message: str, reset_raw: str = "", weekly: bool = False):
        super().__init__(message)
        self.reset_raw = reset_raw
        self.weekly = weekly


def _parse_session_limit(text: str):
    """识别限额错误，返回 (reset_raw, weekly) 或 None（非限额错误）。"""
    low = text.lower()
    if not any(k in low for k in ("session limit", "usage limit", "weekly limit", "rate limit")):
        return None
    weekly = "weekly" in low
    # 5 小时会话限额的重置形如 "resets 4:50pm"；周限额形如 "resets Jun 22 at 10am"
    m = re.search(r"resets?\s+([0-9]{1,2}(?::[0-9]{2})?\s*(?:am|pm)?)", text, re.I)
    return (m.group(1).strip() if m else "", weekly)


def run_claude(prompt: str) -> str:
    """子进程跑 claude -p，带 2 次重试。撞限额时抛 SessionLimitError。"""
    last_err = ""
    for attempt in range(3):
        try:
            proc = subprocess.run(
                [
                    "claude", "-p",
                    "--model", config.CLAUDE_MODEL,
                    "--output-format", "text",
                ],
                input=prompt,
                capture_output=True,
                text=True,
                timeout=config.CLAUDE_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            last_err = f"超时（{config.CLAUDE_TIMEOUT}s）"
            continue
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip()
        last_err = (proc.stderr or proc.stdout or "无输出").strip()[:500]
        parsed = _parse_session_limit(last_err)
        if parsed is not None:  # 限额错误：不重试，直接上抛让 autorun 处理
            reset_raw, weekly = parsed
            raise SessionLimitError(last_err, reset_raw, weekly)
    raise RuntimeError(f"claude -p 调用失败（3 次）: {last_err}")


def parse_output(raw: str) -> dict:
    """解析三段式输出 -> {episode_title, shownotes, script}。"""
    parts = re.split(r"^===([A-Z_]+)===\s*$", raw, flags=re.M)
    # parts: [前导, 'EPISODE_TITLE', text, 'SHOWNOTES', text, 'SCRIPT', text]
    fields = {}
    for i in range(1, len(parts) - 1, 2):
        fields[parts[i]] = parts[i + 1].strip()
    title = fields.get("EPISODE_TITLE", "")
    shownotes = fields.get("SHOWNOTES", "")
    script = fields.get("SCRIPT", "")
    if not script:
        raise RuntimeError("claude 输出缺少 ===SCRIPT=== 段，原始输出开头: " + raw[:200])
    return {"episode_title": title, "shownotes": shownotes, "script": script}


def han_count(text: str) -> int:
    return len(re.findall(r"[一-鿿]", text))


MIN_HAN_CHARS = 6300  # 低于此字数（≈23 分钟）触发一次加长重写


def interpret(article_meta: dict, article_body: str, slug: str) -> dict:
    """生成解读稿并写入 content/scripts/<slug>.md，返回解析后的字段。"""
    prompt = build_prompt(
        title=article_meta.get("title", ""),
        url=article_meta.get("url", ""),
        source=article_meta.get("source", ""),
        published=article_meta.get("published", ""),
        article=article_body,
    )
    raw = run_claude(prompt)
    result = parse_output(raw)

    # 短稿兜底：一次加长重写，取更长的版本
    if han_count(result["script"]) < MIN_HAN_CHARS:
        retry_prompt = prompt + (
            f"\n\n注意：你上一次生成的稿子只有 {han_count(result['script'])} 个汉字，"
            "太短了。这次必须写满 6800 个汉字以上，把核心内容和实践应用部分大幅展开。"
        )
        try:
            retry = parse_output(run_claude(retry_prompt))
            if han_count(retry["script"]) > han_count(result["script"]):
                result = retry
        except RuntimeError:
            pass  # 重写失败就用原稿

    frontmatter = {
        "episode_title": result["episode_title"],
        "article_title": article_meta.get("title", ""),
        "url": article_meta.get("url", ""),
        "published": article_meta.get("published", ""),
        "model": config.CLAUDE_MODEL,
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "han_chars": han_count(result["script"]),
    }
    fm = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    path = config.script_path(article_meta.get("source", ""), slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\n{fm}\n---\n\n## Shownotes\n\n{result['shownotes']}\n\n## Script\n\n{result['script']}\n",
        encoding="utf-8",
    )
    return result
