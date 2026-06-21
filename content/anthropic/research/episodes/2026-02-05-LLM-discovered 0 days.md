# EP303 | Claude 挖出五百个零日漏洞：AI 安全能力正式跨越临界点

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-02-05-LLM-discovered 0 days.mp3`
- 时长：22 分 54 秒

## Shownotes（复制到小宇宙）

本期我们聊一篇让人坐不住的研究报告。Anthropic 的前沿红队用 Claude Opus 四点六，在真实开源代码库里独立发现了超过五百个高危漏洞——包括沉睡了几十年的零日漏洞，而且用的是没有任何专门定制的通用模型。文章详细描述了三个发现漏洞的过程，揭示了 AI 在安全领域的真实能力边界，以及整个行业必须面对的新现实。

- 什么是零日漏洞，传统发现方法有哪些局限
- Claude 如何通过读 Git 提交历史找到 GhostScript 的不完整修复
- OpenSC 案例：AI 如何定向搜索高风险代码模式，比 fuzzer 覆盖更精准
- CGIF 案例：Claude 靠理解 LZW 算法原理构造出触发溢出的特定输入
- Anthropic 同步推出的"探针"实时检测机制，以及九十天披露窗口面临的冲击
- 对工程师的实践建议：怎样把 AI 真正用起来做安全审计，而不只是聊天

---

原文：LLM-discovered 0 days
链接：https://www.anthropic.com/research/zero-days
发表时间：2026-02-05
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
