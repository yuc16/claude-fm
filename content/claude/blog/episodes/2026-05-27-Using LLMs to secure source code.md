# EP418 | AI 已能批量找出漏洞，但九成七没被修：Anthropic 的代码安全六步实战法

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-05-27-Using LLMs to secure source code.mp3`
- 时长：23 分 53 秒

## Shownotes（复制到小宇宙）

Anthropic 安全团队在帮助多个组织扫描代码库的过程中，发现了一个触目惊心的现象：他们披露的一千五百九十六个漏洞，只有九十七个被修复。问题不在"找"，而在"找到之后"。

这期节目拆解 Anthropic 总结的六步实战流程——从威胁建模、沙箱搭建，到发现、验证、分级筛选、修复——帮你建立一套真正能从发现走到修复的 AI 安全工程体系。

- 误报率高达 40% 的根因：模型"对代码理解很好，但对我们理解不够"，威胁建模是解药
- 反直觉发现：给发现 agent 的提示词越简单越好，详细检查清单反而限制创造力
- 发现和验证必须分开用独立 agent，合并会导致真阳性被自我过滤
- 对抗性验证可将假阳性率减半，再要求 PoC 可降至接近零
- 分级筛选现在是真正的瓶颈，要在扩大扫描规模前先建好下游流水线
- 补丁要测试驱动、找变体、做对抗性检查，避免修症状不修根因

---

原文：Using LLMs to secure source code
链接：https://claude.com/blog/using-llms-to-secure-source-code
发表时间：2026-05-27
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
