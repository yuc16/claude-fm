import json
import unittest
from unittest.mock import patch

import httpx

from claude_fm import cli, sources


def resource_html(*cards):
    data = json.dumps(list(cards), separators=(",", ":"))
    # 网站会在任意字符位置切开卡片 JSON。
    cut = len(data) // 2
    return "".join(
        f"<script>self.__next_f.push({json.dumps([1, part])})</script>"
        for part in (data[:cut], data[cut:])
    )


ARTICLE = {
    "_id": "article-1", "_type": "blogPost", "slug": "new-article",
    "externalUrl": None, "date": "2026-10-16", "title": "New article",
}
EXTERNAL = {
    "_id": "article-2", "_type": "blogPost", "slug": None,
    "externalUrl": "https://claude.dev/blog/code-review/",
    "date": "2026-10-15", "title": "Code review",
}


class BlogDiscoveryTests(unittest.TestCase):
    def test_split_cards_keep_dates_external_urls_and_deduplicate(self):
        refs = sources._parse_blog_page(resource_html(ARTICLE, EXTERNAL, ARTICLE))
        self.assertEqual(len(refs), 2)
        self.assertEqual(refs[0].url, "https://claude.com/resources/articles/new-article")
        self.assertEqual(refs[0].published, "2026-10-16")
        self.assertEqual(refs[1].url, EXTERNAL["externalUrl"])

    def test_legacy_links(self):
        refs = sources._parse_blog_page('<a href="/blog/old-article">Old</a>')
        self.assertEqual(refs[0].url, "https://claude.com/blog/old-article")

    @patch.object(sources, "_get_with_retries")
    @patch.object(sources, "_client")
    def test_cumulative_pagination_stops_when_no_new_articles(self, client, get):
        base = "https://claude.com/resources/articles"
        get.side_effect = [
            httpx.Response(200, text=resource_html(*cards), request=httpx.Request("GET", base))
            for cards in ((ARTICLE,), (ARTICLE, EXTERNAL), (ARTICLE, EXTERNAL))
        ]
        self.assertEqual(len(sources.discover_blog_listing()), 2)
        self.assertEqual([call.args[1] for call in get.call_args_list],
                         [base, base + "?page=2", base + "?page=3"])

    @patch.object(sources, "_get_with_retries")
    @patch.object(sources, "_client")
    def test_empty_parser_result_is_failure(self, client, get):
        get.return_value = httpx.Response(200, text="<html>New layout</html>")
        with self.assertRaisesRegex(RuntimeError, "未解析到文章"):
            sources.discover_blog_listing()

    @patch.object(sources, "discover_all")
    def test_weekly_filters_known_card_dates_before_fetch(self, discover):
        discover.return_value = {"blog": [
            sources.ArticleRef(url="current", source="blog", published="2026-10-16"),
            sources.ArticleRef(url="old", source="blog", published="2026-10-08"),
        ]}
        refs = cli._collect_refs({"articles": {}}, "blog", published_start="2026-10-11",
                                 published_end="2026-10-17")
        self.assertEqual([r.url for r in refs], ["current"])


if __name__ == "__main__":
    unittest.main()
