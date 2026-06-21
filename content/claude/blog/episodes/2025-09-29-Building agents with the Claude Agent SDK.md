# EP298 | 给 Claude 一台电脑:解读 Claude Agent SDK 的智能体构建之道

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-09-29-Building agents with the Claude Agent SDK.mp3`
- 时长：24 分 16 秒

## Shownotes（复制到小宇宙）

本期我们聊聊 Anthropic 在二零二五年九月发布的这篇文章,主角是从 Claude Code SDK 改名而来的 Claude Agent SDK。文章的核心思路很简单也很颠覆:不要只给模型一个提示词,而是给它一台电脑,让它像程序员一样工作。我们会拆解智能体的"收集上下文、采取行动、验证结果"三段循环,聊聊文件系统、子智能体、代码生成、MCP 协议这些具体机制怎么落地,最后聊聊普通开发者今天能怎么上手用。

本期要点:
- Claude Code 为什么从一个编程工具,演变成了几乎所有 Anthropic 内部智能体的底层引擎
- 智能体的核心工作循环:收集上下文、采取行动、验证工作、循环往复
- 文件系统即上下文工程,agentic search 与语义搜索的取舍
- 子智能体如何做到并行处理与上下文隔离
- 工具设计、Bash、代码生成和 MCP 协议各自的角色分工
- 三种验证方式:规则反馈、视觉反馈、模型当裁判,以及怎么给智能体做体检

---

原文：Building agents with the Claude Agent SDK
链接：https://claude.com/blog/building-agents-with-the-claude-agent-sdk
发表时间：2025-09-29
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
