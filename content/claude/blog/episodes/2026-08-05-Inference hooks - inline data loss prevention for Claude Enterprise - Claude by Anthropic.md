# EP498 | Claude企业版实时数据防泄露门禁

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-08-05-Inference hooks - inline data loss prevention for Claude Enterprise - Claude by Anthropic.mp3`
- 时长：29 分 10 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 在二〇二六年八月五日发布的 Claude Enterprise 新能力 Inference hooks。它把企业现有的数据防泄露系统接到 Claude 的推理链路里，让每一次 prompt 和工具调用结果在进入模型前都先过安全团队控制的检查点。

- Inference hooks 解决的是企业 AI 使用中的内联数据防泄露问题
- 它通过签名 WebSocket 把请求路由到企业自己的 DLP 服务器，由企业判定放行或阻断
- 覆盖 Claude Enterprise 的 chat、Claude Code、Claude Cowork，以及 MCP、skills、plugins 等工具调用
- 支持 shadow mode、按角色排除、按比例灰度、超时和失败策略配置
- 对工程团队的意义是把 AI 安全从事后审计推进到实时拦截

---

原文：Inference hooks: inline data loss prevention for Claude Enterprise | Claude by Anthropic
链接：https://claude.com/blog/claude-enterprise-inference-hooks
发表时间：2026-08-05
本期解读由模型（gpt-5.5）生成，音频由 edge-tts 合成。
