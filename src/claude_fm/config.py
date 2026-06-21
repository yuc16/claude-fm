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
CLAUDE_TIMEOUT = 1200  # 单篇解读超时（秒）；开深度思考后更慢，放宽到 20 分钟
# 深度思考：Claude Code 靠 prompt 里的触发词分配思考预算（实测有效，环境变量无效）。
# 取值：""=关闭、"think hard"=较深(~4x)、"ultrathink"=最深(~28x)。会附加到每次解读 prompt 末尾。
# 越深质量越高但越慢越耗 token；每周新增集数不多，用 ultrathink 完全可承受。
CLAUDE_THINKING = "ultrathink"

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

# ── 播客 RSS（托管在自有服务器，供小宇宙等客户端订阅）────────────────────
# 音频与 feed.xml 通过 Caddy 托管在东京服务器上，对外 https 访问。
FEED_BASE_URL = "https://fm.yccode.xyz"          # 中性子域名，解析到服务器
PODCAST_TITLE = "Claude FM"
PODCAST_DESCRIPTION = (
    "把 Anthropic 的前沿技术内容做成中文解读：智能体、可解释性、模型发布、"
    "安全研究……通勤、健身随时听，用碎片时间积累最前沿的 AI 知识。"
    "原文版权归 Anthropic，中文解读由 Claude 生成，仅供学习。"
)
PODCAST_AUTHOR = "Claude FM"
PODCAST_EMAIL = "wangyc0924@gmail.com"
PODCAST_COVER = f"{FEED_BASE_URL}/cover.jpg"     # 需上传一张 ≥1400×1400 封面
PODCAST_CATEGORY = "Technology"
PODCAST_LANGUAGE = "zh-cn"

# 时长目标（分钟），超出范围会在产出时告警
DURATION_MIN = 22
DURATION_MAX = 28

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def ensure_dirs() -> None:
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
