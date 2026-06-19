---
title: Introducing web search on the Anthropic API
url: https://claude.com/blog/web-search-api
source: blog
published: '2025-05-07'
fetched: 2026-06-13 12:16
---

# Introducing web search on the Anthropic API

Claude can now search the web through the API, giving users access to real-time information with citations for building up-to-date AI applications.

Claude can now search the web through the API, giving users access to real-time information with citations for building up-to-date AI applications.

- May 7, 2025
- 5min

*Update:** You can now add the web fetch tool to your requests and Claude will fetch and analyze content from any webpage URL. September 10, 2025*

Today, we're introducing web search on the Anthropic API—a new tool that gives Claude access to current information from across the web. With web search enabled, developers can build Claude-powered applications and agents that deliver up-to-date insights.

Developers can now augment Claude’s comprehensive knowledge with current, real-world data by enabling the web search tool when making requests to the Messages API.

When Claude receives a request that would benefit from up-to-date information or specialized knowledge, it uses its reasoning capabilities to determine whether the web search tool would help provide a more accurate response. If searching the web would be beneficial, Claude generates a targeted search query, retrieves relevant results, analyzes them for key information, and provides a comprehensive answer with citations back to the source material.

Claude can also operate agentically and conduct multiple progressive searches, using earlier results to inform subsequent queries in order to do light research and generate a more comprehensive answer. Developers can control this by adjusting the *max_uses* parameter*.* Behind the scenes, Claude may also refine its queries to deliver a more accurate response.

With web search, developers can now build AI solutions that tap into current information without needing to manage their own web search infrastructure.

Web search enables Claude to power a wide range of use cases that benefit from real-time data and specialized knowledge across various industries. Use cases include:

- **Financial services:**Build AI agents that analyze real-time stock prices, market trends, and regulatory updates.
- **Legal research:**Create tools that access recent court decisions, regulatory changes, and legal news.
- **Developer tools:**Enable Claude to reference the latest API documentation, GitHub releases, and technology updates.
- **Productivity:**Build agents that incorporate the latest company reports, competitive intelligence, or industry research.

Every web-sourced response includes citations to source materials, enabling users to verify information directly. This is particularly valuable for sensitive use cases that require accuracy and accountability.

Organizations can maintain additional control through the following admin settings:

- **Domain allow lists**: Specify which domains Claude can search and retrieve information from, ensuring that results only come from approved sources.
- **Domain block lists**: Prevent Claude from accessing certain domains that may contain sensitive, competitive, or inappropriate content for your organization.
- **Organization-level management**: Administrators can allow or prohibit web search use at the organization level.

Web search is also now available in Claude Code, adding the latest information from the web to development workflows.

With web search enabled, Claude Code can access current API documentation, technical articles, and other information on development tools and libraries. This is particularly valuable when working with new or rapidly evolving frameworks, troubleshooting obscure errors, or implementing features that require version-specific API references.

Quora is bringing web search to its AI platform, Poe.

“Anthropic's web search tool is a welcome addition to the Poe platform. It is cost effective and delivers search results with impressive speed, which will benefit people who need access to real-time information while using Claude models on Poe,” said Spencer Chan, Head of Poe Product, Quora.

Adaptive is an AI tool for consumers to create end-to-end apps.

“Anthropic’s web search delivers consistently thorough results that have outperformed other tools we’ve tested. The depth and accuracy of Claude’s responses and its ability to function as a research agent will make a significant difference in how effectively we enable our customers to build web-enabled products,” said Dennis Xu, Co-founder, Adaptive.

Web search is now available on the Anthropic API for Claude 3.7 Sonnet, the upgraded Claude 3.5 Sonnet, and Claude 3.5 Haiku at $10 per 1,000 searches plus standard token costs.

To get started, enable the web search tool in your API requests. Explore our documentation and pricing to learn more.

Get the developer newsletter
