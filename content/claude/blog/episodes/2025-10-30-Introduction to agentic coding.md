# EP237 | 从代码自动补全到自主编程代理：Claude Code如何重塑软件开发

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-10-30-Introduction to agentic coding.mp3`
- 时长：17 分 59 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊Anthropic在二〇二五年十月底发布的一篇博客，主题是agentic coding,也就是自主代理式编程。文章梳理了AI辅助编程从自动补全、到对话式聊天助手、再到能够自主读写整个代码库的agent这三个阶段的演变,并以Claude Code为例,讲了它在真实企业场景里跑出来的效果。我们会展开讲讲这几种工具到底差在哪,自主编程系统是怎么干活的,Rakuten那个七小时无人干预改完vLLM的真实案例到底说明了什么,以及作为工程师你现在能怎么用上手。

- 自动补全工具只看你当前文件附近的上下文,本质还是预测下一个词
- 聊天式AI助手能讨论代码,但要靠你手动复制粘贴,无法跨文件落地修改
- agentic coding是给一个目标,系统自己拆解步骤、读写多个文件、跑测试、迭代,直到达成目标
- Claude Code直接跑在终端里,默认会在改文件前征得你的同意,保留人类审批环节
- Rakuten工程团队让Claude Code在vLLM这个一千二百五十万行代码的项目里自主工作七小时,完成了原本需要人工实现的激活向量提取方法,准确率达到百分之九十九点九
- 文章给出的具体落地场景包括补测试、生成遗留系统文档、做常规重构和实现需求明确的功能

---

原文：Introduction to agentic coding
链接：https://claude.com/blog/introduction-to-agentic-coding
发表时间：2025-10-30
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
