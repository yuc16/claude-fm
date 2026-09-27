# EP557 | Claude Opus 五点五：当编码会话变长，成本该怎么算

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-09-24-Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind. - Claude by Anthropic.mp3`
- 时长：27 分 10 秒

## Shownotes（复制到小宇宙）

Anthropic 在九月二十四日发布了一篇不长的博客，但它讲的不是新模型有多强，而是当编码会话越来越长、上下文越来越重之后，成本结构发生了什么变化。文章第一次公开了 Claude Code 从三月到九月的使用数据，并解释了 Opus 五点五 在定价、模型行为和 Claude Code 运行框架三个层面做了什么，让长会话变得更便宜。

本期要点：
- 开发者的每个 prompt 让 Claude 工作的时间变成了三点三倍，模型调用多出四成，人工打断减少了六成八
- 每次请求携带的上下文增长了二点六倍，输入和输出的 token 比例从一百八十九比一涨到三百二十四比一
- Opus 五点五 把输入输出 token 价格降了两成，把缓存读取价格降了六成，典型负载整体成本低约四成
- 缓存未命中的输入减少了超过一半，因为 Claude Code 修掉了很多会意外打破缓存的小动作
- 模型完成同一任务需要的轮次更少，而少一轮比拼一个缓存更省钱
- 三个可以立刻上手的习惯：会话开始就选定模型、离开前先压缩上下文、长会话设置一小时缓存

---

原文：Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind. | Claude by Anthropic
链接：https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
发表时间：2026-09-24
本期解读由模型（deepseek-v4-flash）生成，音频由 edge-tts 合成。
