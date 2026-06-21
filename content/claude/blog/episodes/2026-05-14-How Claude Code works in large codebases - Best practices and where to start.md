# EP401 | 大代码库驯服指南:为什么工具链比模型更重要

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-05-14-How Claude Code works in large codebases - Best practices and where to start.mp3`
- 时长：27 分 44 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊 Anthropic 官方发布的最新文章,主题是如何在大型代码库里用好 Claude Code。文章基于 Anthropic 应用 AI 团队跟一大批企业客户合作的一线经验,总结出在百万行级单体仓库、跨越数十年的遗留系统、分布式微服务架构里,真正能让 Claude Code 落地见效的配置模式和组织打法。如果你的团队也在大代码库里纠结要不要上手 AI 编程工具,或者用了但效果一般,这期内容值得收藏。

本期要点
- Claude Code 用的是 agentic search,而不是 RAG 检索,不需要维护索引,天然适配持续变化的大代码库
- 决定 Claude Code 表现好坏的不只是模型本身,更是围绕模型搭建的 harness,包括 CLAUDE.md、hooks、skills、plugins、MCP 服务器
- LSP 语言服务器集成能让 Claude 按符号而不是按字符串搜索,是多语言代码库里投入产出比最高的一项工作
- CLAUDE.md 要保持精简分层,按子目录划定测试和构建命令,根目录别堆太多内容
- 配置不是一次性的,要随着模型迭代每三到六个月做一次复查,避免过去的补丁反而限制了新模型
- 大规模落地离不开组织层面的责任人,无论是专职的 agent manager,还是最低限度的 DRI

---

原文：How Claude Code works in large codebases: Best practices and where to start
链接：https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
发表时间：2026-05-14
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
