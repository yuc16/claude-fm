# EP31 | 当 AI 开口说话，代表的是谁的声音——大模型全球观点偏见量化解构

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2023-06-29-Towards Measuring the Representation of Subjective Global Opinions in Language Models.mp3`
- 时长：22 分 12 秒

## Shownotes（复制到小宇宙）

本期深入解析 Anthropic 二〇二三年六月发表的研究：大型语言模型在回答价值观与社会议题时，默认代表哪些人群的声音？研究者构建了 GlobalOpinionQA 数据集，通过三组精心设计的实验，系统揭示了主流 LLM 存在 WEIRD（西方化、富裕化）文化偏向，以及语言翻译并不等于文化适配的关键发现。

- GlobalOpinionQA 数据集的来源：皮尤全球态度调查与世界价值观调查的两千五百五十六道题
- 詹森-香农距离如何把"模型像哪国人"变成一个可量化的数字
- 默认状态下，主流 LLM 最接近美国、加拿大、澳大利亚等 WEIRD 国家的观点
- 国家视角提示（Country Prompting）有效但危险：会触发文化刻板印象而非真实理解
- 语言提示实验：把问题翻译成俄语，模型依然更像美国人，语言不等于文化
- 对工程师的实践指导：多语言产品如何识别和规避系统性文化偏见

---

原文：Towards Measuring the Representation of Subjective Global Opinions in Language Models
链接：https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models
发表时间：2023-06-29
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
