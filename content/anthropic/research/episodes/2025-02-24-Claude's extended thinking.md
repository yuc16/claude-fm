# EP96 | 让 AI 多想一会儿：Claude 扩展思考的推理机制、安全边界与工程实践

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-02-24-Claude's extended thinking.mp3`
- 时长：28 分 45 秒

## Shownotes（复制到小宇宙）

本期拆解 Anthropic 于 2025 年 2 月发布的技术博客《Claude's Extended Thinking》。Claude 三点七 Sonnet 获得了"扩展思考"能力——在给出答案之前，先花时间做内部草稿式推理，并且把这段思考过程原原本本地展示给用户。这听起来像一个简单的功能更新，但背后涉及推理架构、忠实性难题、并行计算策略和安全防线等一系列深层问题，值得认真拆开来讲。

- 扩展思考不是换了新模型，而是给同一个模型更多的推理时间和 token 配额
- 可见的思考过程能增强信任，但"忠实性"问题意味着它不一定代表模型真实的决策路径
- Claude 打通关卡版《精灵宝可梦》背后，是 agent 长程目标追踪能力的真实体现
- 串行加深度 vs 并行加广度：两种测试时计算策略各有适用场景，GPQA 物理子项达到 96.5 分
- prompt injection 防御率从 74% 提升到 88%，但剩下 12% 在高风险场景下绝对不够用
- 开发者必知：如何设思考预算、何时关掉扩展思考、如何在产品里展示思考过程

---

原文：Claude's extended thinking
链接：https://www.anthropic.com/research/visible-extended-thinking
发表时间：2025-02-24
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
