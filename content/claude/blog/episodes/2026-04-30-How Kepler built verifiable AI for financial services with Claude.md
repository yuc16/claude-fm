# EP219 | 把推理交给 Claude，把验证交给系统：Kepler 的金融 AI 信任架构

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-04-30-How Kepler built verifiable AI for financial services with Claude.mp3`
- 时长：24 分 18 秒

## Shownotes（复制到小宇宙）

金融机构最怕的不是 AI 算错，而是算错了还查不出来。这期我们聊 Anthropic 案例文章里的创业公司 Kepler，他们把 Claude 的推理能力和一套完全确定性的基础设施分开，做出一个能把每个数字精确追溯到原始文件、页码、行项目的金融研究平台，目前已经索引了两千六百多万份监管文件，覆盖一万四千多家公司、二十七个市场。

- Kepler 创始团队出身 Palantir，创业前先做了一百四十七场用户访谈，发现金融机构都想用 AI 做研究，但完全不信任 AI 给出的结果
- 核心思路是把"理解问题"和"计算数字"拆成两个阶段：理解交给 Claude，计算交给确定性执行环境，避免模型心算时产生幻觉
- 在长链条、多步骤的复杂任务上，Claude 比其他前沿模型更能稳定执行计划，遇到术语歧义时会主动停下来询问，而不是自己瞎猜往下走
- Kepler 提出"内容工程"概念：围绕 Claude 搭建专有金融本体、权限控制、幂等技能模块，把模型当成流水线里的一环，而不是整个系统
- 多模型分阶段调度：复杂推理交给 Opus，高吞吐量任务交给 Sonnet，外加自训练的小模型把特定召回任务的准确率做到百分之九十四
- 评测体系、审计日志、数据溯源从第一天就内建进系统，并已通过 SOC 2 Type II 认证

---

原文：How Kepler built verifiable AI for financial services with Claude
链接：https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude
发表时间：2026-04-30
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
