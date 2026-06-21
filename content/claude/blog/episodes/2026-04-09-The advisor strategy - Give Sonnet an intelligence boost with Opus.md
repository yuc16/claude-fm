# EP354 | 顾问策略:Opus当军师,Sonnet去打仗,省钱又聪明

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-09-The advisor strategy - Give Sonnet an intelligence boost with Opus.mp3`
- 时长：19 分 17 秒

## Shownotes（复制到小宇宙）

本期我们聊聊 Anthropic 最新发布的顾问策略,核心思路是让便宜快速的 Sonnet 或 Haiku 模型负责干活,遇到搞不定的难题再向更聪明但更贵的 Opus 模型求助一句,从而用接近 Sonnet 的成本拿到接近 Opus 的智能水平。Anthropic 还顺手把这个模式做成了 API 里的一个 advisor 工具,开发者理论上加一行配置就能用上。我们会拆解这个机制具体怎么运作、官方测试数据说明了什么,以及你在自己的项目里怎么落地、要避开哪些坑。

本期要点:
- 顾问策略反转了常见的大模型做指挥官、小模型做苦力的子智能体套路,改成小模型自己扛全程,只在卡住的关键节点临时连线 Opus 要个主意
- Opus 顾问只给建议,不调用工具、不直接面向用户输出,主导权始终在 Sonnet 或 Haiku 手里
- 官方在 SWE-bench Multilingual 上测得 Sonnet 加顾问比单独跑 Sonnet 提升二点七个百分点,成本反而降低百分之十一点九
- Haiku 加 Opus 顾问在 BrowseComp 上的得分是单独跑 Haiku 的两倍以上,成本却只是单独跑 Sonnet 的一小部分,适合海量任务场景
- advisor 工具现在是 Claude Platform 上的公开测试功能,加一个 beta 请求头、声明 advisor 工具类型,再调整系统提示词即可接入
- 落地前建议先用自己的评测集对比单独跑 Sonnet、Sonnet 加顾问、单独跑 Opus 三种方案,系统提示词怎么引导执行者求助是关键变量

---

原文：The advisor strategy: Give Sonnet an intelligence boost with Opus
链接：https://claude.com/blog/the-advisor-strategy
发表时间：2026-04-09
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
