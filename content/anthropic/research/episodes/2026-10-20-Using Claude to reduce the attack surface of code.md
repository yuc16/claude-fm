# EP586 | 让危险代码不可达：Claude 如何缩小软件攻击面

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-10-20-Using Claude to reduce the attack surface of code.mp3`
- 时长：24 分 38 秒

## Shownotes（复制到小宇宙）

找漏洞、打补丁之外，AI 还能怎样改善软件安全？本期解读 Anthropic 的攻击面缩减研究，看 Claude 如何从默认配置、配置组合和执行顺序入手，让攻击者碰不到本来就不该暴露的代码。我们也会深入 OpenSSH 案例，讨论怎样把这套方法落到代码审查和持续集成中。

本期要点
- 从“有没有漏洞”转向“攻击者能不能走到这里”，理解攻击面缩减的防御价值
- 二十五个开源项目、超过五百万行代码中的四百九十三项发现，该怎样解读
- 为什么两个看似合理的配置，放在一起可能悄悄关闭安全控制
- OpenSSH 案例：算法被禁用，不代表它的解析与验签代码不可达
- 三轮分析、动态轨迹与回归测试，如何组成可验证的 AI 安全审查流程
- 实践中的边界：攻击面缩减不等于漏洞修复，测试通过也不等于安全证明

---

原文：Using Claude to reduce the attack surface of code
链接：https://www.anthropic.com/research/attack-surface-reduction
发表时间：2026-10-20
本期解读由模型（gpt-6.1-sol）生成，音频由 edge-tts 合成。
