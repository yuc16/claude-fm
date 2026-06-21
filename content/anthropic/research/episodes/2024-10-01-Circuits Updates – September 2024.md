# EP103 | 解剖大模型的"电路"：Anthropic 如何追踪继任者注意力头与稀疏自编码器特征粒度

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2024-10-01-Circuits Updates – September 2024.mp3`
- 时长：23 分 32 秒

## Shownotes（复制到小宇宙）

本期节目解读 Anthropic 可解释性团队在 2024 年 9 月公布的一批预研发现，聚焦两项主题：一是大语言模型中普遍存在的"继任者注意力头"，它们专门负责序数序列的接续推理；二是在稀疏自编码器（SAE）训练数据中过采样某一话题，会让模型学到该话题更细粒度特征的现象。这些发现虽是初步结果，却是理解 Transformer 内部算法的重要拼图。

- 什么是"继任者注意力头"，它如何实现"2→3""星期三→星期四"这样的接续推理
- 研究团队用四种互补方法（包括 ICA 独立成分分析）识别和分析这些注意力头
- OV 电路权重检视法的具体流程：评分最高的头约 80% 准确率，错误呈现"块状结构"
- 稀疏自编码器（SAE）是什么，以及过采样如何直接影响特征粒度
- 这两项发现对 AI 工程师调试模型、设计可解释工具的实际启示与操作建议

---

原文：Circuits Updates – September 2024
链接：https://www.anthropic.com/research/circuits-updates-sept-2024
发表时间：2024-10-01
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
