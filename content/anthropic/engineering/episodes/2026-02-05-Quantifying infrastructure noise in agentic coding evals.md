# EP304 | 六个百分点的差距：AI 编程评测中被忽视的基础设施噪声

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2026-02-05-Quantifying infrastructure noise in agentic coding evals.mp3`
- 时长：27 分 04 秒

## Shownotes（复制到小宇宙）

Anthropic 工程团队做了一件很务实的事：他们去量化了 AI 编程排行榜上的数字到底有多少是基础设施配置带来的误差。结论相当惊人——仅仅改变容器的内存上限，就能让 Terminal-Bench 的分数产生高达六个百分点的差距，而顶尖模型之间的差距往往只有两三个百分点。

- 静态评测 vs 智能体评测：为什么运行环境的配置在 agentic coding eval 里不再是"无关背景"
- Kubernetes 的陷阱：资源"申请量"和"硬上限"设成相同值，会带来多高的基础设施错误率
- 两层效应：三倍以内是修复基础设施可靠性，三倍以上是真正改变了 agent 能解决哪些问题
- 策略战争：安装重型工具库 vs 从头实现精简代码，资源配置决定哪种策略能赢
- SWE-bench 的交叉验证：效应更小但方向一致，资源配置在主流评测集里都不是中性变量
- 工程师实践建议：三个百分点以内的排行差距怎么看，你的选型评测应该在什么配置下跑

---

原文：Quantifying infrastructure noise in agentic coding evals
链接：https://www.anthropic.com/engineering/infrastructure-noise
发表时间：2026-02-05
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
