# EP9 | 神经网络神经元开口说人话：Anthropic 用一个激活函数让 AI 可解释性提升七成

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2022-06-17-Softmax Linear Units.mp3`
- 时长：25 分 04 秒

## Shownotes（复制到小宇宙）

本期聚焦 Anthropic 于二〇二二年发表的基础性研究《Softmax Linear Units》。研究者仅凭一个名为 SoLU 的激活函数改动，就让 MLP 层中可解释神经元的比例从约 35% 跃升至约 60%，且几乎不损失模型性能。这是 Anthropic 机制可解释性研究路线的重要里程碑，也是日后稀疏自编码器等工作的直接先驱。

- 多义性困境：为什么绝大多数神经网络神经元同时响应多个毫不相关的概念
- 叠加假说（Superposition Hypothesis）：神经网络如何用比神经元数量更多的"特征"来表达世界
- SoLU 的核心机制：用 softmax 竞争迫使神经元稀疏激活，让单个神经元更专一
- 随机双盲实验验证：可解释神经元比例大幅提升，性能几乎零代价
- 没有免费的午餐：LayerNorm 如何被用来"走私"不可解释特征，问题比想象中更深
- 历史坐标：这篇文章在 ChatGPT 之前、SAE 之前，开创了"为可解释性而设计架构"的研究路线

---

原文：Softmax Linear Units
链接：https://www.anthropic.com/research/softmax-linear-units
发表时间：2022-06-17
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
