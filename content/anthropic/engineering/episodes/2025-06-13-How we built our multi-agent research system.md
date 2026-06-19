# EP17 | Anthropic 如何把研究性能提升九成：多智能体系统的工程实战全拆解

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-06-13-How we built our multi-agent research system.mp3`
- 时长：34 分 08 秒

## Shownotes（复制到小宇宙）

Anthropic 工程团队用这篇文章记录了 Claude Research 功能——也就是那个能自主联网做深度研究的功能——从原型走向生产系统的完整历程。这是目前公开资料里少有的、来自真正跑在生产环境里的多智能体系统的第一手工程经验，涵盖架构设计、提示词工程、评测策略和生产运维的全链路。

- 多智能体系统凭什么能把研究性能提升 90%：token 并行消耗才是核心，而不是"更聪明"
- 八条经过实战验证的 agent 提示词工程原则，包括如何教会主导 agent 分工、如何让 agent 改进工具描述
- 为什么从二十个测试样本就能开始评测，以及 LLM-as-judge 的正确打开方式
- 生产系统的四大挑战：有状态错误累积、非确定性调试、彩虹部署、同步瓶颈
- 多智能体适合哪些任务、不适合哪些任务，以及 15 倍 token 消耗的经济账怎么算

---

原文：How we built our multi-agent research system
链接：https://www.anthropic.com/engineering/multi-agent-research-system
发表时间：2025-06-13
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
