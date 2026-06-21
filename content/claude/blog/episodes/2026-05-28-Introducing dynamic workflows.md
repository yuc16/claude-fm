# EP421 | Claude Code 动态工作流：并行百个智能体，把季度级工程压缩进几天

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-05-28-Introducing dynamic workflows.mp3`
- 时长：23 分 27 秒

## Shownotes（复制到小宇宙）

Anthropic 于 2026 年 5 月 28 日正式发布 Claude Code 动态工作流功能，让 Claude 能够自动编排数十至数百个并行子智能体协同处理超大规模工程任务。本期节目深入拆解这项技术的工作原理、核心设计思路，以及一个令人震撼的真实案例：用动态工作流在十一天内完成了七十五万行代码的语言移植。

- 动态工作流是什么：Claude 自动生成编排脚本，启动大规模并行子智能体处理复杂任务
- 三大核心设计：动态任务分解、并行执行、对抗性验证与进度持久化
- Bun 案例详解：从 Zig 到 Rust 的七十五万行移植，十一天完成，测试通过率 99.8%
- 适合哪类任务：代码库全局审计、大型迁移、需要高可信度验证的关键工作
- 实践注意事项：token 消耗显著增加，建议从范围明确的任务开始，结果仍需人工审查
- 如何上手：Pro 用户需在 /config 手动开启，Max/Team/Enterprise 默认开启，支持 ultracode 设置

---

原文：Introducing dynamic workflows
链接：https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
发表时间：2026-05-28
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
