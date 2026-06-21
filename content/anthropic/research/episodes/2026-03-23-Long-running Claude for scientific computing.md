# EP335 | 让 Claude 自主工作数天：科学计算中的长时 Agent 工程实践

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-03-23-Long-running Claude for scientific computing.mp3`
- 时长：25 分 20 秒

## Shownotes（复制到小宇宙）

Anthropic Discovery 团队研究员用 Claude Opus 4.6，在几天内实现了一个宇宙学玻尔兹曼求解器——这类任务通常需要领域专家团队花费数月乃至数年。本期拆解他的完整工作流：CLAUDE.md + CHANGELOG.md 双文档架构、测试预言机设计、HPC 集群配置，以及如何用"Ralph 循环"对抗 Agent 的"拖延症"。

- 从"对话式"到"自主式"：现在的模型已经强到可以让你睡觉时 Agent 还在写代码
- CLAUDE.md 作为"项目大脑"，CHANGELOG.md 记录失败方案，两者合力构成跨会话的持久化记忆
- 测试预言机是自主运行的核心：没有量化的成功标准，Agent 就没有前进方向
- Ralph 循环：一个 for 循环，专门用来对付 Agent 找借口提前收工
- 通过跟踪 git 提交历史，非领域专家也可以"渗透式"学习一个新领域的知识
- 机会成本的认知转变：每个没有让 Agent 工作的夜晚，都是潜在进展的浪费

---

原文：Long-running Claude for scientific computing
链接：https://www.anthropic.com/research/long-running-Claude
发表时间：2026-03-23
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
