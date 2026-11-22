# EP639 | 当九成代码由 AI 写就：Claude Code 团队的验证方法论

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-11-16-How the Claude Code team thinks about verification.mp3`
- 时长：33 分 24 秒

## Shownotes（复制到小宇宙）

Claude Code 团队有大约百分之九十的代码由 Claude 自己编写、自己审查。这篇文章讲的就是他们如何让 agent 用证据证明自己写对了，从而把"一次跑一个"变成"同时跑几十上百个"。我们逐条拆解端到端测试、属性测试、差分测试三种武器，以及 verify skill、提交门禁、可靠性清单这些可以直接抄走的工程实践。

本期要点：

- 验证循环不是锦上添花，而是并行的前提：没有它你只能盯着一两个 Claude，有了它才能开几十上百个
- 如果只能投一种测试，选端到端：单元测试可能通过但功能已经坏了，因为写代码的和写测试的共享同一个误解
- 属性测试用"不可能失败的断言"加海量随机输入来打破你的自信，专攻 agent 最容易漏的边界情况
- 差分测试是新旧系统同输入对拍，迁移和重写场景的第一选择
- 检查不能被它所检查的改动修改，否则这个检查从一开始就是坏的
- 团队维护三十九项可靠性清单，每项带可从 diff 读出的触发条件，Claude 每次只看匹配的三到十项

---

原文：How the Claude Code team thinks about verification
链接：https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
发表时间：2026-11-16
本期解读由模型（deepseek-flash）生成，音频由 edge-tts 合成。
