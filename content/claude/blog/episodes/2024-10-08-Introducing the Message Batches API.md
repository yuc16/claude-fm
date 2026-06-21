# EP105 | 异步批量处理大幅省钱:解读Claude的Message Batches API

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2024-10-08-Introducing the Message Batches API.mp3`
- 时长：17 分 07 秒

## Shownotes（复制到小宇宙）

本期我们聊一聊Anthropic在二〇二四年十月发布的Message Batches API,也就是消息批处理接口。这是一个专门为非实时、大批量任务设计的接口,核心卖点是省钱和省心。我们会从行业背景讲到具体机制,再聊聊工程师在实际工作中应该怎么用它,以及它和实时调用之间应该怎么权衡。

本期要点:
- Message Batches API是什么,解决的是什么问题
- 单批最多一万条查询,二十四小时内处理完成,价格直降五成
- 为什么异步处理能换来这么大的成本优势,背后的资源调度逻辑
- Quora这家公司是怎么用它做摘要和内容提炼的
- 哪些场景特别适合批处理,哪些场景千万别用
- 这篇二〇二四年的旧文章放到今天二〇二六年年中来看,还有哪些参考价值

---

原文：Introducing the Message Batches API
链接：https://claude.com/blog/message-batches-api
发表时间：2024-10-08
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
