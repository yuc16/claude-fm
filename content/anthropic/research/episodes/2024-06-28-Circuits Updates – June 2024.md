# EP137 | 拆解大模型的「词汇」：稀疏自编码器与机械可解释性的前沿战场

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2024-06-28-Circuits Updates – June 2024.mp3`
- 时长：21 分 12 秒

## Shownotes（复制到小宇宙）

本期节目解读 Anthropic 可解释性团队于 2024 年 6 月发布的研究进展报告「Circuits Updates – June 2024」。节目聚焦稀疏自编码器（SAE）这一解析大模型内部运作的核心工具，剖析 Gated SAE 与 TopK SAE 两种新架构如何解决困扰业界已久的「收缩问题」，以及 Anthropic 团队自研的 Clerp 自动评估系统如何量化特征的可解释性。

- Anthropic 可解释性团队确认：Gated SAE 和 TopK SAE 在效率和可解释性上都优于标准 L1 惩罚 SAE
- 「收缩问题」是什么，为什么它让 SAE 的特征质量打折扣
- 高密度特征并不像之前担心的那样「有毒」，在高稀疏度条件下依然可用
- Clerp：Anthropic 用自家 Claude 给自家模型做自动解释的奇妙系统
- RAVEL 基准测试：因果干预才是评估可解释性的正确姿势
- 特征过分裂（feature over-splitting）揭示 SAE 与人类直觉的深层裂缝

---

原文：Circuits Updates – June 2024
链接：https://www.anthropic.com/research/circuits-updates-june-2024
发表时间：2024-06-28
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
