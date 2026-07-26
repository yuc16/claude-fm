# EP481 | Claude 五代模型的上下文工程新规则

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-07-24-The new rules of context engineering for Claude 5 generation models - Claude by Anthropic.mp3`
- 时长：33 分 36 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 最新文章，讨论 Claude 五代模型时代，context engineering 为什么要从“堆规则”转向“给判断空间”。文章最关键的信号是：Anthropic 为 Claude Opus 5 和 Claude Fable 5 删除了 Claude Code 超过八成的 system prompt，却没有在编码评测中看到可测量损失。

- prompt 只是上下文的一小部分，真正影响结果的是 system prompt、Skills、CLAUDE.md、memory 和 references 的组合
- 新模型不再需要大量硬规则，过度约束反而会让 Claude 更难判断用户真实意图
- 工具使用从“给例子”转向“设计好接口”，让模型通过参数和描述理解能力边界
- 上下文加载从“一次性塞满”转向 progressive disclosure，需要时再加载技能、工具和参考资料
- CLAUDE.md 应该轻量化，重点写仓库里的坑，而不是写显而易见的常识
- specs、测试套件、HTML mockup、rubrics 都可以成为更高保真的 rich references

---

原文：The new rules of context engineering for Claude 5 generation models | Claude by Anthropic
链接：https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
发表时间：2026-07-24
本期解读由模型（gpt-5.5）生成，音频由 edge-tts 合成。
