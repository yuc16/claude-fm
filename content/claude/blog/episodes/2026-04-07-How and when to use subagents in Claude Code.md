# EP226 | 什么时候该把任务交给 Claude Code 的子代理

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-07-How and when to use subagents in Claude Code.mp3`
- 时长：27 分 46 秒

## Shownotes（复制到小宇宙）

这一集我们聊聊 Claude Code 里的 subagent,也就是子代理功能。文章是 Anthropic 官方在二零二六年四月发的一篇实战指南,讲的不是子代理怎么配置这种说明书式的内容,而是更实际的问题:什么时候该用、什么时候不该用、怎么一步步把这件事从随口一说变成团队的标准流程。如果你已经在用 Claude Code 写代码,但还没认真用过子代理,这一集会给你一份可以直接照搬的判断清单。

本期要点
- 子代理是什么:一个有独立上下文窗口的 Claude 实例,像浏览器里的标签页,出去探索完只带结果回来
- 五个该用子代理的信号:大量文件调研、并行无依赖任务、需要无偏见审查、需要提交前二次意见、多阶段任务
- 从对话式调用到自定义子代理、CLAUDE.md 规则、skill、hook,自动化程度逐级升高的五种调用方式
- 自定义子代理的 description 字段怎么写才能让 Claude 准确路由任务
- 五种不该用子代理的场景,包括同文件编辑冲突和子代理之间不能互相对话的限制
- 子代理和 agent teams 的边界:需要协作沟通的任务该换工具

---

原文：How and when to use subagents in Claude Code
链接：https://claude.com/blog/subagents-in-claude-code
发表时间：2026-04-07
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
