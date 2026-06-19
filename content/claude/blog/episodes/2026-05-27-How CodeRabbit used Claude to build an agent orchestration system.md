# EP195 | 规划优先于代码：CodeRabbit 如何用 Claude 解决「AI 写出来的东西能跑但不对」的老大难问题

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-05-27-How CodeRabbit used Claude to build an agent orchestration system.mp3`
- 时长：25 分 39 秒

## Shownotes（复制到小宇宙）

本期我们拆解 Anthropic 官方博客"初创公司如何用 Claude 构建产品"系列的最新案例——AI 代码审查平台 CodeRabbit。他们发现 AI 编码工具最普遍的失败模式不是代码有 bug，而是代码能编译、测试能通过，却压根没做对事情。为了解决这个问题，他们用 Claude 构建了一套多模型 agent 编排系统，在任何代码生成之前先跑一个结构化的规划阶段。

- CodeRabbit 发现的核心问题：开发者把隐性知识当成默认假设传给 AI，AI 填补空白的方式和人完全不同
- David Loker 亲历的「没有登录页面」事故，揭示了为什么晚发现问题在 AI 工作流里代价极高
- 用 Opus 做战略规划、Sonnet 做结构化分解、Haiku 做具体执行的三层模型分配策略
- 如何评估「一份规划的好坏」：从手工标注到 LLM 评判系统，以及有无规划阶段的对照实验
- 规划颗粒度的悖论：太细会过时，太粗留给 agent 填充空间，找到那个刚好的抽象层次需要评估基础设施
- 对个人开发者和团队的五条实践建议，以及 AI 时代瓶颈转移的宏观判断

---

原文：How CodeRabbit used Claude to build an agent orchestration system
链接：https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system
发表时间：2026-05-27
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
