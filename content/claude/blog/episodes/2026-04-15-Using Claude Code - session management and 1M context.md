# EP224 | 上下文不是越大越好：Claude Code 会话管理实战课

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-15-Using Claude Code - session management and 1M context.mp3`
- 时长：24 分 52 秒

## Shownotes（复制到小宇宙）

Claude Code 升级到一百万 token 上下文之后,会话该怎么管反而成了新问题。这篇 Anthropic 官方文章把"一件事做完之后该怎么办"拆成了继续、rewind、clear、compact、subagent 五个选项,并给出了每种选择该在什么时候用、为什么用的判断逻辑。本期我们逐条拆解这套框架，并完整推演一个真实工作日里这五个工具是怎么串起来用的。

- 上下文窗口是模型生成回复时能看到的全部内容，一百万 token 也挡不住"上下文腐烂"带来的性能下滑
- 任务完成后的五个选项：继续对话、rewind 倒带、clear 清空、compact 压缩、交给 subagent，各自适合不同场景
- 默认规则是新任务对应新会话，但"半相关"任务要不要开新会话，需要权衡重新读文件的成本
- rewind 比嘴上纠错更干净：跳回失败尝试发生之前的节点，带着教训重新提问，还能让 Claude 自己总结交接信息
- 自动 compact 容易在长调试之后丢掉下一步要用的信息，因为压缩恰好发生在模型最不聪明的时刻，建议主动出手
- subagent 的判断标准很简单：你还需要工具输出本身，还是只需要一个结论

---

原文：Using Claude Code: session management and 1M context
链接：https://claude.com/blog/using-claude-code-session-management-and-1m-context
发表时间：2026-04-15
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
