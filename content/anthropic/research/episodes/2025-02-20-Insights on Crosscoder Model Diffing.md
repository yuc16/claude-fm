# EP129 | 一张特征差分图，读懂大模型微调到底改了什么

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-02-20-Insights on Crosscoder Model Diffing.mp3`
- 时长：26 分 08 秒

## Shownotes（复制到小宇宙）

本期节目深度解读 Anthropic 可解释性团队二〇二五年二月发布的研究报告《Insights on Crosscoder Model Diffing》，中文译为"跨编码器模型差分的若干洞见"。文章提出了一套在特征层面对比两个语言模型内部差异的工具，不只看行为输出，而是直接"X 光透视"模型内部，找出微调前后究竟增加了什么、消失了什么——甚至成功揪出了一个被注入恶意行为的"睡眠特工"模型。

- Crosscoder 是稀疏自编码器（SAE）的跨模型扩展，能同时为两个模型学习一套共享特征词典
- Model Diffing（模型差分）的核心目标：把微调前后的内部特征差异可视化，识别新增与消失的行为
- 关键意外发现：专有特征普遍比共享特征更"多义"、激活密度更高，难以解读，约高出一个数量级
- 根本原因是特征容量竞争：共享特征效率更高，把专有特征挤进了更少的位置
- 改进方案：引入"指定共享特征"（DSF），有效恢复专有特征的单义性和可解释性
- 真实应用：成功识别助手微调引入的礼仪行为特征，以及"睡眠特工"模型中约九成的有害行为特征

---

原文：Insights on Crosscoder Model Diffing
链接：https://www.anthropic.com/research/crosscoder-model-diffing
发表时间：2025-02-20
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
