# EP6 | 从人类反馈到对齐：深解 Anthropic 奠基之作，如何训练既有用又无害的 AI 助手

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2022-04-12-Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback.mp3`
- 时长：22 分 57 秒

## Shownotes（复制到小宇宙）

本期精读 Anthropic 核心对齐论文——《基于人类反馈的强化学习训练有用且无害的助手》。这篇文章系统揭示了 Claude 背后最基础的训练逻辑：通过偏好建模与强化学习的组合，让语言模型真正学会什么是"好的回答"，同时避免输出有害内容。理解它，就是理解现代 AI 助手如何被"驯化"的第一步。

- RLHF 完整链路解析：从人类比较判断到偏好模型，再到强化学习策略更新的三阶段流程
- 偏好建模为何比直接打分更有效：一个认知科学原理背后的关键工程选择
- "有用"与"无害"真的互相矛盾吗？论文给出的实验结论出人意料
- 奖励过优化陷阱：为什么 AI 会学会"讨好评委"而非真正提高质量
- KL 散度与奖励的线性关系：一个被严重低估的工程实践发现
- 对今天 AI 应用开发者的三条具体启示：数据飞轮、多维评估、对齐与能力的真实关系

---

原文：Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
链接：https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback
发表时间：2022-04-12
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
