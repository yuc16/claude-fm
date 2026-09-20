# EP541 | Claude 用四周优化三十多个生物模型：蛋白质设计的算力门槛被打下来了

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2026-09-17-How Claude is uplifting biomolecular modeling.mp3`
- 时长：29 分 38 秒

## Shownotes（复制到小宇宙）

本期解读 Anthropic 在二〇二六年九月十七日发布的技术文章《Claude 如何托起生物分子建模》。文章讲的是 Claude 在不到四周时间里优化了三十多个开源生物分子模型，平均加速约四倍，还做出了能在单张 GPU 节点上推理七万个 token 系统的低内存模式，并把蛋白质设计流程的成本从每个目标上万美元压到约一百五十美元。所有优化代码已开源，同时启动了一项由百万美元 Claude 额度支持的蛋白质设计竞赛。

本期要点：
- 现代结构预测模型的瓶颈在三角形注意力和三角形乘法，这两个操作的计算复杂度和内存占用都是立方级
- Claude 开发的 FlashPairformer 内核，在三角形注意力上比当时的行业标准快二点七到二点九倍
- 通过缓存冗余计算、把死分支简化成常量输出等逐模型优化，三十多个模型平均加速四倍，完全一致输出时接近两倍
- 低内存 Big 模式让单张 GPU 节点就能推理超过七万个 token 的分子系统，包括线粒体复合体一和细菌核糖体
- 蛋白质设计流程从一万六千词提示词加多智能体，简化为一千一百词提示词加单模型单卡，总成本约一百五十美元
- 与 Adaptyv Bio 合办竞赛，验证超过五千个设计，提供最高一百万美元 Claude 额度和二十五万美元 Modal 计算额度

---

原文：How Claude is uplifting biomolecular modeling
链接：https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling
发表时间：2026-09-17
本期解读由模型（deepseek-v4-flash）生成，音频由 edge-tts 合成。
