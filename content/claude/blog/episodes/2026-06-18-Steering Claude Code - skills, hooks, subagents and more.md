# EP177 | 告别 CLAUDE.md 大杂烩：七种方法系统掌控你的 Claude Code

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-06-18-Steering Claude Code - skills, hooks, subagents and more.mp3`
- 时长：25 分 02 秒

## Shownotes（复制到小宇宙）

本期深度解析 Anthropic 于 2026 年 6 月 18 日发布的 Claude Code 定制化系统指南。文章将控制 Claude 行为的方式整理为七种方法，并提供清晰的决策框架，帮助工程师把正确的指令放在正确的位置。如果你曾因 CLAUDE.md 越来越臃肿、Claude 在长对话中"忘记"遵守规则而头疼，这期节目正是你需要的。

- Claude Code 提供七种控制指令的机制，在加载时机、上下文持久性、权威程度上各不相同
- CLAUDE.md 适合存放全局事实与项目概览，但要控制在 200 行内，流程性内容应搬进 Skills（技能）
- 路径范围规则（path-scoped rules）让约束只在相关文件被访问时才进入上下文，节省 token
- Subagents（子智能体）在独立上下文窗口中运行，支持五层嵌套，适合隔离中间过程与结果
- Hooks（钩子）是唯一能实现确定性行为的机制，是自动化触发与安全护栏的正确工具
- 输出风格文件会替换默认系统提示词，使用需谨慎；内置三种风格已覆盖大多数常见场景

---

原文：Steering Claude Code: skills, hooks, subagents and more
链接：https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
发表时间：2026-06-18
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
