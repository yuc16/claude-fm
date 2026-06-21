# EP11 | 攻破大模型的防线：Anthropic 红队测试揭示的 AI 安全真相

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2022-08-22-Red Teaming Language Models to Reduce Harms - Methods, Scaling Behaviors, and Lessons Learned.mp3`
- 时长：21 分 15 秒

## Shownotes（复制到小宇宙）

这期节目解读 Anthropic 在二〇二二年发表的红队测试开创性论文，该研究首次系统地回答了一个关键问题：大语言模型越大是否越安全？他们雇佣测试员对四种不同配置的模型展开"攻击"，发现 RLHF 对齐训练是唯一随规模增大而显著变得更安全的方案。论文同时开源了近四万条攻击样本数据集，成为整个行业 AI 安全评估的基础参考。

- 什么是红队测试，它和普通的安全测试有什么本质区别
- 四种模型配置的对比实验：普通 LM、提示词安全、拒绝采样、RLHF 各有什么弱点
- 规模越大并不等于越安全，唯一的例外是 RLHF 模型
- 近四万条攻击数据集背后，哪些"微妙伤害"最难被发现
- 对齐税是否真实存在：安全和能力真的是鱼和熊掌吗
- 对今天做 AI 产品的工程师，这篇三年前的论文仍有哪些可操作的启发

---

原文：Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned
链接：https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned
发表时间：2022-08-22
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
