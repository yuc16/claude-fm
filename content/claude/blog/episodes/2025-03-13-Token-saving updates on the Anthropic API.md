# EP136 | Claude 提速降本三件套：缓存、工具调用与编辑工具全解析

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-03-13-Token-saving updates on the Anthropic API.mp3`
- 时长：19 分 20 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊 Anthropic 在二〇二五年三月发布的一篇技术博客，主题是如何用更少的 token 把 Claude 用得更快更省。文章发布的时候 Claude 三点七 Sonnet 刚刚问世不久，Anthropic 借着这次更新，把缓存机制、速率限制和工具调用都做了一轮"瘦身"。虽然这篇文章已经过去一年多了，但里面讲的几个机制至今仍然是用好 Claude API 的基础知识，值得回顾。

本期要点：
- 缓存读取的 token 不再占用输入速率限制，相当于免费多出一大块吞吐量
- prompt caching 自动匹配最长缓存前缀，开发者不用再手动管理缓存版本
- token 高效工具调用能把输出 token 消耗降低最多七成，平均省一成四
- 全新的 text_editor 工具让 Claude 可以对文档做精准的局部编辑,而不是整篇重写
- Cognition 公司用这些功能给 Devin 提速降本的真实案例
- 这些功能从二〇二五年三月起已经全面开放,接入成本很低

---

原文：Token-saving updates on the Anthropic API
链接：https://claude.com/blog/token-saving-updates
发表时间：2025-03-13
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
