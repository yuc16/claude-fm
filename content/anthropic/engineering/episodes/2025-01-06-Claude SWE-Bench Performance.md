# EP123 | Claude 四十九分背后的工程哲学：用最简脚手架撬动真实软件工程能力的底层逻辑

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-01-06-Claude SWE-Bench Performance.mp3`
- 时长：25 分 52 秒

## Shownotes（复制到小宇宙）

本期聊的是 Anthropic 工程博客于 2025 年 1 月发布的一篇技术文章，详细拆解了他们如何围绕 Claude 3.5 Sonnet 构建 agent 系统，在 SWE-bench Verified 评测上取得 49% 的成绩，超越当时的最高水准 45%。文章的核心价值不在分数本身，而在于其背后的工程设计哲学——工具接口该怎么设计、给模型多少自主权、以及评测基准的真实局限性。

- **SWE-bench 是什么**：用真实 GitHub issue 考察 AI 解决软件工程问题的全流程能力，远比代码补全难
- **Anthropic 的核心哲学**：给模型最大自主权，脚手架越简单越好，不要把工作流写死
- **工具接口设计的关键**：Bash 工具和 Edit 工具的描述字段比功能本身更重要，防错胜过纠错
- **真实案例拆解**：模型如何分六步诊断并修复 scikit-learn 的一个参数传递 bug
- **跑 SWE-bench 踩过的四个坑**：成本、评分可靠性、隐藏测试、多模态缺失
- **对开发者的启示**：如何把这套思路迁移到自己的 coding agent 构建实践中

---

原文：Claude SWE-Bench Performance
链接：https://www.anthropic.com/engineering/swe-bench-sonnet
发表时间：2025-01-06
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
