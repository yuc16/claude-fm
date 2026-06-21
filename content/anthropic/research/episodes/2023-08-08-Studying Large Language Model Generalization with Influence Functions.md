# EP37 | 训练数据的指纹：用影响函数追溯大语言模型行为的来源

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2023-08-08-Studying Large Language Model Generalization with Influence Functions.mp3`
- 时长：20 分 37 秒

## Shownotes（复制到小宇宙）

本期节目解读 Anthropic 于二零二三年八月发表的研究论文"用影响函数研究大语言模型的泛化能力"。影响函数是一种追踪"哪些训练数据导致了某个模型行为"的数学工具，本期将带你了解 Anthropic 如何把它扩展到五百亿参数量级的大模型上，以及他们在实验中发现的六个关键泛化规律。注意：这篇论文距今约三年，是在 AI 黑箱之争刚刚进入主流视野时发表的，放在那个时间节点上，它的意义尤其深远。

- 影响函数的核心思想：通过反事实推断，定量衡量某条训练数据对模型特定行为的贡献
- EK-FAC 技术突破：用 Kronecker 分解近似黑塞矩阵，让影响函数首次可扩展到五百亿参数的大模型
- 影响模式高度稀疏：少数几条关键训练数据决定了模型大部分的特定行为
- 规模带来更抽象的泛化：模型越大，从字面匹配演进为跨领域的概念层面关联
- 跨语言共享语义空间：英文训练数据实质上影响着中文任务，双向影响需要警惕
- 令人惊讶的词序局限：关键短语顺序颠倒后影响力几乎归零，揭示大模型的表面统计本质

---

原文：Studying Large Language Model Generalization with Influence Functions
链接：https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions
发表时间：2023-08-08
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
