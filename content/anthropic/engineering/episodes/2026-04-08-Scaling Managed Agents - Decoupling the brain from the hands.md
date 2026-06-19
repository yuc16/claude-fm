# EP6 | 大脑与双手的分离：Anthropic 如何为 AI Agent 设计一套能活过任何实现的底层架构

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2026-04-08-Scaling Managed Agents - Decoupling the brain from the hands.mp3`
- 时长：28 分 19 秒

## Shownotes（复制到小宇宙）

Anthropic 工程博客发布了一篇关于 Managed Agents 架构设计的深度实践报告，核心思路是把 AI agent 的"大脑"（Claude 与控制框架）、"双手"（沙盒与工具）和"记忆"（会话日志）彻底解耦，用稳定接口取代紧耦合的单体容器。这一架构让中位数首令牌延迟下降约六成、第九十五百分位延迟下降超过九成，同时从结构层面解决了凭证暴露的安全隐患。如果你正在构建任何 AI agent 系统，这期节目里有几个可以立刻拿去对照自己架构的工程问题。

- 所谓 harness 里的"假设"为何会随着模型升级变成死代码，以及如何系统性地避免这个问题
- "宠物与牲口"类比如何解释单体容器的运维噩梦，以及解耦如何把宠物变回牲口
- Anthropic 如何通过结构性隔离而非权限收紧来解决 prompt 注入带来的凭证泄露风险
- 会话日志作为"上下文档案馆"，如何在不丢弃任何信息的前提下处理超长任务
- 解耦带来的具体性能数据：首令牌时间的中位数和尾部延迟分别改善了多少
- 操作系统的抽象哲学如何被借鉴到 AI agent 基础设施的元框架设计中

---

原文：Scaling Managed Agents: Decoupling the brain from the hands
链接：https://www.anthropic.com/engineering/managed-agents
发表时间：2026-04-08
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
