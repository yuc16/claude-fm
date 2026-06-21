# EP24 | 分布式表示的两种灵魂：神经网络里的组合与叠加之争

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2023-05-04-Distributed Representations - Composition & Superposition.mp3`
- 时长：23 分 04 秒

## Shownotes（复制到小宇宙）

Anthropic 研究员 Chris Olah 在这篇非正式笔记中揭示了一个长期被混淆的概念：人们口中的"分布式表示"其实暗含两种截然不同的策略——"组合"（composition）与"叠加"（superposition）。这两种策略不仅数学性质迥异，而且在根本上相互竞争，不能简单地看成一个光谱的两端。理解它们的区别，是迈向神经网络机械可解释性的基础一步。

- 分布式表示有两个完全不同的含义：组合型表示用独立特征拼装复杂概念，叠加型表示把多于神经元数量的特征挤进同一空间
- 组合型表示：泛化性强、线性可读，Word2Vec 的词向量方向就是经典案例
- 叠加型表示：信息密度极高，但神经元因此变得多义，难以线性探查
- 两者根本性地竞争同一块指数级的"体积资源"，没有两全其美
- 稀疏性是关键中介：特征激活越稀疏，叠加和组合越能和平共存，这与压缩感知理论高度吻合
- 这对 AI 可解释性、SAE 稀疏自编码器、prompt 工程和模型微调都有直接的实践含义

---

原文：Distributed Representations: Composition & Superposition
链接：https://www.anthropic.com/research/distributed-representations-composition-superposition
发表时间：2023-05-04
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
