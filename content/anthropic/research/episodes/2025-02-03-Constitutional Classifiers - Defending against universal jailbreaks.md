# EP127 | 用宪法给大模型装安检：Anthropic 防御通用越狱实验全解析

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-02-03-Constitutional Classifiers - Defending against universal jailbreaks.mp3`
- 时长：26 分 25 秒

## Shownotes（复制到小宇宙）

当大模型能力越来越强，越狱攻击的危害也在急剧升级——Anthropic 用「宪法分类器」技术，在模型外部构建了一套可配置的独立安全守卫。本期我们深入拆解这篇二〇二五年二月发表的研究论文，讲清楚它的工作原理、红队测试数据、公开演示的破与防，以及对一线 AI 工程师的实际意义。

- 越狱攻击为何十年未解：模型安全训练的根本局限在哪里
- 宪法分类器的核心架构：输入输出双层守卫 + AI 生成合成数据训练
- 原型系统红队测试：183 人、3000+ 小时，无人实现通用越狱
- 改进版自动化评估：越狱成功率从 86% 降至 4.4%，过拒率仅增 0.38%
- 公开演示七天实录：339 名安全研究者、30 万次对话，最终一人突破
- 对 AI 应用开发者的启示：安全层架构设计、合成数据与对抗测试实践

---

原文：Constitutional Classifiers: Defending against universal jailbreaks
链接：https://www.anthropic.com/research/constitutional-classifiers
发表时间：2025-02-03
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
