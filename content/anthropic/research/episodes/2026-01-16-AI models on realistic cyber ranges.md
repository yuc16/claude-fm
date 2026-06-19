# EP147 | AI攻防新前线：Claude仅用标准工具独立突破真实网络靶场

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-01-16-AI models on realistic cyber ranges.mp3`
- 时长：19 分 06 秒

## Shownotes（复制到小宇宙）

Anthropic前沿红队最新研究发现，Claude Sonnet 4.5已能在不借助任何定制工具的情况下，仅凭标准渗透测试工具完成对真实网络靶场的多阶段攻击，包括高度仿真的 Equifax 数据泄露模拟场景。这一突破标志着 AI 网络攻击能力从"需要专用工具辅助"向"自主利用标准工具"的关键跃迁，对安全行业影响深远。

- Sonnet 4.5 在五次 Equifax 模拟中成功两次，仅用 Bash shell 和 Kali Linux 标准工具，无需定制框架
- 模型能瞬间识别 CVE-2017-5638（Apache Struts 2 远程代码执行漏洞），无需查阅直接写出 exploit 代码
- 三份实验记录对比：3.5 版本迷失探索无功而返、有 Incalmo 框架辅助的 3.5 版本全面攻陷 50 台主机、4.5 版本凭标准工具独立完成攻击链
- N-day 漏洞在 AI 加持下，从公开披露到被利用的时间窗口将大幅压缩，补丁管理策略需要重新审视
- 防御侧同样需要 AI 赋能工具才能跟上攻击侧的节奏，研究呼吁加快投入

---

原文：AI models on realistic cyber ranges
链接：https://www.anthropic.com/research/cyber-toolkits-update
发表时间：2026-01-16
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
