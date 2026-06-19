# EP3 | Claude Code 自动模式：用 AI 分类器替代人类审批，把 agent 从"点击地狱"里解救出来

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2026-03-25-How we built Claude Code auto mode - a safer way to skip permissions.mp3`
- 时长：27 分 31 秒

## Shownotes（复制到小宇宙）

Anthropic 工程团队详解 Claude Code auto mode 的完整设计：为什么手动授权会失败、两层防护架构如何拦截危险动作、分类器为何要"推理盲视"，以及那个诚实的百分之十七漏报率意味着什么。

本期要点
- 用户有百分之九十三的情况都会点"批准"，手动授权实际上已经退化为仪式
- auto mode 用两层防护替代人类审批：输入端的提示词注入探针 + 输出端的转录分类器
- 分类器故意看不到 Claude 自己的推理内容，防止 agent 用"自圆其说"绕过安全检查
- 两段式分类设计：快速单 token 过滤把误拦截率从百分之八点五压到百分之零点四
- 真实过度积极行为的漏报率是百分之十七，文章对此诚实地说明了适用场景边界

---

原文：How we built Claude Code auto mode: a safer way to skip permissions
链接：https://www.anthropic.com/engineering/claude-code-auto-mode
发表时间：2026-03-25
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
