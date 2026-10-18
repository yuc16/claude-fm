# EP571 | 当智能体撑爆代码仓库，版本控制该如何重建

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2026-10-13-Redesigning source control at Anthropic.mp3`
- 时长：24 分 00 秒

## Shownotes（复制到小宇宙）

当每天合入的代码变更从两千五百次增长到三万多次，瓶颈就从写代码转移到了开发基础设施。本期解读 Anthropic 如何用五个月构建并迁移到内部版本控制系统 Scion，以及普通工程团队真正值得借鉴的架构思想。

本期要点
- 为什么面向离线协作的 Git，在始终在线的智能体工作负载下出现规模压力
- Scion 如何通过服务端计算、增量变更集和派生数据组织超大仓库
- 按需获取对象与分层缓存，如何降低代码检出的成本
- 七人团队快速迁移的背后，工程师如何把守约束、审查意图与系统质量
- 当变更速度超过测试速度，持续集成与合并队列需要重新思考
- 不必重造版本控制：从查询接口、共享缓存和工作流测量开始改进

---

原文：Redesigning source control at Anthropic
链接：https://www.anthropic.com/engineering/redesigning-source-control
发表时间：2026-10-13
本期解读由模型（gpt-6.1-sol）生成，音频由 edge-tts 合成。
