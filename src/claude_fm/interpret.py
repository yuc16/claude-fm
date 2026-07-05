"""调用模型生成中文解读稿。"""

import json
import os
import re
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Iterator

import httpx
import yaml

from . import config

_CN_NUMS = "〇一二三四五六七八九"

# claude -p 默认带文件工具且会加载所在目录的项目上下文/记忆。对着讲 agent、
# Claude Code 的文章时，它会"角色混淆"去读 state.json、扮演流水线操作员，输出
# 状态汇报而非解读稿。对策：在中性空目录里跑（不加载本项目上下文/记忆）+ 禁用
# 所有工具（物理上无法读文件/操作），强制它只做纯文本生成。
_NEUTRAL_CWD = os.path.join(tempfile.gettempdir(), "claude_fm_gen")
os.makedirs(_NEUTRAL_CWD, exist_ok=True)
# 只列当前 claude 版本确实存在的工具名——列表里出现未知工具名会让 claude
# 直接拒绝整个调用（"matches no known tool"），导致每次都失败。
_DISALLOWED_TOOLS = (
    "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,"
    "Task,NotebookEdit,TodoWrite"
)

_CODEX_URL = "https://chatgpt.com/backend-api/codex/responses"
_CODEX_AUTH_PATH = Path.home() / ".codex" / "auth.json"


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
    """模型后端限额耗尽。reset_raw 是原始重置时间文本（如 '4:50pm'）；
    weekly=True 表示是周限额（重置在数天后，不该睡等，应停下提示换号）。"""

    def __init__(self, message: str, reset_raw: str = "", weekly: bool = False):
        super().__init__(message)
        self.reset_raw = reset_raw
        self.weekly = weekly


class CodexAuthError(RuntimeError):
    pass


class DeepSeekAuthError(RuntimeError):
    pass


def _parse_session_limit(text: str):
    """识别限额错误，返回 (reset_raw, weekly) 或 None（非限额错误）。"""
    low = text.lower()
    if not any(k in low for k in ("session limit", "usage limit", "weekly limit", "rate limit")):
        return None
    weekly = "weekly" in low
    # 5 小时会话限额的重置形如 "resets 4:50pm"；周限额形如 "resets Jun 22 at 10am"
    m = re.search(r"resets?\s+([0-9]{1,2}(?::[0-9]{2})?\s*(?:am|pm)?)", text, re.I)
    return (m.group(1).strip() if m else "", weekly)


def run_llm(prompt: str) -> str:
    """按配置选择解读后端。"""
    if config.INTERPRET_PROVIDER == "codex":
        return run_codex(prompt)
    if config.INTERPRET_PROVIDER == "deepseek":
        return run_deepseek(prompt)
    if config.INTERPRET_PROVIDER == "claude":
        return run_claude(prompt)
    raise RuntimeError(f"未知 INTERPRET_PROVIDER: {config.INTERPRET_PROVIDER}")


def run_codex(prompt: str) -> str:
    """通过 Codex Responses SSE endpoint 生成文本，认证来自 ~/.codex/auth.json。"""
    last_err = ""
    for attempt in range(3):
        try:
            return _run_codex_once(prompt)
        except SessionLimitError:
            raise
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)[:500]
            if attempt >= 2 or not _is_retryable_error(exc):
                break
            time.sleep(20.0 * (attempt + 1))
    raise RuntimeError(f"codex responses 调用失败（3 次）: {last_err}")


def _run_codex_once(prompt: str) -> str:
    body: dict[str, Any] = {
        "model": config.CODEX_MODEL,
        "store": False,
        "stream": True,
        "instructions": "你是中文科技播客解读稿生成器。严格遵守用户提示词里的输出格式。",
        "input": [
            {
                "role": "user",
                "content": [{"type": "input_text", "text": prompt}],
            }
        ],
        "text": {"verbosity": "medium"},
        "reasoning": {"effort": config.CODEX_REASONING_EFFORT, "summary": "auto"},
        "include": ["reasoning.encrypted_content"],
        "tool_choice": "none",
        "parallel_tool_calls": False,
    }
    timeout = httpx.Timeout(
        connect=30.0,
        read=config.CODEX_TIMEOUT,
        write=30.0,
        pool=30.0,
    )
    parts: list[str] = []
    with httpx.Client(timeout=timeout) as client:
        with client.stream("POST", _CODEX_URL, headers=_codex_headers(), json=body) as response:
            if response.status_code != 200:
                raw = response.read().decode("utf-8", "ignore")
                message = _friendly_codex_error(response.status_code, raw)
                if _is_codex_limit_error(response.status_code, message):
                    raise SessionLimitError(message)
                raise RuntimeError(message)
            for event in _iter_sse(response):
                event_type = event.get("type")
                if event_type == "response.output_text.delta":
                    parts.append(event.get("delta") or "")
                elif event_type in {"error", "response.failed"}:
                    message = f"Codex stream error: {json.dumps(event, ensure_ascii=False)[:500]}"
                    if _is_codex_limit_error(None, message):
                        raise SessionLimitError(message)
                    raise RuntimeError(message)
    text = "".join(parts).strip()
    if not text:
        raise RuntimeError("Codex responses 无输出")
    return text


def _codex_headers() -> dict[str, str]:
    access_token, account_id = _load_codex_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "OpenAI-Beta": "responses=experimental",
        "originator": os.getenv("OPENAI_CODEX_ORIGINATOR", "claude-fm"),
        "User-Agent": "claude-fm (python)",
        "accept": "text/event-stream",
        "content-type": "application/json",
    }
    if account_id:
        headers["chatgpt-account-id"] = account_id
    return headers


def _load_codex_token() -> tuple[str, str]:
    if not _CODEX_AUTH_PATH.exists():
        raise CodexAuthError(f"缺少 {_CODEX_AUTH_PATH}。请先运行 `codex login`。")
    try:
        data = json.loads(_CODEX_AUTH_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CodexAuthError(f"读取 {_CODEX_AUTH_PATH} 失败: {exc}") from exc
    tokens = data.get("tokens") or {}
    access_token = tokens.get("access_token") or ""
    account_id = tokens.get("account_id") or ""
    if not access_token:
        raise CodexAuthError(f"{_CODEX_AUTH_PATH} 中没有 access_token。请重新运行 `codex login`。")
    return access_token, account_id


def _iter_sse(response: httpx.Response) -> Iterator[dict[str, Any]]:
    buffer: list[str] = []
    for line in response.iter_lines():
        if line == "":
            if not buffer:
                continue
            payload_lines = [item[5:].strip() for item in buffer if item.startswith("data:")]
            buffer = []
            raw = "\n".join(payload_lines).strip()
            if not raw or raw == "[DONE]":
                continue
            try:
                yield json.loads(raw)
            except json.JSONDecodeError:
                continue
            continue
        buffer.append(line)


def _friendly_codex_error(code: int, raw: str) -> str:
    if code == 401:
        return "ChatGPT OAuth token expired. Re-run `codex login`."
    if code == 403:
        return "ChatGPT access denied. The account may need an active Plus/Pro subscription."
    if code == 429:
        return "ChatGPT quota or rate limit exceeded."
    return f"HTTP {code}: {raw[:500]}"


def _is_codex_limit_error(code: int | None, message: str) -> bool:
    if code == 429:
        return True
    low = message.lower()
    return any(k in low for k in ("rate limit", "quota", "usage limit", "weekly limit"))


def _is_retryable_error(exc: Exception) -> bool:
    if isinstance(exc, (httpx.TimeoutException, httpx.TransportError)):
        return True
    message = str(exc).lower()
    return any(
        key in message
        for key in (
            "429",
            "500",
            "503",
            "rate limit",
            "quota",
            "timeout",
            "timed out",
            "server disconnected",
            "connection",
            "temporarily",
            "暂时",
            "try again",
            "限流",
            "配额",
        )
    )


def run_deepseek(prompt: str) -> str:
    """通过 DeepSeek OpenAI-compatible Chat Completions 生成文本。"""
    last_err = ""
    for attempt in range(3):
        try:
            return _run_deepseek_once(prompt)
        except SessionLimitError:
            raise
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)[:500]
            if attempt >= 2 or not _is_retryable_error(exc):
                break
            time.sleep(20.0 * (attempt + 1))
    raise RuntimeError(f"deepseek chat completions 调用失败（3 次）: {last_err}")


def _run_deepseek_once(prompt: str) -> str:
    body: dict[str, Any] = {
        "model": config.DEEPSEEK_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "你是中文科技播客解读稿生成器。严格遵守用户提示词里的输出格式。",
            },
            {"role": "user", "content": prompt},
        ],
        "stream": True,
    }
    if config.DEEPSEEK_THINKING:
        body["thinking"] = {"type": config.DEEPSEEK_THINKING}
    if config.DEEPSEEK_REASONING_EFFORT:
        body["reasoning_effort"] = config.DEEPSEEK_REASONING_EFFORT

    timeout = httpx.Timeout(
        connect=30.0,
        read=config.DEEPSEEK_TIMEOUT,
        write=30.0,
        pool=30.0,
    )
    parts: list[str] = []
    with httpx.Client(timeout=timeout) as client:
        with client.stream(
            "POST",
            f"{config.DEEPSEEK_BASE_URL.rstrip('/')}/chat/completions",
            headers=_deepseek_headers(),
            json=body,
        ) as response:
            if response.status_code != 200:
                raw = response.read().decode("utf-8", "ignore")
                message = _friendly_deepseek_error(response.status_code, raw)
                if _is_deepseek_limit_error(response.status_code, message):
                    raise SessionLimitError(message)
                raise RuntimeError(message)
            for event in _iter_sse(response):
                if "error" in event:
                    message = f"DeepSeek stream error: {json.dumps(event, ensure_ascii=False)[:500]}"
                    if _is_deepseek_limit_error(None, message):
                        raise SessionLimitError(message)
                    raise RuntimeError(message)
                choices = event.get("choices") or []
                if not choices:
                    continue
                delta = choices[0].get("delta") or {}
                content = delta.get("content") or ""
                if content:
                    parts.append(content)
    text = "".join(parts).strip()
    if not text:
        raise RuntimeError("DeepSeek chat completions 无输出")
    return text


def _deepseek_headers() -> dict[str, str]:
    if not config.DEEPSEEK_API_KEY:
        raise DeepSeekAuthError("缺少 DEEPSEEK_API_KEY。请在 .env 中配置 DeepSeek API key。")
    return {
        "Authorization": f"Bearer {config.DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
        "User-Agent": "claude-fm (python)",
    }


def _friendly_deepseek_error(code: int, raw: str) -> str:
    if code == 401:
        return "DeepSeek API key 错误或认证失败。请检查 DEEPSEEK_API_KEY。"
    if code == 402:
        return "DeepSeek 账户余额不足。请充值或切换模型后重试。"
    if code == 429:
        return "DeepSeek 请求速率达到上限。"
    if code in {500, 503}:
        return f"DeepSeek 服务暂时不可用（HTTP {code}）: {raw[:500]}"
    return f"DeepSeek HTTP {code}: {raw[:500]}"


def _is_deepseek_limit_error(code: int | None, message: str) -> bool:
    if code in {402, 429}:
        return True
    low = message.lower()
    return any(k in low for k in ("rate limit", "quota", "余额不足", "请求速率"))


def run_claude(prompt: str) -> str:
    """子进程跑 claude -p，带 2 次重试。撞限额时抛 SessionLimitError。"""
    # Claude CLI 通过 prompt 触发词分配思考预算。
    if config.CLAUDE_REASONING_EFFORT:
        prompt = f"{prompt}\n\n{config.CLAUDE_REASONING_EFFORT}"
    last_err = ""
    for _ in range(3):
        try:
            proc = subprocess.run(
                [
                    "claude", "-p",
                    "--model", config.CLAUDE_MODEL,
                    "--output-format", "text",
                    "--disallowedTools", _DISALLOWED_TOOLS,
                ],
                input=prompt,
                capture_output=True,
                text=True,
                timeout=config.CLAUDE_TIMEOUT,
                cwd=_NEUTRAL_CWD,
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
        raise RuntimeError("模型输出缺少 ===SCRIPT=== 段，原始输出开头: " + raw[:200])
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
    # 解析重试：claude 偶发吐出不带 ===SCRIPT=== 标记的输出，立即重生成而非
    # 跳过等下一轮（SessionLimitError 不在此捕获，照常上抛给 autorun）。
    result = None
    last_parse_err = None
    for _ in range(3):
        raw = run_llm(prompt)
        try:
            result = parse_output(raw)
            break
        except RuntimeError as e:
            last_parse_err = e
    if result is None:
        raise last_parse_err or RuntimeError("解读输出解析失败")

    # 短稿兜底：一次加长重写，取更长的版本
    if han_count(result["script"]) < MIN_HAN_CHARS:
        retry_prompt = prompt + (
            f"\n\n注意：你上一次生成的稿子只有 {han_count(result['script'])} 个汉字，"
            "太短了。这次必须写满 6800 个汉字以上，把核心内容和实践应用部分大幅展开。"
        )
        try:
            retry = parse_output(run_llm(retry_prompt))
            if han_count(retry["script"]) > han_count(result["script"]):
                result = retry
        except RuntimeError:
            pass  # 重写失败就用原稿

    frontmatter = {
        "episode_title": result["episode_title"],
        "article_title": article_meta.get("title", ""),
        "url": article_meta.get("url", ""),
        "published": article_meta.get("published", ""),
        "model": config.interpret_model(),
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
