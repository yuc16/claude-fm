"""全局配置：数据源、模型、音色、时长目标。"""

from pathlib import Path

# 项目根目录（src/claude_fm/config.py -> 上三级）
ROOT = Path(__file__).resolve().parents[2]

CONTENT_DIR = ROOT / "content"
SAMPLES_DIR = CONTENT_DIR / "samples"
STATE_FILE = CONTENT_DIR / "state.json"
PROMPT_FILE = ROOT / "prompts" / "interpret.md"

# 数据源。anthropic.com 三个源通过 sitemap 发现，claude.com/blog 解析列表页。
# dir 是该源在 content/ 下的子目录。
ANTHROPIC_SITEMAP = "https://www.anthropic.com/sitemap.xml"
SOURCES = {
    "engineering": {
        "kind": "sitemap",
        "prefix": "https://www.anthropic.com/engineering/",
        "dir": "anthropic/engineering",
    },
    "research": {
        "kind": "sitemap",
        "prefix": "https://www.anthropic.com/research/",
        "dir": "anthropic/research",
    },
    "news": {
        "kind": "sitemap",
        "prefix": "https://www.anthropic.com/news/",
        "dir": "anthropic/news",
    },
    "blog": {
        "kind": "listing",
        "url": "https://claude.com/blog",
        "dir": "claude/blog",
    },
}


def source_dir(source: str) -> Path:
    return CONTENT_DIR / SOURCES.get(source, {}).get("dir", source)


def article_path(source: str, base: str) -> Path:
    return source_dir(source) / "articles" / f"{base}.md"


def script_path(source: str, base: str) -> Path:
    return source_dir(source) / "scripts" / f"{base}.md"


def audio_path(source: str, base: str) -> Path:
    return source_dir(source) / "audio" / f"{base}.mp3"


def episode_path(source: str, base: str) -> Path:
    return source_dir(source) / "episodes" / f"{base}.md"


def ensure_source_dirs(source: str) -> None:
    for sub in ("articles", "scripts", "audio", "episodes"):
        (source_dir(source) / sub).mkdir(parents=True, exist_ok=True)

# 解读模型（claude -p 无头模式，走订阅）
CLAUDE_MODEL = "claude-sonnet-4-6"
CLAUDE_TIMEOUT = 900  # 单篇解读超时（秒）

# TTS 音色。运行 `claude-fm voices` 生成试听样品后，把选中的音色填到这里。
# TTS_VOICE 用于音色试听样品；正式合成在 TTS_VOICES 里轮换，避免一个声音听腻。
TTS_VOICE = "zh-CN-XiaoxiaoNeural"
TTS_VOICES = [
    "zh-CN-YunxiNeural",     # 男声，轻快
    "zh-CN-YunyangNeural",   # 男声，播报腔
]
TTS_RATE = "+0%"  # 语速微调，如 "+10%" / "-5%"
VOICE_CANDIDATES = {
    "zh-CN-YunxiNeural": "男声，自然轻快",
    "zh-CN-YunyangNeural": "男声，新闻播报腔",
    "zh-CN-XiaoxiaoNeural": "女声，最通用",
    "zh-CN-XiaoyiNeural": "女声，柔和",
}

# 时长目标（分钟），超出范围会在产出时告警
DURATION_MIN = 22
DURATION_MAX = 28

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def ensure_dirs() -> None:
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
