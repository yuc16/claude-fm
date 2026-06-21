# EP275 | Bloom：用 AI 生成测试题来评估 AI，Anthropic 如何破解行为评估的污染难题

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-12-19-Introducing Bloom - an open source tool for automated behavioral evaluations.mp3`
- 时长：28 分 04 秒

## Shownotes（复制到小宇宙）

Anthropic 开源了一个叫 Bloom 的行为评估框架，能把原本需要几周手工完成的 AI 安全测试，压缩到几天之内自动完成。本期我们拆解 Bloom 的四步流水线架构，聊聊它如何解决测试集污染问题，以及它在"自我偏好偏见"这个案例上发现的一个有趣新结论。

- 为什么传统行为评估又慢又脆：污染、过时、扩展难
- Bloom 的四步流水线：理解 → 构想 → 执行 → 判断，每步的设计逻辑
- 可靠性验证：10 个模型生物体测试 9 个通过，Opus 4.1 与人类判断相关系数 0.86
- 案例研究：自我偏好偏见，以及"更深的推理让模型选择回避而非公正"的新发现
- 实践上手指南：种子文件写法、judge 模型选择、二级维度过滤、引用规范

---

原文：Introducing Bloom: an open source tool for automated behavioral evaluations
链接：https://www.anthropic.com/research/bloom
发表时间：2025-12-19
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
