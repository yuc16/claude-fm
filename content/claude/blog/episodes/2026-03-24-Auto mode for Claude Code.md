# EP228 | Claude Code 自动模式:自主与安全之间的中间地带

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-03-24-Auto mode for Claude Code.mp3`
- 时长：24 分 21 秒

## Shownotes（复制到小宇宙）

本期我们聊聊 Anthropic 刚给 Claude Code 上线的自动模式,它在"每一步都要人工批准"和"完全跳过权限检查"这两个极端之间找到了一条新路:用一个实时风险分类器在操作执行前做判断,安全的自动放行,危险的拦下来引导 AI 换思路,反复被拦才升级给人决定。我们会讲清楚这个分类器具体在防什么、被拦截之后 Claude 会怎么应对、这个模式的安全边界在哪里,以及普通开发者具体怎么开启和使用。

本期要点:
- 默认权限模式下 Claude Code 每次文件写入和命令执行都要人工确认,安全但没法长时间放手不管
- 跳过权限检查的做法风险很高,官方明确不建议在隔离环境之外使用
- 自动模式引入一个分类器,在工具调用前判断是否存在大规模删除、敏感数据外泄、恶意代码执行等高风险行为
- 操作被拦截后 Claude 会尝试换一种更保守的方式完成任务,反复被拦才会把决定权交还给用户
- 自动模式降低风险但不能消除风险,官方仍建议搭配隔离环境使用
- 目前支持 Claude Sonnet 四点六和 Opus 四点六,先在 Team 计划开放研究预览,随后扩展到 Enterprise 和 API 用户

---

原文：Auto mode for Claude Code
链接：https://claude.com/blog/auto-mode
发表时间：2026-03-24
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
