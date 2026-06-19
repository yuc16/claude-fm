"""抓取文章正文 → content/articles/<slug>.md（frontmatter + markdown 正文）。"""

import re
from datetime import datetime

import httpx
import trafilatura
import yaml

from . import config
from .sources import ArticleRef

_MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}


def _parse_english_date(text: str) -> str:
    """'Dec 19, 2024' / 'December 19, 2024' -> '2024-12-19'，解析失败返回空。"""
    m = re.search(r"([A-Z][a-z]{2,8})\.?\s+(\d{1,2}),\s+(\d{4})", text)
    if not m:
        return ""
    mon = _MONTHS.get(m.group(1)[:3])
    if not mon:
        return ""
    return f"{m.group(3)}-{mon:02d}-{int(m.group(2)):02d}"


# 页面套话（newsletter 订阅等）。注意：trafilatura 往往不保留文章自身的小节
# 标题，不能按"标题到下一个标题"删整节，只能按段落精确剔除。
_BOILERPLATE_HEADING = re.compile(
    r"^#{1,6}\s*(Get the developer newsletter|Newsletter|Related (articles|posts)|"
    r"Subscribe.*|Stay informed)\s*$",
    re.I,
)
_BOILERPLATE_TEXT = re.compile(
    r"(Delivered monthly to your inbox|Product updates, how-tos, community spotlights)",
    re.I,
)


def _clean_markdown(markdown: str) -> str:
    paragraphs = re.split(r"\n\s*\n", markdown)
    out: list[str] = []
    drop_next = False
    for p in paragraphs:
        stripped = p.strip()
        if _BOILERPLATE_HEADING.match(stripped):
            drop_next = True  # 套话标题后紧跟的一段一并删
            continue
        if _BOILERPLATE_TEXT.search(stripped):
            drop_next = False
            continue
        if drop_next:
            drop_next = False
            continue
        out.append(stripped)
    return "\n\n".join(out).strip()


def fetch_article(ref: ArticleRef) -> dict:
    """抓取并解析一篇文章，返回 {title, published, markdown, slug}。"""
    with httpx.Client(
        headers={"User-Agent": config.USER_AGENT}, timeout=60, follow_redirects=True
    ) as client:
        resp = client.get(ref.url)
        resp.raise_for_status()
    html = resp.text

    markdown = trafilatura.extract(
        html,
        output_format="markdown",
        include_tables=True,
        include_links=False,
        favor_recall=True,
    )
    if not markdown or len(markdown) < 300:
        raise RuntimeError(f"正文提取失败或过短: {ref.url}")
    markdown = _clean_markdown(markdown)

    meta = trafilatura.extract_metadata(html)
    title = ref.title or (meta.title if meta and meta.title else "")
    if not title:
        m = re.search(r"<title>(.*?)</title>", html, re.S)
        title = m.group(1) if m else ref.url
    # 去掉站点名后缀，如 "标题 | Claude"、"标题 \ Anthropic"
    title = re.sub(r"\s*[\\|]\s*(Claude|Anthropic)\s*$", "", title).strip()

    published = ref.published or _extract_published(html)

    return {
        "title": title,
        "published": published,
        "markdown": markdown,
        "slug": make_base(published, title),
    }


_HUMAN_DATE = r"([A-Z][a-z]{2,8})\.?\s+(\d{1,2}),\s+(\d{4})"


def _extract_published(html: str) -> str:
    """提取发表日期，返回 'YYYY-MM-DD' 或 ''。

    Anthropic 文章页（engineering/research/news）的可见日期紧跟在标题 </h1>
    之后的一个 div 里，如 <h1>...</h1><div class="...">Feb 16, 2026</div>。
    这是最可靠的锚点；trafilatura 的 meta.date 对 research 页会返回错误的固定值，
    弃用。
    """
    # 锚点 1：anthropic.com 文章标题 </h1> 后紧跟的可见日期 div（research/news）
    m = re.search(r"</h1>\s*<div[^>]*>\s*" + _HUMAN_DATE, html)
    if m:
        return _parse_english_date(m.group(0))
    # 锚点 2：claude.com/blog 的 "Date" 标签字段 <div>Date</div><div>June 8, 2026</div>
    m = re.search(r">Date</div>\s*<div[^>]*>\s*" + _HUMAN_DATE, html)
    if m:
        return _parse_english_date(m.group(0))
    # 锚点 3：engineering 的 "Published ... Dec 19, 2024"（日期可能隔着嵌套标签）
    m = re.search(r"Published.{0,80}?" + _HUMAN_DATE, html, re.S)
    if m:
        return _parse_english_date(m.group(0))
    # 都没有就返回空（宁可标未知，不取页面随机日期瞎猜）
    return ""


def make_base(published: str, title: str) -> str:
    """文件名：发表日期-文章完整标题（替换文件系统非法字符）。"""
    safe = re.sub(r'[\\/:*?"<>|]', " - ", title)
    safe = re.sub(r"\s+", " ", safe).strip().rstrip(".")
    return f"{published or '0000-00-00'}-{safe}"


def save_article(ref: ArticleRef, data: dict) -> None:
    frontmatter = {
        "title": data["title"],
        "url": ref.url,
        "source": ref.source,
        "published": data["published"],
        "fetched": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    fm = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    path = config.article_path(ref.source, data["slug"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{fm}\n---\n\n{data['markdown']}\n", encoding="utf-8")


def read_with_frontmatter(path) -> tuple[dict, str]:
    """读取带 frontmatter 的 md 文件，返回 (meta, body)。"""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n+(.*)$", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)
