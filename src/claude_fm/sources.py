"""文章发现：anthropic.com sitemap + claude.com/blog 列表页。"""

import re
from dataclasses import dataclass

import httpx

from . import config


@dataclass
class ArticleRef:
    url: str
    source: str
    # 列表页能拿到的元数据（sitemap 拿不到，留空，抓正文时再补）
    title: str = ""
    published: str = ""  # YYYY-MM-DD
    lastmod: str = ""  # sitemap 的最后修改时间，仅用于排序


def _client() -> httpx.Client:
    return httpx.Client(
        headers={"User-Agent": config.USER_AGENT},
        timeout=30,
        follow_redirects=True,
    )


def discover_sitemap_sources() -> dict[str, list[ArticleRef]]:
    """从 anthropic.com sitemap 发现 engineering/research/news 全量文章。"""
    with _client() as client:
        resp = client.get(config.ANTHROPIC_SITEMAP)
        resp.raise_for_status()
    entries = re.findall(
        r"<loc>(.*?)</loc>\s*(?:<lastmod>(.*?)</lastmod>)?", resp.text
    )
    result: dict[str, list[ArticleRef]] = {}
    for name, src in config.SOURCES.items():
        if src["kind"] != "sitemap":
            continue
        prefix = src["prefix"]
        # 只要 /<source>/<slug> 单级文章；排除 /<source>/team/... 这类多级页面
        refs = [
            ArticleRef(url=u, source=name, lastmod=mod)
            for u, mod in entries
            if u.startswith(prefix)
            and (rem := u[len(prefix):].rstrip("/")) and "/" not in rem
        ]
        # 新文章在前；lastmod 是修改时间不是发表时间，但用于"取最近 N 篇"足够
        refs.sort(key=lambda r: r.lastmod, reverse=True)
        result[name] = refs
    return result


def discover_blog_listing(max_pages: int = 40) -> list[ArticleRef]:
    """解析 claude.com/blog 列表页（Webflow 站，含分页）。

    Webflow CMS 翻页参数带动态哈希前缀，如 ?b7eea976_page=2，且首页标注
    "Page 1 of N"。先读首页拿到总页数和分页前缀，再逐页收集 /blog/<slug>。
    """
    base = config.SOURCES["blog"]["url"]
    seen: dict[str, ArticleRef] = {}
    with _client() as client:
        first = client.get(base)
        first.raise_for_status()
        html = first.text
        for a in _parse_blog_page(html):
            seen.setdefault(a.url, a)

        m = re.search(r"Page 1 of (\d+)", html)
        total_pages = min(int(m.group(1)), max_pages) if m else 1
        prefixes = sorted(set(re.findall(r"\?([0-9a-f]+)_page=", html)))
        if total_pages <= 1 or not prefixes:
            return list(seen.values())

        # 选一个真正能翻出新文章的分页前缀
        page1_urls = set(seen)
        prefix = next(
            (p for p in prefixes
             if set(u.url for u in _parse_blog_page(client.get(f"{base}?{p}_page=2").text)) - page1_urls),
            prefixes[0],
        )
        for page in range(2, total_pages + 1):
            try:
                resp = client.get(f"{base}?{prefix}_page={page}")
                resp.raise_for_status()
            except httpx.HTTPError:
                break
            for a in _parse_blog_page(resp.text):
                seen.setdefault(a.url, a)
    return list(seen.values())


def _parse_blog_page(html: str) -> list[ArticleRef]:
    refs = []
    for m in re.finditer(r'href="(?:https://claude\.com)?(/blog/[a-z0-9][a-z0-9-]*)"', html):
        path = m.group(1)
        url = f"https://claude.com{path}"
        refs.append(ArticleRef(url=url, source="blog"))
    # 去重保持顺序
    out, seen = [], set()
    for r in refs:
        if r.url not in seen:
            seen.add(r.url)
            out.append(r)
    return out


def discover_all() -> dict[str, list[ArticleRef]]:
    """返回 {source: [ArticleRef]}，全量（不与 state 求差）。"""
    result = discover_sitemap_sources()
    result["blog"] = discover_blog_listing()
    return result
