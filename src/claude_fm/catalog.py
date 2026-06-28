"""生成全集文字目录 CATALOG.md，并同步刷新 README 里的集数。每周更新时调用。"""

import re
from urllib.parse import quote

from . import config, state

_SRC_META = [
    ("engineering", "🛠️ Engineering", "anthropic/engineering"),
    ("research", "🔬 Research", "anthropic/research"),
    ("blog", "📝 Blog", "claude/blog"),
    ("news", "📰 News 周报", "anthropic/news"),
]


def _entry(source: str, rec: dict) -> dict | None:
    slug = rec.get("slug")
    ep_path = config.episode_path(source, slug)
    src_dir = dict((s, d) for s, _, d in _SRC_META)[source]
    if not config.script_path(source, slug).exists():
        return None
    title = slug
    if ep_path.exists():
        m = re.search(r"^# EP\d+ \|\s*(.+)$", ep_path.read_text(encoding="utf-8"), re.M)
        if m:
            title = m.group(1).strip()
    # news 周报是多篇合集，无单一原文；其余各有英文原文
    article_link = None
    if source != "news" and config.article_path(source, slug).exists():
        article_link = quote(f"content/{src_dir}/articles/{slug}.md")
    return {
        "ep": rec["episode"],
        "date": rec.get("published") or slug[:10],
        "title": title,
        "link": quote(f"content/{src_dir}/scripts/{slug}.md"),
        "article": article_link,
    }


def _all(st: dict) -> dict:
    by_src = {s: [] for s, _, _ in _SRC_META}
    for a in st["articles"].values():
        if a["stages"].get("packaged") and "episode" in a and a.get("source") in by_src:
            e = _entry(a["source"], a)
            if e:
                by_src[a["source"]].append(e)
    for d in st.get("digests", {}).values():
        if d["stages"].get("packaged") and "episode" in d:
            e = _entry("news", d)
            if e:
                by_src["news"].append(e)
    for s in by_src:
        by_src[s].sort(key=lambda x: (x["date"], x["ep"]))
    return by_src


def build_catalog() -> tuple:
    st = state.load()
    by_src = _all(st)
    total = sum(len(v) for v in by_src.values())
    lines = [
        "# Claude FM 全集目录",
        "",
        f"共 **{total} 集**，按来源分组、组内按发表时间排列。点击**标题**读中文解读，点击**英文原文**读原帖。",
        f"想按时间线收听，请到 [小宇宙](https://www.xiaoyuzhoufm.com/podcast/6a37f2bcdd580cf9cf4bf121)。",
        "",
    ]
    for s, label, _ in _SRC_META:
        items = by_src[s]
        lines.append(f"## {label}（{len(items)}）\n")
        for e in items:
            row = f"- `EP{e['ep']}` · {e['date']} · [{e['title']}]({e['link']})"
            if e["article"]:
                row += f" · [英文原文]({e['article']})"
            lines.append(row)
        lines.append("")
    (config.ROOT / "CATALOG.md").write_text("\n".join(lines), encoding="utf-8")
    counts = {s: len(by_src[s]) for s, _, _ in _SRC_META}
    _refresh_readme_count(total, counts)
    return total, counts


# README 表格里各源对应的标签
_TABLE_LABELS = {"engineering": "Engineering", "research": "Research",
                 "blog": "Blog", "news": "News 周报"}


def _refresh_readme_count(total: int, counts: dict) -> None:
    """把 README 里徽章、表格总数、以及各源行的集数都刷成最新。"""
    readme = config.ROOT / "README.md"
    if not readme.exists():
        return
    text = readme.read_text(encoding="utf-8")
    text = re.sub(r"已更新-\d+%20集", f"已更新-{total}%20集", text)
    text = re.sub(r"\*\*共 \d+ 集", f"**共 {total} 集", text)
    text = re.sub(r"\*\*\d+ 集\*\*", f"**{total} 集**", text)
    text = re.sub(r"完整 \d+ 集目录", f"完整 {total} 集目录", text)
    for s, label in _TABLE_LABELS.items():
        text = re.sub(rf"({re.escape(label)} \| )\d+( \|)", rf"\g<1>{counts[s]}\g<2>", text)
    readme.write_text(text, encoding="utf-8")
