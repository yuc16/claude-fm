# EP21 | 残差流的秘密：Adam 优化器如何在神经网络里制造"特权坐标"

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2023-03-16-Privileged Bases in the Transformer Residual Stream.mp3`
- 时长：24 分 07 秒

## Shownotes（复制到小宇宙）

本期拆解 Anthropic 二〇二三年三月发表的一篇机械可解释性研究。Transformer 的残差流，数学理论上应该是旋转对称的——也就是说坐标轴不该有任何特殊意义。但实验结果完全相反。Anthropic 挨个排查了三个嫌疑人，最终把"锅"甩给了 Adam 优化器里一个几乎所有人都在用、却很少有人深想过的设计。

本期要点：
- 什么是残差流，为什么它是 Transformer 信息流通的核心通道
- "特权基底"是什么意思，旋转对称性和可解释性研究有什么关系
- 三个嫌疑人：Layer Normalization、浮点数精度、Adam 优化器——前两个怎么被排除
- Adam 的 per-dimension 归一化机制为什么会打破旋转对称性，直觉类比解释
- 这个发现对 logit lens、激活值修补、稀疏自编码器等工具意味着什么
- 实践启发：做模型分析、模型合并、AI 安全探针时各该注意什么

---

原文：Privileged Bases in the Transformer Residual Stream
链接：https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
发表时间：2023-03-16
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
