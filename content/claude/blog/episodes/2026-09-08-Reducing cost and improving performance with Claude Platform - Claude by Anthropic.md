# EP540 | 不牺牲性能砍掉一半成本：Claude 平台的三大降本杠杆与三个审计命令

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-09-08-Reducing cost and improving performance with Claude Platform - Claude by Anthropic.mp3`
- 时长：32 分 04 秒

## Shownotes（复制到小宇宙）

Anthropic 在二〇二六年九月八日发布了一篇很实用的工程指南：用 Claude Platform 的应用完全可以在不牺牲性能的前提下把成本砍下来。文章给出三个杠杆——把提示缓存命中率拉满、在升级前沿模型时清掉提示词里的反模式、把 effort 校准到任务本身，并把这套经验固化成了 Claude Code 里的三个命令。

本期要点：
- 提示缓存的成本机制：prefill 是输入处理最贵的一步，缓存读取只按完整输入价格的一小部分计费，但缓存写入要付一点二五倍甚至两倍的价格
- 缓存失效的五个隐形杀手：中途改 effort 设置、前缀里的动态时间戳、自我重排序的工具定义、非字节一致的对话 fork、活过 TTL 的同步工具调用
- 六种拖垮前沿模型的提示词反模式，以及一次模拟升级实验的结果：跑一遍 prompt-audit 后成本降百分之十四点六、准确率反而升百分之五点三
- effort 校准的两条真实曲线：便宜模型拼命干，往往不如强模型轻松干，Fable 五点一在低 effort 下用三分之一成本追平 Fable 五
- hillclimb 在客户支持基准上的搜索过程：从 Opus 四点八 起步，一路降到 Sonnet 五加低 effort，最终在留出集上准确率从百分之七十八点六升到百分之九十点五，成本约五分之一
- cost-optimize 在四个公开基准上的结果：LegalBench 降百分之五十八、tau2-bench 零售降百分之七十三、OfficeQA Pro 降百分之五十二、SWE-bench Verified 降百分之五十五

---

原文：Reducing cost and improving performance with Claude Platform | Claude by Anthropic
链接：https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
发表时间：2026-09-08
本期解读由模型（deepseek-v4-flash）生成，音频由 edge-tts 合成。
