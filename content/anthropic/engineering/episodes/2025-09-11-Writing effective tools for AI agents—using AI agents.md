# EP200 | 给 AI Agent 写工具不等于封装 API：Anthropic 评估驱动的实战设计方法论

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-09-11-Writing effective tools for AI agents—using AI agents.mp3`
- 时长：26 分 19 秒

## Shownotes（复制到小宇宙）

Anthropic 工程团队在内部大量实验的基础上，总结出一套为 AI agent 设计高效工具的方法论。本期节目深入拆解这篇发表于二〇二五年九月的工程文章，从搭原型、跑评估、与 agent 协作优化，到五大设计原则逐一落地，帮你少走弯路。

- 工具是确定性系统与非确定性 agent 之间的新型契约，需要全新的设计思维
- 评估驱动迭代：用真实、复杂的任务生成评估集，而不是简化的沙盒环境
- 用 agent 分析 agent 的对话记录，自动化识别工具的问题并批量重构
- 工具不是越多越好，合并高频工作流，减少 agent 上下文消耗
- 命名空间、语义化标识符、响应格式枚举——这些细节对评估结果有显著影响
- 工具描述是主动引导 agent 行为的手段，精准的描述可以带来质的性能提升

---

原文：Writing effective tools for AI agents—using AI agents
链接：https://www.anthropic.com/engineering/writing-tools-for-agents
发表时间：2025-09-11
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
