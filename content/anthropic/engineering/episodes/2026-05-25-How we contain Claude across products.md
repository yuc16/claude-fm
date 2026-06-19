# EP2 | 给 AI Agent 套上笼头：Anthropic 三大产品的安全边界工程实录

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2026-05-25-How we contain Claude across products.mp3`
- 时长：27 分 58 秒

## Shownotes（复制到小宇宙）

Anthropic 工程团队公开了一篇难得的"踩坑实录"——过去两年里，他们在 claude.ai、Claude Code 和 Claude Cowork 三款产品上，如何设计 AI agent 的安全边界、遭遇了哪些真实安全事故、又是怎么一步步修复的。这期节目把文章里最硬核的工程细节和教训，用通俗的方式拆解清楚。

- 爆炸半径思维：为什么 AI agent 越强大，控制"出了问题最多坏多少"比控制"出问题概率"更重要
- 三层防御体系：环境层、模型层、外部内容层各自能做什么、不能做什么
- 审批疲劳的工程真相：93% 批准率背后，人工审核机制是如何走向失效的
- 两个震撼的真实事故：员工被钓鱼导致 AWS 凭证泄露，允许列表被 api.anthropic.com 绕过
- 给工程师的实践建议：凭证隔离、出口控制、把允许列表理解为"能力授权"而非"目标过滤器"

---

原文：How we contain Claude across products
链接：https://www.anthropic.com/engineering/how-we-contain-claude
发表时间：2026-05-25
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
