# EP621 | 常驻智能体怎么造：从事件驱动到安全自主行动

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-11-13-Building always-on agents.mp3`
- 时长：23 分 21 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 于二〇二六年十一月十三日发表的《Building always-on agents》，聊聊真正能长期替用户做事的智能体，为什么不需要一直运行。我们从事件收件箱、定时器、记忆、权限和发件箱出发，把一套可恢复、能等待、懂得少打扰的系统架构讲清楚。

本期要点
- “始终在线”是一种用户体验，底层其实是休眠与短暂运行组成的循环
- 用持久化事件收件箱处理并发、去重、重试与会话恢复
- 区分跟进提醒和周期任务，让定时器通过事件唤醒智能体
- 把长期记忆与会话历史分开，只保存无法重新查询的重要信息
- 用凭据代理、风险判断和延迟工具调用控制无人值守的行动权限
- 从安静开始，通过评估寻找主动服务与通知噪声之间的平衡

---

原文：Building always-on agents
链接：https://claude.com/resources/articles/building-always-on-agents
发表时间：2026-11-13
本期解读由模型（gpt-6.1-sol）生成，音频由 edge-tts 合成。
