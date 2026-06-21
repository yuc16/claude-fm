# EP66 | 当上下文成为武器：Anthropic 揭秘多轮示例越狱攻击原理与防御

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2024-04-02-Many-shot jailbreaking.mp3`
- 时长：18 分 26 秒

## Shownotes（复制到小宇宙）

今天我们聊的是 Anthropic 于二零二四年三月发表的一篇安全研究——"Many-shot jailbreaking"（多轮示例越狱攻击）。他们发现，越来越长的大模型上下文窗口，在带来强大能力的同时，也打开了一扇全新的攻击大门。更出人意料的是：模型越大越聪明，反而对这种攻击越脆弱。

- 什么是多轮示例越狱：通过在 prompt 中塞入大量伪造的人机对话，临时"覆盖"模型的安全训练
- 为什么它有效：根本原因是大模型的 in-context learning 能力被恶意利用
- 越大越脆弱：大模型 in-context learning 能力越强，反而越容易被这种方式操控
- 三种防御方向的实验结果：限制上下文、微调、prompt 预处理，效果差异悬殊
- 最有效的缓解手段将攻击成功率从 61% 降至 2%，但"猫鼠游戏"仍在继续
- 对工程师的实际启示：安全需要分层防御，不能只靠模型自带的安全训练

---

原文：Many-shot jailbreaking
链接：https://www.anthropic.com/research/many-shot-jailbreaking
发表时间：2024-04-02
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
