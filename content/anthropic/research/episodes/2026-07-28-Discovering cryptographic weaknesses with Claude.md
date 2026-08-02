# EP491 | Claude 如何加速密码学攻防研究

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-07-28-Discovering cryptographic weaknesses with Claude.mp3`
- 时长：28 分 12 秒

## Shownotes（复制到小宇宙）

Anthropic 最新研究展示了 Claude Mythos Preview 在密码分析中的能力：它不仅能找代码实现漏洞，还能帮助发现算法设计层面的弱点。本期我们拆解 HAWK 后量子签名和七轮 AES 两个案例，聊聊这对安全工程、密码学研究和 AI agent 工作流意味着什么。

- Claude Mythos Preview 改进了对 HAWK 后量子签名候选方案的攻击
- 对七轮 AES 的 meet-in-the-middle 攻击被加速约二百到八百倍
- 两个结果都不影响当前生产系统，但显示了 AI 做研究级密码分析的潜力
- Anthropic 使用多 agent、沙箱、Python 和 Sage 等工具完成半自主探索
- 未来瓶颈可能从发现漏洞转向人类验证、披露和修复

---

原文：Discovering cryptographic weaknesses with Claude
链接：https://www.anthropic.com/research/discovering-cryptographic-weaknesses
发表时间：2026-07-28
本期解读由模型（gpt-5.5）生成，音频由 edge-tts 合成。
