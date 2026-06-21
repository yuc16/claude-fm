# EP415 | 代码的魔法回来了:Claude 新增自托管沙箱与私有网络隧道

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-05-26-Code w - Claude London 2026 - Rethinking how we build.mp3`
- 时长：25 分 22 秒

## Shownotes（复制到小宇宙）

本期我们聊聊 Anthropic 把 Code with Claude 开发者大会第一次办到伦敦的这篇报道。Claude Code 负责人 Boris Cherny 在主题演讲里讲了一段关于编程魔法回归的故事,而大会上正式发布的两项新能力,自托管沙箱和 MCP 隧道,让企业终于能把 agent 装进自己已经搭好的安全边界里运行。这一期我们把这两条线索拆开讲透,也聊聊它们对实际工作的意义。

本期要点:
- Boris Cherny 回忆中学时用 TI 八十三计算器和自学 HTML 的经历,提出 agent 正在把想法变成程序之间的距离重新拉近
- Claude Managed Agents 新增自托管沙箱,公测阶段,工具执行环境可以放在自己的基础设施或 Cloudflare、Daytona、Modal、Vercel 等托管服务商,agent 的编排循环仍由 Anthropic 负责
- MCP 隧道进入研究预览,通过自己部署的轻量网关,让 agent 不暴露公网端口就能访问内网的 MCP 服务器,流量端到端加密
- Spotify、Base44、Legora 已经在用 Claude Code 找回写代码的轻快感,Amplitude、Clay、Rogo 已经在用自托管沙箱搭建生产级 agent
- 两项新能力背后是同一个思路:把 agent 的执行环境和它能触达的服务,都收回到企业自己已经建好的安全边界之内
- Code with Claude 下一站是东京,六月五号到六号,主题演讲和分会场视频都已经放出回放

---

原文：Code w/ Claude London 2026: Rethinking how we build
链接：https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
发表时间：2026-05-26
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
