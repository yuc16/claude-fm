# EP556 | Claude Tag 支持个人连接器，频道协作的权限边界重新划了一条线

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-09-24-Claude Tag now supports personal connectors in channels - Claude by Anthropic.mp3`
- 时长：29 分 40 秒

## Shownotes（复制到小宇宙）

Anthropic 在二〇二六年九月二十四日更新了 Claude Tag：现在你在 Slack 频道里艾特 Claude，它可以用你自己的个人连接器，去读那些只有你能打开的数据。别人用不了你的连接器，你还能自己决定结果怎么发出去。这篇文章篇幅很短，但它把企业 AI 落地里最难的权限问题，拆成了一条清晰的边界线。

本期要点：
- 过去频道连接器挂的是"频道身份"，管理员只能把清单压得很短，因为数据访问权应该跟着人走而不是跟着频道走
- 新能力让 Claude 在频道里以"提问者身份"执行，用你的日历、云盘、CRM、预发布环境，权限不放大、可随时断开
- 输出端有 review 和 auto 两种模式，企业版管理员可以强制所有人先审后发
- 审计上两条通路完全分开：你的操作记在你账号下，频道的操作记在服务账号下
- 个人连接器不支持无人值守，定时任务和 Claude 自发动作必须走共享连接器
- 最容易被误解的一点：输入是私密的，输出是公开的，Claude 发到频道的内容所有人都能看到

---

原文：Claude Tag now supports personal connectors in channels | Claude by Anthropic
链接：https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels
发表时间：2026-09-24
本期解读由模型（deepseek-v4-flash）生成，音频由 edge-tts 合成。
