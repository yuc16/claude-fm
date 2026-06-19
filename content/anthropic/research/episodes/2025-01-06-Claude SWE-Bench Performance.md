# EP111 | AI 自主修代码终于走通了：深度解析 Claude 软件工程 Agent 的架构设计与工程洞见

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-01-06-Claude SWE-Bench Performance.mp3`
- 时长：26 分 31 秒

## Shownotes（复制到小宇宙）

本期我们聊一篇来自 Anthropic 的技术研究文章，记录了他们如何搭建一套极简 agent 架构，让 Claude 三点五 Sonnet 在软件工程基准测试 SWE-bench Verified 上拿下当时的世界第一，得分百分之四十九。这篇文章的核心价值不在于那个历史分数，而在于它把一个工程级别的 AI agent 架构完整摊开来讲：prompt 怎么写、工具怎么设计、为什么这样设计。

- 什么是 SWE-bench：为什么它是目前最接近真实软件工程场景的 AI 评测
- 设计哲学：极简脚手架 + 把控制权还给模型，为什么这条路更有效
- Bash 工具和编辑工具的设计细节，以及工具 description 字段有多重要
- 一个真实 sklearn bug 修复的完整过程走读，12 步到提交
- 运行 SWE-bench 时踩到的坑：成本、评分噪音、隐藏测试、多模态缺失
- 对开发者的实践启示：工具接口设计原则、让错误变得明显、prompt 与约束的平衡

---

原文：Claude SWE-Bench Performance
链接：https://www.anthropic.com/research/swe-bench-sonnet
发表时间：2025-01-06
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
