# EP20 | 让 AI 智能体跨越多个会话持续推进复杂任务的框架设计实践

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2025-11-26-Effective harnesses for long-running agents.mp3`
- 时长：26 分 22 秒

## Shownotes（复制到小宇宙）

当你让 AI agent 独立完成一个需要好几天的大型项目，它会在哪些地方翻车？Anthropic 工程团队用「克隆 claude.ai」这个真实任务做了系统性实验，发现了两个最致命的失败模式，并设计出一套两阶段框架来解决它们。本期我们逐层拆解这套框架的每个关键设计决策，以及背后的工程逻辑。

- 核心挑战：每个新上下文窗口对 agent 来说相当于失忆，需要从零恢复状态
- 失败模式一：agent 一口气想把整个项目做完，结果上下文用尽，留下半成品烂摊子
- 失败模式二：做了几个功能之后就宣告完成，大量需求根本没有碰过
- 解法一：初始化 agent 负责打地基——init.sh 脚本、进度记录文件、JSON 格式功能验收清单、初始 git 提交
- 解法二：编程 agent 每次只做一个功能，完成后做 git commit、更新进度文件，保持环境「干净收工」
- 端到端测试的重要性：用浏览器自动化工具像真实用户一样验收，而不只是跑单元测试或 curl

---

原文：Effective harnesses for long-running agents
链接：https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
发表时间：2025-11-26
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
