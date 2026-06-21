# EP322 | AI Agent三大工作流模式全解析：顺序、并行与评估优化

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-03-05-Common workflow patterns for AI agents.mp3`
- 时长：20 分 46 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊Anthropic官方博客上一篇关于AI agent工作流模式的文章。文章核心观点是，构建agent系统时不需要发明复杂架构，绝大多数生产场景用顺序、并行、评估优化这三种模式就能覆盖。我们会逐一拆解每种模式的适用场景、典型例子、容易踩的坑，以及怎么把它们组合起来用。

本期要点：
- 工作流不是限制agent自主性，而是给自主性划定边界，就像装配线上每个工位的工人仍有自主决策空间
- 顺序工作流适合有明确依赖关系的多阶段任务，比如先提取数据再校验再入库
- 并行工作流适合可以拆分成独立子任务、且需要速度或多角度判断的场景，比如多agent代码审查
- 评估优化工作流把生成和评估拆成两个角色，适合有明确可衡量质量标准的任务，比如代码生成、客户邮件撰写
- 选择模式前先用单一agent试一遍，能满足质量要求就别加复杂度
- 三种模式可以互相嵌套组合，关键是匹配实际需求而不是为了用而用

---

原文：Common workflow patterns for AI agents
链接：https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
发表时间：2026-03-05
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
