# EP486 | Claude 驱动的自主网络安全调查员

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-07-22-How Outtake built a cyber investigator on Claude - Claude by Anthropic.mp3`
- 时长：32 分 19 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 官方博客里 Outtake 如何用 Claude Code 和 Claude Agent SDK 构建一个长时间运行的网络安全调查 agent。它不只是发现一个仿冒登录页，而是追踪背后的攻击基础设施、证据链和威胁行为者画像。

本期也会重点聊长任务 agent 的工程经验：什么该交给 prompt，什么该写进系统护栏，为什么 eval 对开发速度比对质量门禁更重要，以及面对 prompt injection 时 agent 应该怎样穿上“盔甲”。

- AI 正在加速钓鱼、仿冒和攻击链，传统安全工具只覆盖其中一段
- Outtake 的 Recon Agent 如何从单个仿冒页面追到完整攻击网络
- Claude Code 和 Agent SDK 在原型验证、工具使用、记忆和会话管理里的作用
- 长时间运行 agent 的关键原则：编排要收紧，判断要放开
- 为什么文件系统、自动 eval、沙箱和 prompt injection 防护是生产级 agent 的核心

---

原文：How Outtake built a cyber investigator on Claude | Claude by Anthropic
链接：https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude
发表时间：2026-07-22
本期解读由模型（gpt-5.5）生成，音频由 edge-tts 合成。
