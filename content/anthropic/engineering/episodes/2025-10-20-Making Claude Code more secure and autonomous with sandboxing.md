# EP23 | 沙箱护盾：Anthropic 如何让 Claude Code 又快又安全地自主编程

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-10-20-Making Claude Code more secure and autonomous with sandboxing.mp3`
- 时长：28 分 03 秒

## Shownotes（复制到小宇宙）

Anthropic 工程博客详解了他们为 Claude Code 构建的沙箱安全体系——通过操作系统级别的文件系统隔离与网络隔离，在几乎不打扰开发者的前提下，把 AI 智能体的"破坏半径"压缩到最小。内部测试数据显示，这套机制让权限确认提示减少了 84%，同时对提示词注入等攻击提供了实质性防护。

- 为什么频繁的"批准"弹窗反而让开发更不安全——"批准疲劳"的陷阱
- 文件系统隔离与网络隔离必须同时存在，缺一不可的架构原因
- OS 级原语：Linux bubblewrap 与 macOS seatbelt 是如何在内核层强制执行限制的
- 网络隔离的代理架构：域名白名单 + 用户确认机制的完整闭环
- 网页版 Claude Code 的受限凭证代理，如何解决云端智能体的 git 凭证安全难题
- 对自建智能体应用的开发者而言，沙箱化应该是架构阶段的核心约束，而非事后补丁

---

原文：Making Claude Code more secure and autonomous with sandboxing
链接：https://www.anthropic.com/engineering/claude-code-sandboxing
发表时间：2025-10-20
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
