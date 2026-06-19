"""edge-tts 合成：长文分块、逐块重试、mp3 拼接、时长校验。"""

import asyncio
import re

import edge_tts
from mutagen.mp3 import MP3

from . import config

CHUNK_LIMIT = 2000  # 单块最大字符数，过长 edge-tts 易断流


def extract_script(script_file_body: str) -> str:
    """从 scripts/<slug>.md 的正文部分提取 Script 段（去掉 Shownotes）。"""
    m = re.search(r"^## Script\s*$(.*)", script_file_body, re.S | re.M)
    text = m.group(1) if m else script_file_body
    return text.strip()


def extract_shownotes(script_file_body: str) -> str:
    m = re.search(r"^## Shownotes\s*$(.*?)^## Script\s*$", script_file_body, re.S | re.M)
    return m.group(1).strip() if m else ""


def split_chunks(text: str, limit: int = CHUNK_LIMIT) -> list[str]:
    """按段落聚合成 <= limit 字符的块；单段超长再按句子切。"""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    units: list[str] = []
    for p in paragraphs:
        if len(p) <= limit:
            units.append(p)
        else:
            sentences = re.split(r"(?<=[。！？；])", p)
            buf = ""
            for s in sentences:
                if len(buf) + len(s) > limit and buf:
                    units.append(buf)
                    buf = ""
                buf += s
            if buf:
                units.append(buf)

    chunks: list[str] = []
    buf = ""
    for u in units:
        if len(buf) + len(u) + 2 > limit and buf:
            chunks.append(buf)
            buf = ""
        buf = f"{buf}\n\n{u}" if buf else u
    if buf:
        chunks.append(buf)
    return chunks


async def _synth_chunk(text: str, voice: str, rate: str) -> bytes:
    last_err: Exception | None = None
    for attempt in range(4):
        try:
            communicate = edge_tts.Communicate(text, voice=voice, rate=rate)
            audio = b""
            async for message in communicate.stream():
                if message["type"] == "audio":
                    audio += message["data"]
            if not audio:
                raise RuntimeError("空音频")
            return audio
        except Exception as e:  # edge-tts 偶发断流，退避重试
            last_err = e
            await asyncio.sleep(2 * (attempt + 1))
    raise RuntimeError(f"TTS 块合成失败（4 次）: {last_err}")


async def synthesize_async(
    text: str, out_path, voice: str | None = None, rate: str | None = None,
    progress: bool = True,
) -> float:
    """合成整篇文本到 out_path（mp3），返回时长（秒）。"""
    voice = voice or config.TTS_VOICE
    rate = rate or config.TTS_RATE
    chunks = split_chunks(text)
    audio = b""
    for i, chunk in enumerate(chunks, 1):
        if progress:
            print(f"    TTS 块 {i}/{len(chunks)}（{len(chunk)} 字符）...")
        audio += await _synth_chunk(chunk, voice, rate)
    out_path.write_bytes(audio)
    return MP3(out_path).info.length


def synthesize(text: str, out_path, voice: str | None = None, rate: str | None = None) -> float:
    return asyncio.run(synthesize_async(text, out_path, voice, rate))


SAMPLE_TEXT = (
    "欢迎收听 Claude FM，这是一档把 Anthropic 最前沿的技术博客做成中文解读的播客节目。"
    "这篇文章发表于二〇二四年十二月十九日，讨论的是如何构建高效的 agent 系统。"
    "我们会聊到 prompt 设计、工具调用，以及在生产环境里落地时要注意的坑。"
    "比如说，Claude 三点五在处理十万 token 的长上下文时，表现已经相当稳定了。"
    "好，我们正式开始今天的节目。"
)


def make_samples() -> list[tuple[str, str, float]]:
    """为每个候选音色生成试听样品，返回 [(voice, 描述, 时长)]。"""
    config.ensure_dirs()
    results = []
    for voice, desc in config.VOICE_CANDIDATES.items():
        out = config.SAMPLES_DIR / f"{voice}.mp3"
        dur = asyncio.run(synthesize_async(SAMPLE_TEXT, out, voice=voice, progress=False))
        results.append((voice, desc, dur))
    return results
