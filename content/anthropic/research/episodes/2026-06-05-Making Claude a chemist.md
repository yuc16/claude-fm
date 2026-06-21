# EP430 | 当 Claude 拿起核磁共振仪：Anthropic 让 AI 真正走进化学实验室

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-06-05-Making Claude a chemist.mp3`
- 时长：30 分 23 秒

## Shownotes（复制到小宇宙）

Anthropic 发布首篇化学方向白皮书，用严格的 benchmark 对比了 Claude 三个版本与 ChemDraw、MestReNova 两款行业标准软件在核磁共振谱图分析上的表现。结果出人意料：Opus 4.7 在氢谱预测精度上胜出，在逆向结构解析（从谱图反推分子）这个专业软件做不好的任务上更展示了令人印象深刻的能力。这期节目带你深入拆解这篇白皮书的实验设计、结果和局限性，并聊聊对工程师和 AI 从业者的实际意义。

- 化学家需要在四种"语言"之间来回切换：手绘结构、仪器谱图、SMILES 字符串、系统命名，翻译工作极度耗时
- NMR 核磁共振是合成化学里最常见的结构确认手段，每个新化合物都要手动分析，是流程瓶颈
- Opus 4.7 氢谱平均误差 ±0.079 ppm，远低于化学家认可的 ±0.2 ppm 容差；碳谱与 MestReNova 基本并列
- 在耦合常数（子峰间距）预测上，Claude 三个版本均约 80% 准确率，而 ChemDraw/MestReNova 只有 26-35%
- 逆向结构解析：给定分子式+一维谱图，Opus 4.7 对简单分子满分通过，复杂分子也有 4/7 全对
- 局限清单同样重要：20 个样本统计力度有限，无法处理立体化学，复杂结构会陷入推理循环

---

原文：Making Claude a chemist
链接：https://www.anthropic.com/research/making-claude-a-chemist
发表时间：2026-06-05
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
