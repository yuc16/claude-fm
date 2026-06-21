# EP250 | 让 Claude 学会边搜索边过滤,网页搜索准确率与效率双提升

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-02-17-Improved Web Search with Dynamic Filtering.mp3`
- 时长：22 分 35 秒

## Shownotes（复制到小宇宙）

这一期我们聊聊 Anthropic 在二〇二六年二月发布的一篇技术博客,主题是网页搜索工具的动态过滤升级。核心结论是,让模型在搜索过程中自己写代码来筛选搜索结果,而不是把整页网页内容塞进上下文窗口,既能提升回答准确率,又能省下不少 token。我们会拆解这个机制的工作原理,看看在两个权威基准测试上的具体数据,顺便聊聊这次一起发布的几个配套能力,比如代码执行、记忆功能、程序化工具调用,最后说说这对正在搭建搜索类 agent 的工程师们意味着什么。

本期要点
- 动态过滤的核心思路:让 Claude 在网页搜索时自动写代码,对搜索结果做后处理筛选,只保留有用信息再进入上下文
- 为什么传统网页搜索很烧 token:整页 HTML 拉入上下文,信息密度低,还会拉低回答质量
- BrowseComp 基准测试结果:Sonnet 四点六从百分之三十三点三提升到百分之四十六点六,Opus 四点六从百分之四十五点三提升到百分之六十一点六
- DeepsearchQA 基准测试结果:衡量多答案搜索任务的完整性和准确性,F1 分数同样有明显提升
- token 成本的两面性:平均省了百分之二十四的输入 token,但价格加权后的成本在不同模型上表现不同,需要用自己的真实查询去实测
- 配套发布的五件套:代码执行、记忆、程序化工具调用、工具搜索、工具使用示例,全部进入正式可用阶段

---

原文：Improved Web Search with Dynamic Filtering
链接：https://claude.com/blog/improved-web-search-with-dynamic-filtering
发表时间：2026-02-17
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
