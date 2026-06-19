# EP22 | Anthropic 首次公开三个基础设施 Bug 的完整事后复盘：从悄悄变差到公开承认

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-09-17-A postmortem of three recent issues.mp3`
- 时长：20 分 40 秒

## Shownotes（复制到小宇宙）

今年八月到九月初，Anthropic 的基础设施出现了三个同时活跃的 Bug，导致部分用户收到质量明显下降的 Claude 回复。这是 Anthropic 工程团队少见地向公众完整披露事故经过的一次——他们解释了每个 Bug 的根因、为什么检测和修复花了那么久，以及未来打算怎么改。

- 三个 Bug 并发叠加，最严重时段有约十六分之一的 Sonnet 4 请求被路由到错误服务器
- "粘性路由"让部分用户持续受影响，而其他用户完全感知不到，造成矛盾的社区反馈
- TPU 编译器的精度混用 Bug（bf16 与 fp32 不一致）是技术上最复杂的一个，连调试行为本身都会改变 Bug 的表现
- 现有评测体系没能及时捕捉到质量下滑，内部隐私保护机制也限制了工程师排查真实对话
- Anthropic 明确声明：绝不会因服务器负载或时间段主动降低模型质量
- 用户反馈在这次事故排查中起到了关键作用，文章鼓励继续用 /bug 指令或点踩上报

---

原文：A postmortem of three recent issues
链接：https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
发表时间：2025-09-17
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
