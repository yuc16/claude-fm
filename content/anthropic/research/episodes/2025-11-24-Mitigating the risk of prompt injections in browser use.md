# EP73 | 浏览网页的 AI Agent 如何被黑：提示词注入攻击与防御全解

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-11-24-Mitigating the risk of prompt injections in browser use.mp3`
- 时长：24 分 49 秒

## Shownotes（复制到小宇宙）

本期我们拆解 Anthropic 在 2025 年底发布的一篇安全研究：当 AI Agent 代替你上网操作，网页上藏着的恶意指令能悄悄劫持它的行为——这就是提示词注入攻击。Anthropic 公布了 Claude Opus 4.5 的实测攻击成功率，并坦承这个问题尚未解决。

- 什么是 prompt injection，为什么它比 SQL 注入更难防
- 浏览器 Agent 的攻击面有多大，能力越强风险越高
- Anthropic 三条防线：强化学习训练、外部分类器、人工红队
- Claude Opus 4.5 攻击成功率降至约 1%，但这意味着什么
- 工程师如何在自己的 Agent 系统里落地纵深防御
- 为什么"过度宣传安全性"在 AI 时代特别危险

---

原文：Mitigating the risk of prompt injections in browser use
链接：https://www.anthropic.com/research/prompt-injection-defenses
发表时间：2025-11-24
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
