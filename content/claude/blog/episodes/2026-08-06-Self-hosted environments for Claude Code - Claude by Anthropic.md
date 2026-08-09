# EP497 | Claude Code 企业自托管运行新解

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-08-06-Self-hosted environments for Claude Code - Claude by Anthropic.mp3`
- 时长：32 分 20 秒

## Shownotes（复制到小宇宙）

Anthropic 在八月六日发布了 Claude Code 自托管环境的公开测试版，让企业可以把代码 agent 的执行过程放到自己的基础设施里。本期我们拆解它到底解决什么问题，哪些数据留在企业内部，哪些仍会发送给 Anthropic，以及工程团队落地时该怎么判断值不值得上。

- 自托管环境让 Claude Code session 运行在企业内网和自有基础设施中
- Anthropic 仍建议大多数企业优先使用托管版，自托管适合有网络、工具链和合规要求的团队
- 代码仓库、构建产物、密钥和文件留在自有环境，但对话和工具结果会发送给 Anthropic 做推理
- runner 是核心执行组件，支持固定容量和按需启动两种模式
- 它不同于 Remote Control，不是把个人电脑上的会话远程接上，而是平台团队运营的共享执行环境
- 实践中要重点关注镜像维护、权限边界、密钥治理、成本弹性和 ZDR 限制

---

原文：Self-hosted environments for Claude Code | Claude by Anthropic
链接：https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
发表时间：2026-08-06
本期解读由模型（gpt-5.5）生成，音频由 edge-tts 合成。
