# EP545 | Claude Projects 重新设计：从文件夹到对话，让 AI 自己协调工作

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-09-17-Projects redesigned - from folder to conversation - Claude by Anthropic.mp3`
- 时长：33 分 26 秒

## Shownotes（复制到小宇宙）

Anthropic 在九月十七日给 Claude Projects 做了一次彻底改版：它不再是一个装文件的文件夹，而是一个由 coordinator 指挥、多个 thread 并行执行的工作系统。你只需要说清目标，拆解、分工、并行、审查、汇总全部交给 Claude，而且它在你关掉电脑之后还在跑。

本期我们把这篇五分钟的产品文章拆成二十五分钟来讲透，重点回答一个问题：当 AI 不只是写代码，而是开始管理一堆 AI 写代码的工作时，我们工程师的位置应该放到哪里。

本期要点：
- Projects 的本质变化是从静态上下文容器变成动态编排系统，coordinator 负责拆解和调度，thread 负责执行
- 每个 thread 是一个独立的 Claude Code 云端会话，有自己的分支和仓库副本，多个 thread 改到同一块代码会以合并冲突的形式暴露
- 共享记忆让不同 thread 之间不再需要人工搬上下文，甚至能记住你的沟通偏好，但也带来记忆污染和漂移的风险
- 并行会更快触及用量上限，好在可以给 coordinator 和 worker 分别配置模型和投入程度来做成本分层
- 发布节奏：先 Pro 和 Max 的部分用户，再扩到全部 Claude Code 用户，Team 和 Enterprise 排在后面，现有 project 不受影响
- 真正的瓶颈会从「能不能做」变成「你能审查多少」，这道天花板值得每个团队提前想清楚

---

原文：Projects redesigned: from folder to conversation | Claude by Anthropic
链接：https://claude.com/blog/projects-redesigned
发表时间：2026-09-17
本期解读由模型（deepseek-v4-flash）生成，音频由 edge-tts 合成。
