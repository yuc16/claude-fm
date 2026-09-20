# EP548 | 智能体写代码压垮 CI：Anthropic 重造测试影响分析服务

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-09-14-Agentic coding is straining CI. Here’s how we scaled test impact analysis at Anthropic - Claude by Anthropic.mp3`
- 时长：25 分 02 秒

## Shownotes（复制到小宇宙）

Anthropic 的 CI 作业量在六个月内涨了二十五倍，核心原因是 Claude 写了百分之八十的代码、测试量涨了十倍、而工程师人数几乎没变。这篇文章复盘了他们三次打补丁、三次失败、最终推倒重来重造测试影响分析服务的全过程，以及一个反直觉的结论：当写代码不再是瓶颈，扩容技巧买来的时间只剩一年前的零头。

本期要点：
- Anthropic 工程师人均季度代码产出是过去几年的八倍，Claude 撰写其中百分之八十，同时深度参与 PR 审查
- 测试影响分析服务由 listener 和 selector 两个确定性组件构成，listener 落后二十分钟就可能导致几万条测试结果丢失
- 三次快速修复：加倍 CPU 核心撑了七十天、按代码包并行分片撑了二十九天、每日重启撑了不到一天
- 最终方案是把状态从进程里搬进内存数据存储，让 listener 变成无状态、可水平扩展，一个工程师三周完成
- 作者建议：无论自建还是采购，都假设你的架构两个季度内会承受二十五倍负载
- 核心洞察不是"怎么扩容"，而是"为指数增长做规划"——半吊子方案浪费的时间远比你想的多

---

原文：Agentic coding is straining CI. Here’s how we scaled test impact analysis at Anthropic | Claude by Anthropic
链接：https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
发表时间：2026-09-14
本期解读由模型（deepseek-v4-flash）生成，音频由 edge-tts 合成。
