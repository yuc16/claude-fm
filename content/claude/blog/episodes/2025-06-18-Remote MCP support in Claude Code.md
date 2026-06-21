# EP313 | Claude Code 接入远程 MCP：告别本地服务器的开发新姿势

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-06-18-Remote MCP support in Claude Code.mp3`
- 时长：18 分 04 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊 Anthropic 在二〇二五年六月发布的一篇博客,主题是 Claude Code 支持远程 MCP 服务器。简单说,就是你不用再在自己电脑上折腾本地服务进程,直接填一个网址,经过一次授权,就能让 Claude Code 连上 Sentry、Linear 这类第三方工具,把外部上下文直接拉进编程助手里。我们会拆解这个功能背后的协议逻辑、安全设计,以及它对日常开发流程的实际影响。

本期要点
- MCP 协议到底是什么,为什么它被称为"AI 应用的 USB 接口"
- 本地 MCP 服务器和远程 MCP 服务器的本质区别,以及远程方案省掉了哪些运维负担
- OAuth 原生支持如何解决凭证管理这个老大难问题
- Sentry 和 Linear 两个真实集成案例,看看具体能干什么活
- 这篇文章发布已经一年,结合今天的 AI 生态进展,我们该怎么看待它的历史位置
- 普通工程师现在上手远程 MCP,应该从哪一步开始,有哪些坑要提前避开

---

原文：Remote MCP support in Claude Code
链接：https://claude.com/blog/claude-code-remote-mcp
发表时间：2025-06-18
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
