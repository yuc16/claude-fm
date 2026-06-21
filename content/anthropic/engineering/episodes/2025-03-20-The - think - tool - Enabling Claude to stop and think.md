# EP139 | 给 AI 装上"暂停键"：Anthropic 的 think 工具如何让 Claude 在工具调用中学会深呼吸

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-03-20-The - think - tool - Enabling Claude to stop and think.mp3`
- 时长：21 分 55 秒

## Shownotes（复制到小宇宙）

这期节目带你深挖 Anthropic 工程团队发布的一篇技术文章，他们给 Claude 加了一个叫"think"的特殊工具，让模型在执行复杂任务时能主动停下来想清楚再行动。结果在客服场景的压力测试里，航空域的通过率直接提升了 54%。文章发表于 2025 年 3 月，距今已超过一年，我会结合后续进展来讲清楚这个技术的前世今生。

- think 工具的核心思路：给模型一块"草稿纸"，让它在工具调用链中途停下来梳理信息
- think 工具与 extended thinking（扩展思考）的本质区别：一个用于行动中途，一个用于行动之前
- tau-bench 基准测试结果：有无 think 工具、有无优化 prompt 的四种配置对比
- 优化 prompt 的关键作用：在复杂策略场景下，光有工具不够，还得告诉模型怎么用
- 适用与不适用的场景边界：哪类任务加了有用，哪类任务加了白费
- 2025 年 12 月的重要更新：extended thinking 能力提升后，Anthropic 推荐大多数场景优先用它而非 think 工具

---

原文：The "think" tool: Enabling Claude to stop and think
链接：https://www.anthropic.com/engineering/claude-think-tool
发表时间：2025-03-20
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
