# EP357 | AI让漏洞利用窗口缩短到小时级，Anthropic给出七条重构安全防线的实战建议

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-10-Preparing your security program for AI-accelerated offense.mp3`
- 时长：28 分 14 秒

## Shownotes（复制到小宇宙）

Anthropic 安全工程团队用最前沿的模型扫描真实代码库后，把亲身观察到的现象整理成了一份行动清单：在接下来两年内，潜伏代码库多年的漏洞将被 AI 批量发现并串联成可用的利用链——但防御方同样可以用这些工具反过来保护自己。本期逐层拆解这篇文章的七条建议，从补丁窗口、漏洞数量爆炸、CI 安全、零信任设计到事件响应，每条都有今天就能落地的具体操作。

本期要点

- AI 让"补丁反向工程"速度从天级缩短到小时级，补丁缺口从麻烦变成紧急风险
- CISA KEV 目录 + EPSS 评分系统：用两张清单把几千个 CVE 变成可管理的优先级队列
- 漏洞数量将出现数量级增长，依赖电子表格和周例会的漏洞管理流程撑不住
- 在 CI/CD 里部署 AI 漏洞扫描：用攻击者会用的模型，在攻击者之前扫描你自己的代码
- 零信任架构的核心不是"增加麻烦"，而是构建即使面对有无限耐心的攻击者也成立的硬性屏障
- 提交漏洞报告前，关掉编辑器、凭记忆讲一遍——讲不清楚就说明还没准备好报告

---

原文：Preparing your security program for AI-accelerated offense
链接：https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense
发表时间：2026-04-10
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
