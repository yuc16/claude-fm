# EP10 | 告别上下文爆炸：Anthropic 三大新功能让 AI Agent 工具调用脱胎换骨

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-11-24-Introducing advanced tool use on the Claude Developer Platform.mp3`
- 时长：27 分 24 秒

## Shownotes（复制到小宇宙）

当 AI Agent 要同时管理几十上百个工具时，光是工具说明书就能吃掉上下文窗口的一大半，选错工具、参数出错的问题也接踵而至。2025 年 11 月，Anthropic 发布了三个专门解决这些痛点的高级功能：Tool Search Tool、Programmatic Tool Calling 和 Tool Use Examples。本期节目带你逐一拆解这三个功能的设计思路、实测数据和工程落地方法。

- Tool Search Tool 让模型按需发现工具，上下文占用减少 85%，工具选择准确率大幅提升
- Programmatic Tool Calling 用代码编排取代逐次工具调用，平均 token 消耗减少 37%
- Tool Use Examples 通过具体调用示例消除 JSON Schema 的歧义，复杂参数准确率从 72% 升至 90%
- 三个功能如何判断何时启用、何时叠加，以及工程落地的关键细节
- 延迟加载如何与 prompt caching 共存，不破坏缓存命中率
- 实际产品案例：Claude for Excel 用 PTC 处理数千行表格数据而不撑爆上下文

---

原文：Introducing advanced tool use on the Claude Developer Platform
链接：https://www.anthropic.com/engineering/advanced-tool-use
发表时间：2025-11-24
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
