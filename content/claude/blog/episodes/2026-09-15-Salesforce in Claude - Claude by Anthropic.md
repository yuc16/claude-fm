# EP546 | Salesforce 进 Claude：三十七个销售技能，和一次写回记录系统的示范

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-09-15-Salesforce in Claude - Claude by Anthropic.mp3`
- 时长：26 分 47 秒

## Shownotes（复制到小宇宙）

Anthropic 和 Salesforce 联手，把销售人员的客户、商机和管道直接搬进了 Claude。这不是又一个"帮你写邮件"的小功能，而是一次企业级 AI 代理的完整架构示范：三十七个技能、两个连接器、继承既有权限、写操作默认要人批准、记录系统保持不动。

本期我们把这篇五分钟的官方博客拆成二十五分钟，逐个讲透五个真实使用场景，然后重点聊它背后的四条企业 AI 架构默认值，以及你自己动手时要避开的五个坑。

本期要点
- Salesforce in Claude 是一个 beta 插件，含三十七个面向销售日常的技能，覆盖客户研究、通话准备、管道复盘和 CRM 更新
- 两个连接器打通信息孤岛：Salesforce 连接器让 Claude 读写记录，Slack 连接器覆盖交易频道和客户团队线程
- 首次使用会跑一个配置技能，识别工具链并生成贴合个人业务盘子的 Claude Artifact
- 权限设计是最大亮点：用户用自己的 Salesforce 凭据登录，Claude 只读权限允许的数据，每一笔写回都默认要人工批准
- 五个真实场景：早晨简报、通话准备、交易评分与成交计划、会后更新、管道复盘与预测分享
- GitLab、Siemens、Legora 已部署，七千名 Salesforce 销售在日常使用，规模化落地已经发生

---

原文：Salesforce in Claude | Claude by Anthropic
链接：https://claude.com/blog/salesforce-in-claude
发表时间：2026-09-15
本期解读由模型（deepseek-v4-flash）生成，音频由 edge-tts 合成。
