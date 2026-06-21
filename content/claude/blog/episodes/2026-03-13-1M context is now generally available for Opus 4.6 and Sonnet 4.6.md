# EP330 | 百万级上下文全面开放,Claude 终于不再"失忆"

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-03-13-1M context is now generally available for Opus 4.6 and Sonnet 4.6.mp3`
- 时长：21 分 28 秒

## Shownotes（复制到小宇宙）

本期我们聊聊 Anthropic 在二〇二六年三月十三日发布的一篇博客,主题是 Opus 四点六和 Sonnet 四点六两款模型的百万 token 上下文窗口正式全面可用。这次更新最大的亮点是取消了长上下文的额外加价,统一按标准价格计费,同时大幅提升了媒体文件的处理上限,还把这项能力直接整合进了 Claude Code。我们会从定价机制、速率限制、媒体上限、MRCR 二代评测成绩这几个角度展开讲,再聊聊这对日常写代码、做合同审查、跑长链路 agent 任务的工程师们到底意味着什么。

本期要点
- 百万 token 上下文窗口正式全面可用,不再是测试版功能
- 取消长上下文加价,九千 token 和九十万 token 的请求按同样的单价计费
- 速率限制在整个上下文长度区间内保持一致,不会因为用得多就被限流更狠
- 图片和 PDF 页面的处理上限从一百提升到六百,提升了六倍
- 不再需要发送测试版请求头,超过二十万 token 的请求自动生效
- Claude Code 的 Max、Team 和 Enterprise 用户在使用 Opus 四点六时默认开启百万上下文,减少对话被压缩的情况

---

原文：1M context is now generally available for Opus 4.6 and Sonnet 4.6
链接：https://claude.com/blog/1m-context-ga
发表时间：2026-03-13
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
