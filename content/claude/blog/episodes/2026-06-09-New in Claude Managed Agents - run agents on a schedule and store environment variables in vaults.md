# EP437 | Claude 托管智能体重磅更新：定时调度加密凭证库正式上线公测

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-06-09-New in Claude Managed Agents - run agents on a schedule and store environment variables in vaults.mp3`
- 时长：27 分 18 秒

## Shownotes（复制到小宇宙）

本期聚焦 Anthropic 于二〇二六年六月九日发布的 Claude Managed Agents（托管智能体）重大更新：两项面向生产环境的核心能力正式进入公测，分别是基于 cron 的定时调度部署，以及 Vault 环境变量安全存储。这意味着工程团队不再需要自建调度基础设施，也不需要冒险把 API 密钥暴露给模型——两道长期卡在 agent 生产化路上的坎，一次性被搬掉了。

- 定时部署：agent 可按 cron 计划自动触发，平台托管调度，无需自建
- Vault 新增环境变量支持：CLI 工具和命令行程序可安全完成身份验证
- 密钥从不经过模型层，在网络边界才被附加，严格遵循最小权限原则
- 真实落地案例：乐天、Actively AI、Ando、Notion、Browserbase、KERNEL、Milana
- Managed Agents 首次获得浏览器操作能力，通过 Browserbase 和 KERNEL 实现
- 对开发者的实际影响：从 POC 跨越到生产自动化的关键工程补丁

---

原文：New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults
链接：https://claude.com/blog/whats-new-in-claude-managed-agents
发表时间：2026-06-09
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
