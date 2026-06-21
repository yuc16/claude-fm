# EP426 | Skills 不只是 Markdown：Anthropic 用几百个内部工具踩出的 AI 工程实践

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-06-03-Lessons from building Claude Code - How we use skills.mp3`
- 时长：25 分 43 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 技术团队发布的工程实践文章，作者是 Claude Code 核心开发者 Thariq Shihipar。文章总结了 Anthropic 内部使用几百个 skills 的真实经验，覆盖技能的九类分类框架、写作最佳实践和团队分发策略。如果你在用 Claude Code，或者正在考虑如何把 AI 引入工程工作流，这是一篇能帮你大幅压缩试错成本的第一手实战指南。

- Skills 是文件夹而非 markdown 文件，可以包含脚本、资产、数据和动态钩子，这个认知差异极为重要
- Anthropic 将内部 skills 归纳为九大类：使用指南、验证、数据监控、工作流自动化、脚手架、代码质量、部署、故障调查、运维操作
- 验证类 skills 对 Claude 输出质量的提升最为显著，值得专门让工程师花一整周打磨
- Gotchas 段落是整个 skill 里信噪比最高的内容，应持续积累 Claude 踩过的具体错误
- Skill 描述字段是触发条件而非功能摘要，直接影响 Claude 能否在正确时机识别并调用它
- 通过日志文件给 skill 添加"记忆"，让 Claude 在多次运行之间保持状态连续性

---

原文：Lessons from building Claude Code: How we use skills
链接：https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
发表时间：2026-06-03
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
