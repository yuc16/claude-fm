# EP307 | Claude Code 自动化安全审查：从终端到 PR 的全流程防线

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-08-06-Automate security reviews with Claude Code.mp3`
- 时长：25 分 50 秒

## Shownotes（复制到小宇宙）

本期我们聊聊 Anthropic 在二〇二五年八月发布的一篇技术博客，主题是如何用 Claude Code 把安全审查这件事自动化。这篇文章介绍了两个新功能,一个是终端里的斜杠命令 security-review，另一个是接入 GitHub 的自动化 Action，两者结合起来,试图把安全审查从"上线前临时抱佛脚"变成"写代码的时候就顺手做掉"的日常习惯。我们会拆解这两个功能具体怎么用、能查出哪些类型的漏洞,以及 Anthropic 自己内部用这套工具抓到的两个真实案例。

- 文章发表于二〇二五年八月六日,距今已近一年,我们会聊聊这个时间点在 AI 辅助编程发展史上的位置
- 第一个核心功能,终端里的 security-review 命令,能做哪些类型的漏洞检测
- 第二个核心功能,GitHub Actions 集成,如何在 PR 阶段自动把关
- Anthropic 自己内部用这套工具抓到的两个真实漏洞案例,一个是 DNS 重绑定导致的远程代码执行,另一个是代理系统的 SSRF 漏洞
- 这套工具对个人开发者和团队各自意味着什么,该怎么落地、要避免哪些误区
- 我个人对这种"AI 既写代码又审代码"模式的看法和担忧

---

原文：Automate security reviews with Claude Code
链接：https://claude.com/blog/automate-security-reviews-with-claude-code
发表时间：2025-08-06
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
