# EP173 | Agent 终于有了长期记忆：Claude 托管 Agent 跨会话学习能力全解析

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-23-Built-in memory for Claude Managed Agents.mp3`
- 时长：25 分 54 秒

## Shownotes（复制到小宇宙）

Anthropic 在二〇二六年四月正式推出了 Claude Managed Agents 的内置记忆功能公测版。这期节目我们来拆解为什么「基于文件系统的记忆」是个聪明的设计选择，以及 Rakuten 如何用它把 Agent 一次错误率砍掉了 97%、Wisedocs 验证速度提升 30% 背后的工程逻辑。

- 什么是 Managed Agents，Agent「金鱼记忆」问题为什么一直没被解决好
- 为什么选择文件系统而不是向量数据库来存记忆：自然融合 vs 引入新机制
- 企业级设计的三板斧：权限分级、并发控制、审计日志与可回滚
- 跨 Agent 共享记忆池：org-wide 只读层 + 用户级读写层的两层架构
- 四个早期用户案例深析：Netflix、Rakuten、Wisedocs、Ando 各自解决了什么问题
- 开发者上手指南：哪些场景最值得接入，三个你容易踩的坑

---

原文：Built-in memory for Claude Managed Agents
链接：https://claude.com/blog/claude-managed-agents-memory
发表时间：2026-04-23
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
