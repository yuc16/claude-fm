# EP210 | 

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-05-12-How Anthropic's cybersecurity team built a threat detection platform with Claude Code.mp3`
- 时长：25 分 06 秒

## Shownotes（复制到小宇宙）

这一期我们聊 Anthropic 内部安全团队的真实故事：他们怎么用 Claude Code 在几周内搭出一套叫 CLUE 的威胁检测平台，把警报分诊和深入调查都交给 Claude 来做。文章给出了详细的量化数据，误报率从三分之一降到百分之七，三十天内自动完成的工作量相当于人工二百三十四人天。我们还会聊聊团队从实践中得出的一个反直觉经验：给 Claude 设定边界但放开具体调查策略，效果反而更好。

本期要点：
- CLUE 是什么：Claude Looks Up Evidence，一个用自然语言连接公司内部系统的威胁检测平台
- CLUE Triage 如何借助 Slack、内部文档、代码仓库等上下文，给每条警报打分诊标签和置信度分数
- CLUE Investigate 用智能体并行查询，三到四分钟完成原本要耗费数小时甚至半天的人工调查
- 量化效果：误报率从三分之一降到百分之七，三十天自动完成相当于二百三十四人天的工作量，效率提升五到十倍
- 苦涩的教训：为什么给 Claude 划定边界、但放开调查策略，比写死每一步流程效果更好
- CLUE 的下一步：从被动响应转向主动巡查，并主动拥抱调查路径的非确定性

---

原文：How Anthropic's cybersecurity team built a threat detection platform with Claude Code
链接：https://claude.com/blog/how-anthropic-uses-claude-cybersecurity
发表时间：2026-05-12
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
