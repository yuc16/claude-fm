# EP227 | 用合规API审计Claude平台里的每一次操作

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-03-30-Audit Claude Platform activity with the Compliance API.mp3`
- 时长：23 分 42 秒

## Shownotes（复制到小宇宙）

Anthropic在2026年3月底为Claude Platform上线了Compliance API,让企业的安全与合规团队第一次能够用程序化的方式拉取组织内的审计日志,而不必再靠人工导出和抽样检查。这期节目带你拆解这个API记录什么、不记录什么,以及企业团队该怎么把它接进自己的合规体系。

- Compliance API提供一个活动信息流,可以按时间范围、用户或API密钥过滤查询
- 记录分两大类:会修改访问权限或配置的管理与系统活动,以及用户创建、修改资源数据的资源活动
- 关键设计:它不记录推理活动,用户和模型之间到底说了什么完全不在审计范围内
- 开通方式需要联系Anthropic客户团队,创建管理员API密钥后才能调用接口
- 日志从开通那一刻才开始记录,没有历史回填,这是一个容易踩的坑
- 已经在用Claude Enterprise合规功能的组织,可以把Claude API组织并入同一个父组织,统一查看两边的活动

---

原文：Audit Claude Platform activity with the Compliance API
链接：https://claude.com/blog/claude-platform-compliance-api
发表时间：2026-03-30
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
