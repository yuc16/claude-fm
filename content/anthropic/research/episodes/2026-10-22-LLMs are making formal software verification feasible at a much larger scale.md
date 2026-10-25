# EP585 | 让证明追上代码：大模型如何放大软件安全验证

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-10-22-LLMs are making formal software verification feasible at a much larger scale.mp3`
- 时长：24 分 52 秒

## Shownotes（复制到小宇宙）

当大模型越来越擅长寻找漏洞，防守方能不能不再只靠“多测一点”，而是证明某些漏洞根本不会出现？本期解读 Anthropic 与 Theorem 的形式化验证研究，拆解 Claude 如何把现有模糊测试变成数学命题，以及这些证明距离真实生产环境还有多远。

本期要点
- 从测试到证明：把“这些输入没出错”升级为“范围内所有输入都不会触发指定错误”
- 一百二十三个开源库、二百三十九个入口：理解汇编级证明的规模与前提
- 证明过程也是漏洞发现过程：为什么长期模糊测试仍会漏掉特殊输入
- 模型负责生成，检查器负责验收：可信边界到底在哪里
- 成本、证明复用与依赖治理：工程团队如何开始小规模试点
- 形式化验证不等于没有漏洞：规格、机器模型和调用方式仍然决定保证范围

---

原文：LLMs are making formal software verification feasible at a much larger scale
链接：https://www.anthropic.com/research/formal-verification
发表时间：2026-10-22
本期解读由模型（gpt-6.1-sol）生成，音频由 edge-tts 合成。
