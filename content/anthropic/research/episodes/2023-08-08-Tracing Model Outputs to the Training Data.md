# EP125 | 影响函数：Anthropic 如何把大模型的每句话追溯到训练数据源头

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2023-08-08-Tracing Model Outputs to the Training Data.mp3`
- 时长：21 分 45 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 二零二三年的研究论文《Tracing Model Outputs to the Training Data》。团队把经典统计工具"影响函数"扩展到了五百亿参数级别的大语言模型，让我们首次能够定量地问出：模型说的每句话，到底和哪些训练数据最相关？这篇文章距今将近三年，但它提出的问题框架和研究路径，至今仍是可解释性领域最重要的方向之一。

- 什么是影响函数，核心思路是"反事实假设"——如果多加一份训练样本，输出会变多少
- Anthropic 如何克服"逆海森向量积"这个计算天堑，把影响函数扩展到五百二十亿参数
- 核心发现：模型越大，泛化越抽象——小模型找词，大模型找意思
- 跨语言影响随规模显著增强，说明大模型有超越语言形式的内部概念表征
- 影响分布呈幂律分布，模型不是在背课文，而是扩散式地吸收大量来源
- 影响力在网络层间的分布规律：底层管词汇风格，中间层管抽象主题

---

原文：Tracing Model Outputs to the Training Data
链接：https://www.anthropic.com/research/influence-functions
发表时间：2023-08-08
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
