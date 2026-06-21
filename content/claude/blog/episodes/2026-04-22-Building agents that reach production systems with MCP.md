# EP368 | API、CLI 还是 MCP？智能体接入生产系统该怎么选

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-22-Building agents that reach production systems with MCP.mp3`
- 时长：25 分 31 秒

## Shownotes（复制到小宇宙）

智能体要真正干活,得连得上你的业务系统。这件事一般有三条路:直接调用API、跑CLI命令、或者接入MCP协议。这一期我们跟着Anthropic这篇文章把三条路的优劣摆开来讲清楚,重点拆解云端生产级智能体为什么越来越离不开MCP,以及怎么把MCP服务端和客户端都做得真正好用。

本期要点:
- 三条连接路径的核心差异:直接调用API面临M乘N集成难题,CLI受限于本地shell环境,MCP提供跨客户端、跨部署环境的统一协议层
- MCP生态月下载量从一亿涨到三亿多,已经支撑起Claude Cowork、Claude Managed Agents等产品
- 搭建MCP服务端的关键设计模式:远程优先、按意图分组工具而不是照搬API端点、超大接口面用代码编排、用MCP Apps和elicitation提供富交互、用CIMD和令牌保险库做标准化认证
- Cloudflare的例子:两个工具搜索和执行,用约一千token覆盖两千五百个接口
- MCP客户端侧的两个省token技巧:工具按需检索能省下八成以上的工具定义token,代码沙箱处理结果能省下约四成的多步骤工作流token
- skill和MCP是互补关系:MCP给能力,skill给方法论,两者打包成插件或从服务端直接分发技能会成为越来越常见的模式

---

原文：Building agents that reach production systems with MCP
链接：https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
发表时间：2026-04-22
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
