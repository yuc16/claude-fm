# EP241 | MCP 工具一多代理就变慢变贵？用代码执行模式砍掉九成九的 token 消耗

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-11-04-Code execution with MCP - building more efficient AI agents.mp3`
- 时长：23 分 50 秒

## Shownotes（复制到小宇宙）

本期我们精读 Anthropic 工程团队二〇二五年十一月发布的一篇实践文章，讨论随着 MCP 服务器越接越多，传统直接工具调用模式如何造成 token 爆炸和响应延迟。文章提出"代码执行模式"作为解法，通过让代理写代码来调用 MCP 工具，将 token 消耗从十五万骤降到两千，省掉九成九，同时还能带来更好的数据隐私保护与状态管理能力。

- MCP 是什么，为什么在一年内就成为 AI 代理接外部工具的事实标准
- 大规模使用 MCP 的两大痛点：工具定义全量预加载导致 token 爆炸，以及中间数据反复流过模型的额外消耗
- 核心解法：把 MCP 服务器表示为文件树，用"按需读文件"代替"预加载全量工具定义"，实测省掉九成九的 token
- 数据过滤下沉到代码执行环境，让模型只看处理后的结果而非原始万行数据
- 安全红利：中间数据默认不过模型，PII 自动令牌化防止敏感信息意外暴露给模型
- 文章坦诚的代价提示：代码执行需要安全沙箱与运维投入，并非所有规模都适用

---

原文：Code execution with MCP: building more efficient AI agents
链接：https://www.anthropic.com/engineering/code-execution-with-mcp
发表时间：2025-11-04
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
