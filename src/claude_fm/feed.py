"""生成标准播客 RSS（RSS 2.0 + iTunes 标签），供小宇宙等客户端订阅。

音频托管在自有服务器：https://fm.yccode.xyz/audio/<source>/<slug>.mp3
feed.xml 也放服务器根：https://fm.yccode.xyz/feed.xml
"""

import re
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from urllib.parse import quote
from xml.sax.saxutils import escape

from . import config, state


def _collect(st: dict) -> list[dict]:
    items = []
    for a in st["articles"].values():
        if a["stages"].get("packaged") and "episode" in a:
            m = _meta(a["source"], a)
            if m:
                items.append(m)
    for d in st.get("digests", {}).values():
        if d["stages"].get("packaged") and "episode" in d:
            m = _meta("news", d)
            if m:
                items.append(m)
    items.sort(key=lambda x: x["ep"], reverse=True)  # 新集在前（RSS 惯例）
    return items


def _meta(source: str, rec: dict) -> dict | None:
    slug = rec["slug"]
    ep_path = config.episode_path(source, slug)
    audio = config.audio_path(source, slug)
    if not ep_path.exists() or not audio.exists():
        return None
    text = ep_path.read_text(encoding="utf-8")
    tm = re.search(r"^# EP\d+ \|\s*(.+)$", text, re.M)
    title = tm.group(1).strip() if tm else slug
    sm = re.search(r"## Shownotes[^\n]*\n+(.*?)\n+---", text, re.S)
    shownotes = sm.group(1).strip() if sm else ""
    ep = rec["episode"]
    date = rec.get("published") or slug[:10]
    # 标题带上文章发布日期；news 周报标题已含日期范围，不重复加
    full_title = f"EP{ep} | {title}" if source == "news" else f"EP{ep} · {date} | {title}"
    return {
        "ep": ep,
        "title": full_title,
        "shownotes": shownotes,
        "date": date,
        "duration": int(rec.get("duration_sec") or 0),
        "bytes": audio.stat().st_size,
        "url": f"{config.FEED_BASE_URL}/audio/{source}/{quote(slug)}.mp3",
        "guid": f"{source}/{slug}",
    }


def _rfc822(date: str, ep: int) -> str:
    """'YYYY-MM-DD' → RFC822；按 ep 加偏移，保证同日内按集号稳定排序。"""
    try:
        dt = datetime.strptime(date[:10], "%Y-%m-%d")
    except ValueError:
        dt = datetime(2021, 1, 1)
    dt = dt.replace(hour=8, tzinfo=timezone.utc) + timedelta(seconds=ep)
    return format_datetime(dt)


def _hms(sec: int) -> str:
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


def _cdata(text: str) -> str:
    safe = text.replace("]]>", "]]]]><![CDATA[>")
    return f"<![CDATA[{safe}]]>"


def build_feed() -> str:
    st = state.load()
    items = _collect(st)
    now = format_datetime(datetime.now(timezone.utc))
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" '
        'xmlns:content="http://purl.org/rss/1.0/modules/content/" '
        'xmlns:atom="http://www.w3.org/2005/Atom">',
        "<channel>",
        f"<title>{escape(config.PODCAST_TITLE)}</title>",
        f"<link>{config.FEED_BASE_URL}</link>",
        f"<language>{config.PODCAST_LANGUAGE}</language>",
        f"<description>{_cdata(config.PODCAST_DESCRIPTION)}</description>",
        f"<itunes:summary>{_cdata(config.PODCAST_DESCRIPTION)}</itunes:summary>",
        f"<itunes:author>{escape(config.PODCAST_AUTHOR)}</itunes:author>",
        "<itunes:explicit>false</itunes:explicit>",
        "<itunes:type>episodic</itunes:type>",
        f'<itunes:image href="{escape(config.PODCAST_COVER)}"/>',
        f'<itunes:category text="{escape(config.PODCAST_CATEGORY)}"/>',
        f"<itunes:owner><itunes:name>{escape(config.PODCAST_AUTHOR)}</itunes:name>"
        f"<itunes:email>{escape(config.PODCAST_EMAIL)}</itunes:email></itunes:owner>",
        f'<image><url>{escape(config.PODCAST_COVER)}</url>'
        f"<title>{escape(config.PODCAST_TITLE)}</title>"
        f"<link>{config.FEED_BASE_URL}</link></image>",
        f'<atom:link href="{config.FEED_BASE_URL}/feed.xml" rel="self" type="application/rss+xml"/>',
        f"<lastBuildDate>{now}</lastBuildDate>",
    ]
    for it in items:
        parts += [
            "<item>",
            f"<title>{escape(it['title'])}</title>",
            f"<itunes:title>{escape(it['title'])}</itunes:title>",
            f"<itunes:episode>{it['ep']}</itunes:episode>",
            f"<description>{_cdata(it['shownotes'])}</description>",
            f"<content:encoded>{_cdata(it['shownotes'].replace(chr(10), '<br/>'))}</content:encoded>",
            f"<pubDate>{_rfc822(it['date'], it['ep'])}</pubDate>",
            f'<enclosure url="{escape(it["url"])}" length="{it["bytes"]}" type="audio/mpeg"/>',
            f'<guid isPermaLink="false">{escape(it["guid"])}</guid>',
            f"<itunes:duration>{_hms(it['duration'])}</itunes:duration>",
            "<itunes:explicit>false</itunes:explicit>",
            "</item>",
        ]
    parts += ["</channel>", "</rss>"]
    return "\n".join(parts)


def write_feed() -> tuple:
    xml = build_feed()
    out = config.CONTENT_DIR / "feed.xml"
    out.write_text(xml, encoding="utf-8")
    n = xml.count("<item>")
    return out, n
