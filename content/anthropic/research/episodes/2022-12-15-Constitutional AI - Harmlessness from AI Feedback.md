# EP14 | 让 AI 自我约束：Constitutional AI 如何用一部原则清单训练无害但不回避的智能助手

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2022-12-15-Constitutional AI - Harmlessness from AI Feedback.mp3`
- 时长：24 分 41 秒

## Shownotes（复制到小宇宙）

这篇来自 Anthropic 的研究论文提出了「宪法式人工智能」——一套不依赖大量人工标注、而是让 AI 依据明确原则自我批评、自我修订的对齐方法。它分成两个阶段：先用监督学习做自我改写，再用 AI 反馈替代人类反馈做强化学习。这套方法深刻影响了 Claude 系列模型的训练方式，理解它，就是理解现代 AI 助手「为什么这样说话」的钥匙。

- 「宪法」是什么：一份人类写好的原则清单，替代逐条人工标注来约束 AI 行为
- 监督学习阶段：让 AI 用宪法原则批评自己的输出，再自我修订，用修订后的数据做微调
- RLAIF：用 AI 替代人类做偏好评估，训练奖励模型，再用强化学习进一步对齐
- 思维链推理的双重价值：既提升输出质量，也让 AI 决策过程对人类可见可审查
- 「无害但不回避」：区分「沉默拒绝」和「解释顾虑后仍然有用」这两种完全不同的设计目标
- 对从业者的启发：在 prompt 工程里复用这套自我检查思路，以及 RLAIF 放大偏见的潜在风险

---

原文：Constitutional AI: Harmlessness from AI Feedback
链接：https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
发表时间：2022-12-15
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
