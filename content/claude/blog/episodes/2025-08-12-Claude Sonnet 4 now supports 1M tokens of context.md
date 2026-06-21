# EP187 | Claude Sonnet 4 上下文扩到百万令牌意味着什么

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-08-12-Claude Sonnet 4 now supports 1M tokens of context.mp3`
- 时长：25 分 36 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊 Anthropic 在二〇二五年八月发布的一条更新：Claude Sonnet 四点零的上下文窗口从二十万令牌一口气扩大到一百万令牌，足足放大了五倍。这意味着什么,能不能把一整个代码仓库塞进去,价格又会怎么变,我们都会一层一层拆开讲清楚。结合现在已经是二〇二六年年中的时间点,我们也会聊聊这条更新放在整个大模型发展节奏里处于什么位置,以及对今天还在用 Claude 写代码、做文档分析、搭 agent 的工程师来说,实际该怎么用、怎么省钱、怎么避坑。

本期要点
- Claude Sonnet 四点零上下文窗口从二十万扩到一百万令牌,五倍提升,目前在 Anthropic API 上以公开测试版形式提供
- 一百万令牌大概能装下七万五千行以上的代码,或者几十篇研究论文,足够覆盖很多真实项目的全量代码
- 三大典型场景:大规模代码分析、海量文档综合分析、能跨越上百次工具调用保持连贯的 agent
- 超过二十万令牌之后定价会上调,输入从三美元每百万令牌涨到六美元,输出从十五美元涨到二十二点五美元
- 配合 prompt caching 也就是提示缓存和批处理 batch processing 可以分别降低延迟和成本,批处理还能再省一半费用
- Bolt.new 和 iGent AI 两家客户分享了真实落地反馈,百万上下文直接改变了他们做大型项目和多日自动化编程任务的方式

---

原文：Claude Sonnet 4 now supports 1M tokens of context
链接：https://claude.com/blog/1m-context
发表时间：2025-08-12
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
