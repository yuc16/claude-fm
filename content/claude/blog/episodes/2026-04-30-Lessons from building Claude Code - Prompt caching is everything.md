# EP383 | 提示词缓存才是一切:Claude Code的省钱提速法则

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-30-Lessons from building Claude Code - Prompt caching is everything.mp3`
- 时长：24 分 58 秒

## Shownotes（复制到小宇宙）

本期我们聊聊Anthropic官方博客最新发布的一篇文章,主题是Claude Code团队在打造长时间运行的智能体产品过程中,总结出的关于prompt caching,也就是提示词缓存的实战经验。这篇文章揭示了一个反直觉但极其重要的事实,智能体产品的成本和速度,很大程度上不是由模型能力决定的,而是由你的请求结构设计能不能命中缓存决定的。我们会拆解前缀缓存的工作原理、为什么换模型换工具会变得异常昂贵,以及Claude Code是怎么用Plan Mode和工具搜索这些功能设计,巧妙地绕开缓存失效的坑。

本期要点:
- 提示词缓存按前缀逐字匹配,请求里任何靠前的改动都会让后面全部失效,因此要把系统提示词和工具定义这类静态内容放在最前面,会变化的内容放在最后面
- 想给模型传递时效性信息时,不要去改系统提示词,而是通过下一轮消息或者工具结果里的提示标签来传递,这样才能保住缓存
- 缓存是按模型独立计算的,对话进行到一半时直接换成更便宜的模型反而可能更贵,真要换模型应该用子agent做交接
- 中途增减工具会打破整个对话的缓存,Plan Mode之类的状态切换应该用工具调用本身来表达,而不是动工具列表;暂时用不到的工具可以用延迟加载的方式保留占位符
- compaction压缩对话时如果用独立的系统提示词和调用方式会导致完全无法命中缓存,正确做法是沿用主对话完全相同的前缀,只在末尾追加总结请求
- 这套思路的本质,是把缓存命中率当成跟系统稳定性同等重要的核心指标来设计和监控

---

原文：Lessons from building Claude Code: Prompt caching is everything
链接：https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything
发表时间：2026-04-30
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
