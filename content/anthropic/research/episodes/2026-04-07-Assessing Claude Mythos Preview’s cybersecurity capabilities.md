# EP143 | 一个 AI 模型自主找到了二十七年前的漏洞，还自己写好了攻击代码

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-04-07-Assessing Claude Mythos Preview’s cybersecurity capabilities.mp3`
- 时长：27 分 54 秒

## Shownotes（复制到小宇宙）

本期节目深度解读 Anthropic 前沿红队发布的技术报告：他们用最新模型 Claude Mythos Preview 自主发现了多个沉睡数十年的安全漏洞，并在没有人工干预的情况下写出了完整的攻击代码。这不是实验室演示，而是在真实的、完全打补丁的生产系统上实际发生的事情，波及 OpenBSD、FreeBSD、FFmpeg、主流浏览器和 Linux 内核。Anthropic 认为，AI 辅助的漏洞挖掘可能正在打破过去二十年的网络安全平衡，并为此专门启动了 Project Glasswing 防御行动。

- Claude Mythos Preview 自主实现了零日漏洞挖掘和 exploit 开发，成功率远超上一代 Opus 四点六，在 Firefox JS 引擎漏洞上的成功次数从两次跃升至一百八十一次
- 实测案例：27 年老漏洞 OpenBSD SACK 崩溃攻击、16 年老漏洞 FFmpeg H.264 越界写入、自主写出 FreeBSD NFS 服务器完整远程 root exploit（CVE-2026-4747）
- 模型能将多个漏洞串联成利用链，在 Linux 内核上实现本地提权，在浏览器上实现 JIT 堆喷和沙箱逃逸
- 这些能力并非专门训练的结果，而是代码理解与自主推理能力提升后的自然涌现
- 文章详解了两个 N-Day exploit 的完整技术细节，说明从公开 CVE 到可用攻击代码的时间正大幅压缩
- 对防御方的具体建议：立即用现有模型主动扫漏洞、缩短补丁部署窗口、自动化安全事故响应流程

---

原文：Assessing Claude Mythos Preview’s cybersecurity capabilities
链接：https://www.anthropic.com/research/mythos-preview
发表时间：2026-04-07
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
