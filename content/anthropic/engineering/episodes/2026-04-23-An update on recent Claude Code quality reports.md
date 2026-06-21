# EP370 | Claude Code 三月危机：Anthropic 罕见公开的工程事故全复盘

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/engineering/audio/2026-04-23-An update on recent Claude Code quality reports.mp3`
- 时长：28 分 11 秒

## Shownotes（复制到小宇宙）

本期我们拆解 Anthropic 发布的一份罕见的工程事故报告。今年三月到四月，Claude Code 用户陆续反映质量下滑——有人说变笨了，有人说容易忘事，有人说用量额度消耗异常快。Anthropic 最终查明，这背后是三个相互独立的工程变动叠加导致的，每一个单独看都有其道理，合在一起却产生了难以捉摸的系统性退化。

- 推理努力级别被降至 medium，内部测试说差不多，用户说明显变笨
- 思维历史清除的 bug：本来只清一次，结果每轮都清，Claude 越来越失忆
- 一条 25 词限制的系统提示词，和其他指令叠加后导致代码质量下降 3%
- 三个问题影响不同用户、不同场景，合在一起呈现出难以复现的模糊退化感
- Opus 4.7 事后用代码审查找到了 bug，Opus 4.6 没找到——新模型的实际差距
- benchmark 和真实用例的 gap、内外部测试环境差异：经典工程教训的 AI 版本

---

原文：An update on recent Claude Code quality reports
链接：https://www.anthropic.com/engineering/april-23-postmortem
发表时间：2026-04-23
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
