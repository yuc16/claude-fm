# EP133 | 当 AI 排行榜不说误差：用统计学给模型评测补上最重要的一关

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2024-11-19-A statistical approach to model evaluations.mp3`
- 时长：26 分 37 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 于二〇二四年十一月发表的研究论文《Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations》。文章用严格的统计学框架，系统分析了 AI 模型评测中长期被忽视的测量误差问题——那个让所有排行榜看起来精准，却可能只是幻觉的漏洞。

- 为什么"模型 A 比模型 B 高两个百分点"这句话可能完全站不住脚
- 中心极限定理如何帮我们给每个评测分数附上置信区间
- 题目聚类陷阱：阅读理解类评测的统计误差可能被低估三倍以上
- 两种主动降低测量噪声的工程方法：多次重采样与 token 概率评分
- 配对差异分析：同一批题目同时测两个模型，能免费获得更高的统计精度
- 功效分析：跑评测之前先算清楚，这批题目到底够不够用

---

原文：A statistical approach to model evaluations
链接：https://www.anthropic.com/research/statistical-approach-to-model-evals
发表时间：2024-11-19
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
