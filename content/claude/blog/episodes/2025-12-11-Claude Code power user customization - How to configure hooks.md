# EP269 | 用 Hooks 给 Claude Code 装上自动化引擎

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-12-11-Claude Code power user customization - How to configure hooks.mp3`
- 时长：22 分 25 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊 Anthropic 官方博客在二〇二五年十二月发布的一篇技术文章,主题是如何通过配置 hooks 来给 Claude Code 做深度定制。如果你已经在日常工作里用 Claude Code 写代码,但还在手动跑格式化工具、反复点确认弹窗、每次开新会话都要重新粘贴项目背景,这篇文章和这期节目就是为你准备的。我们会把文章里提到的八种 hook 类型挨个拆开讲清楚,再聊聊怎么落地、要注意哪些安全风险。

本期要点
- hooks 到底是什么,它解决的三类问题:消除重复操作、强制项目规则、自动注入上下文
- PreToolUse、PermissionRequest、PostToolUse 这三个跟工具调用相关的 hook 怎么配合使用
- SessionStart、Stop、SubagentStop、UserPromptSubmit、PreCompact 各自适合什么场景
- 配置文件放在哪,matcher 怎么写,JSON 输入输出和退出码的规则
- 用 hooks 要注意的安全风险,以及怎么用 transcript 文件和日志脚本调试
- 给普通听众的实践建议,从哪个 hook 开始上手最划算

---

原文：Claude Code power user customization: How to configure hooks
链接：https://claude.com/blog/how-to-configure-hooks
发表时间：2025-12-11
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
