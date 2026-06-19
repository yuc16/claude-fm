# EP158 | AI 做裁判会偏心吗？语言模型决策歧视的系统评估与消除方法

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2023-12-07-Evaluating and Mitigating Discrimination in Language Model Decisions.mp3`
- 时长：20 分 12 秒

## Shownotes（复制到小宇宙）

这期我们聊 Anthropic 在 2023 年底发布的一篇重要研究：当语言模型被用于贷款审批、住房申请、招聘筛选这类高风险决策时，它会不会歧视某些人群？研究团队用 AI 生成大规模测试场景，横跨七十个社会决策领域，系统性地检测了 Claude 2.0 的偏见模式，并证明通过精心设计提示词可以显著缓解这些问题。

- 研究动机：语言模型正被引入高风险社会决策场景，歧视风险亟需主动评估而非事后补救
- 核心方法：用语言模型自动生成测试提示词，系统性变化人口学信息，覆盖七十个决策场景
- 主要发现：未干预的 Claude 2.0 在特定场景下同时存在正向歧视和负向歧视
- 缓解手段：通过 prompt engineering 明确公平性指令、控制输入信息、要求决策理由，可显著减少歧视
- 实践启示：减少歧视不等于消除歧视，高风险场景必须持续评估，绝不能一劳永逸
- 重要警示：研究明确声明不推荐将语言模型用于文中所研究的高风险场景的自动化决策

---

原文：Evaluating and Mitigating Discrimination in Language Model Decisions
链接：https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions
发表时间：2023-12-07
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
