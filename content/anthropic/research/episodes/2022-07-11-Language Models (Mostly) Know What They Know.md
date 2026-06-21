# EP10 | AI 知道自己不知道什么吗？Anthropic 早期研究揭示语言模型的元认知之路

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2022-07-11-Language Models (Mostly) Know What They Know.mp3`
- 时长：22 分 24 秒

## Shownotes（复制到小宇宙）

这期我们聊一篇 Anthropic 在 2022 年发布的研究论文——《语言模型（大多数情况下）知道自己知道什么》。文章探讨的核心问题是：大语言模型能不能准确评估自己答案的可信度，以及在回答之前就预测自己是否有能力回答某道题？这些发现不仅是"诚实 AI"训练方向的奠基之作，对今天做 RAG、agent 和生产部署的工程师依然有直接的实践指导价值。

- 模型越大，自我校准能力越好——大模型不仅答得准，还更清楚自己哪里不准
- P(True) 框架：先生成答案，再让模型评估这个答案是否正确，可实现开放域自我审核
- 自洽性加成：让模型先看多个候选答案再评估，准确度进一步提升
- P(IK)（"我知道"概率）：在生成答案之前就预测能否回答，是控制模型"答或不答"的关键机制
- 上下文能动态提升 P(IK)：加入相关文档或提示，模型会理性地变得更有把握，RAG 系统可借此优化检索策略
- 跨任务泛化有限：P(IK) 在新任务类型上校准会下降，需要重新验证而不是想当然复用

---

原文：Language Models (Mostly) Know What They Know
链接：https://www.anthropic.com/research/language-models-mostly-know-what-they-know
发表时间：2022-07-11
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
