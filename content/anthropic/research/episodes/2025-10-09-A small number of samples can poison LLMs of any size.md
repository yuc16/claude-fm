# EP90 | 两百五十条毒文档就能控制任何大模型：大规模数据投毒实验揭示的安全盲区

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-10-09-A small number of samples can poison LLMs of any size.mp3`
- 时长：23 分 45 秒

## Shownotes（复制到小宇宙）

Anthropic 联合英国人工智能安全研究所和阿兰·图灵研究院发布了一项迄今最大规模的大模型数据投毒研究，结论令人不安：只需往训练数据里混入两百五十条精心构造的恶意文档，就能给任意规模的大语言模型植入后门漏洞——不管模型是六亿参数还是一百三十亿参数，这个数字几乎保持不变。这打破了"大模型因体量大而天然更安全"的普遍假设，也让数据投毒攻击的可行门槛远比以往想象的更低。

- 核心发现：植入后门所需的毒化文档数量是绝对数量而非比例，模型规模不影响攻击门槛
- 实验规模：训练了六亿到一百三十亿参数共四种规模模型，总计七十二个训练配置
- 两百五十条文档约等于四十二万 token，仅占总训练数据的约十六万分之一
- 攻击类型：测试的是"拒绝服务"型后门，触发词出现后模型输出乱码
- 防御视角：数据投毒是对防御者有利的攻击向量，前提是防御者必须先意识到威胁存在
- 实践建议：训练数据的来源审计与安全性需要和模型本身的安全防护同等重视

---

原文：A small number of samples can poison LLMs of any size
链接：https://www.anthropic.com/research/small-samples-poison
发表时间：2025-10-09
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
