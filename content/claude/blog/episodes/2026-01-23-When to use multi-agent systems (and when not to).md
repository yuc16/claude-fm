# EP289 | 别急着上多智能体,这三个场景才真正该用

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-01-23-When to use multi-agent systems (and when not to).mp3`
- 时长：26 分 39 秒

## Shownotes（复制到小宇宙）

本期我们聊一聊 Anthropic 官方博客的最新文章,什么时候该用多智能体系统,什么时候不该用。文章的核心态度挺出乎意料:大多数场景下,一个设计得当的单智能体远比想象中强大,多智能体系统只在三种特定情况下才真正划得来。我们会拆解这三种场景、一个反直觉的任务拆分原则,以及一个性价比很高的验证子智能体模式。

- 单智能体被严重低估:配置得当的单智能体能完成的任务,远超大多数开发者的预期
- 多智能体的隐藏成本:同等任务下通常要多花三到十倍的 token,协调开销可能反超执行本身
- 真正该用多智能体的三种场景:上下文污染需要隔离、任务可以并行探索、不同任务需要不同工具或专业知识
- 反直觉的拆分原则:按上下文边界分工,而不是按角色或工作类型分工,否则容易陷入信息层层失真的电话游戏
- 验证子智能体:用一个独立智能体专门做黑盒测试和校验,成本低、效果好,但要把验证标准写得足够死板具体
- 几个实用信号:工具数量超过十五到二十个时,先试试动态工具检索,而不是急着拆多智能体

---

原文：When to use multi-agent systems (and when not to)
链接：https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
发表时间：2026-01-23
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
