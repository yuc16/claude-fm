# EP15 | 上下文让 RAG 重生：Anthropic 把检索失败率降低了六成七

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2024-09-19-Contextual Retrieval in AI Systems.mp3`
- 时长：27 分 01 秒

## Shownotes（复制到小宇宙）

本期我们精读 Anthropic 工程博客的一篇技术文章，深入拆解他们提出的"上下文检索"方案——通过给每个文档片段自动补充上下文说明，结合向量检索与词法检索，再叠加重排序，将 RAG 系统的检索失败率从 5.7% 压低到 1.9%，降幅高达 67%。这篇文章发表于 2024 年 9 月，距今接近两年，但其中的工程思路和实验方法论在今天依然有直接的实践价值。

- 传统 RAG 的致命伤：文档切块之后为什么会"失忆"
- BM25 与向量检索的互补逻辑：语义理解 vs 精确词法匹配
- Contextual Retrieval 核心方法：用 Claude 给每个片段自动写上下文说明
- Prompt caching 如何把批量上下文生成的成本压到每百万 token 一美元出头
- 重排序（Reranking）加入之后效果如何叠加
- 实际落地的六步路径与四个高频踩坑点

---

原文：Contextual Retrieval in AI Systems
链接：https://www.anthropic.com/engineering/contextual-retrieval
发表时间：2024-09-19
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
