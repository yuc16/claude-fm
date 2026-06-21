# EP75 | Claude 提示词生成器：让写 prompt 这件事不再靠玄学

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2024-05-20-Generate better prompts in the developer console.mp3`
- 时长：17 分 00 秒

## Shownotes（复制到小宇宙）

这一期我们聊一篇来自 Anthropic 官方博客的老文章，主题是开发者控制台里上线的"提示词生成器"功能。这个功能能根据你的任务描述，自动生成一份遵循最佳实践的 prompt 模板，无论你是刚入门的新手还是经验丰富的提示词工程师，都能省下不少调试时间。我们会把文章里提到的角色设定、思维链、变量标签化这几个核心技巧拆开讲清楚,并聊聊放在两千零二十六年的今天,这套思路是否还值得用。

本期要点：
- Anthropic 在控制台里加入了能自动生成 prompt 模板的功能，输入任务描述即可产出可直接使用的提示词
- 核心技巧一：角色设定，让 Claude 在回答前先"入戏"成某个领域专家
- 核心技巧二：思维链，给模型一个草稿区，让它先想清楚再回答
- 核心技巧三：用 XML 标签给变量和长文本划清边界，提升结构清晰度
- 真实客户案例 ZoomInfo 使用该功能后，将 RAG 应用的 prompt 调试时间缩短了百分之八十
- 结合两千零二十六年的视角，聊聊这些技巧在今天 agent 和长上下文时代是否依然适用

---

原文：Generate better prompts in the developer console
链接：https://claude.com/blog/prompt-generator
发表时间：2024-05-20
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
