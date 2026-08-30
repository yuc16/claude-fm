# EP523 | Claude 进 Chrome，浏览器代理正式可用

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-08-26-Claude in Chrome is generally available - Claude by Anthropic.mp3`
- 时长：25 分 15 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 文章《Claude in Chrome is generally available》。Claude in Chrome 已面向所有付费计划开放，并开始支持在浏览器里更自主地执行操作，但重点其实是它背后的安全机制：如何防 prompt injection，以及如何判断一个动作是否符合用户原始意图。

- Claude in Chrome 为什么重要：它让 AI 能操作内部系统、旧后台和供应商门户
- 浏览器 agent 最大风险：网页、邮件、表单里隐藏的 prompt injection
- Anthropic 的三层防护：模型训练、内容探针、动作前分类器
- 最新评测结果：更强红队攻击下，防护组合显著降低成功率
- 工程实践启发：企业如何试用、限制域名、设计审批和审计机制

---

原文：Claude in Chrome is generally available | Claude by Anthropic
链接：https://claude.com/blog/claude-in-chrome-generally-available
发表时间：2026-08-26
本期解读由模型（gpt-5.5）生成，音频由 edge-tts 合成。
