# EP27 | 生物学的老城窄巷：AI智能体为何需要一条确定性数据基础设施高速路

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-06-08-Paving the way for agents in biology.mp3`
- 时长：31 分 52 秒

## Shownotes（复制到小宇宙）

Anthropic 研究者 Laura Luebbert 团队发布了一项关于科学 AI agent 的重要研究：用 VirBench 基准测试发现，当前最强模型在无工具辅助的病毒序列检索任务中，准确率仅有 16.9% 到 91.3%，且同一问题三次问得到三个差异极大的答案。当他们为 agent 配备 gget virus 这个确定性检索工具后，所有模型准确率均突破 90%，最高达 99.7%。这揭示了一个对所有 AI 工程师都适用的核心洞见：在高准确性要求的领域，好的工具层可以对冲模型能力的差距，让模型的选择变得不那么重要。

- 生物数据基础设施像为人类设计的老城窄巷，AI agent 再强也难以可靠导航——瓶颈不在推理，在确定性执行层的缺失
- VirBench 测试：Claude Sonnet 4 对同一埃博拉序列检索题三次分别返回 106、15、5 条，正确答案是 266 条
- 序列数据不完整导致进化树推算的最近共同祖先时间出现百年偏差：1922 年 vs. 正确的 2014 年
- gget virus 确定性检索层加入后，GPT-5.5 准确率达 99.7%，模型间性能差距大幅缩小
- 核心结论：加上确定性检索层，模型的选择变得不那么重要了——便宜模型加正确工具胜过昂贵模型裸奔
- 对 AI 工程师的启示：高准确性任务中，先在模型和数据源之间加入确定性工具层，而不是换更强的模型

---

原文：Paving the way for agents in biology
链接：https://www.anthropic.com/research/agents-in-biology
发表时间：2026-06-08
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
