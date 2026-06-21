# EP210 | Claude 上下文管理新功能：让智能体不再"失忆"也不再"爆窗"

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2025-09-29-Managing context on the Claude Developer Platform.mp3`
- 时长：21 分 15 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊 Anthropic 在二〇二五年九月底发布的一篇博客,主题是 Claude Developer Platform 上新增的两个上下文管理能力,一个叫上下文编辑,一个叫记忆工具。这两个功能专门用来解决长时间运行的智能体在执行复杂任务时会遇到的两个老大难问题,一个是上下文窗口被各种工具调用结果撑爆,一个是跨会话的知识没办法保留下来。我们会拆解这两个功能具体是怎么工作的,官方给出的实测数据说明了什么,以及作为开发者你应该怎么把它们用到自己的智能体项目里。

- 上下文编辑会自动清理过期的工具调用和结果,让对话能跑得更久而不触发上限
- 记忆工具让 Claude 能把信息写到文件系统里,跨会话保留项目状态和经验
- 两者结合在内部评测中带来百分之三十九的性能提升,单独用上下文编辑也有百分之二十九的提升
- 在一百轮的网页搜索评测里,上下文编辑让原本会失败的任务跑完了,还把 token 消耗降低了百分之八十四
- 这两个功能目前是公开测试版,在 Claude 原生平台、亚马逊 Bedrock 和谷歌云 Vertex AI 上都能用
- 适合编程类智能体、长周期研究类智能体、以及大批量数据处理类智能体

---

原文：Managing context on the Claude Developer Platform
链接：https://claude.com/blog/context-management
发表时间：2025-09-29
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
