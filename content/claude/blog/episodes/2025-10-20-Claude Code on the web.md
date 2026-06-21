# EP288 | Claude Code 搬上云端:并行编程任务与安全沙箱的新玩法

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-10-20-Claude Code on the web.mp3`
- 时长：18 分 41 秒

## Shownotes（复制到小宇宙）

本期我们聊聊 Anthropic 在二〇二五年十月发布的网页版 Claude Code。这次更新把原本只能在终端里跑的编程助手搬到了浏览器和手机上,让你可以同时给多个仓库派发任务,在云端跑测试、改代码、提 PR,彻底告别一个一个排队等终端的日子。我们会拆解它的并行任务机制、安全沙箱设计,以及移动端预览体验,还会聊聊普通工程师在日常工作里到底能怎么用上它。

- 网页版 Claude Code 的核心卖点:连接 GitHub 仓库后,可以同时派发多个独立任务,各自跑在隔离环境里
- 适合处理 bug 积压、常规修复、后端改动这类"定义清晰"的任务,而不是开放式的复杂设计工作
- 安全机制:每个任务跑在带网络和文件系统限制的沙箱里,Git 操作通过代理服务统一管控
- 支持自定义网络白名单,比如只放行 npm 源,既能装包跑测试,又不会乱连外网
- iOS 端同步上线早期预览,意味着"通勤路上派任务,到公司看 PR"正在变成现实
- 云端会话和本地终端共享同一个用量限额,不是白嫖出来的额外算力

---

原文：Claude Code on the web
链接：https://claude.com/blog/claude-code-on-the-web
发表时间：2025-10-20
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
