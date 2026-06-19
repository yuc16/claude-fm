# EP99 | 用密码学证明 AI 没有偷看你的数据：Anthropic 机密推理架构深解

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/anthropic/research/audio/2025-06-18-Confidential Inference via Trusted Virtual Machines.mp3`
- 时长：21 分 10 秒

## Shownotes（复制到小宇宙）

你把公司代码、客户合同、财务报告发给 Claude，服务器那端到底发生了什么？数据在多少个环节是"裸奔"状态？这期节目带你深入 Anthropic 在 2023 年发布的机密推理研究，看他们如何用可信执行环境和密码学证明链，把"请相信我们的承诺"升级为"数学可验证的保证"。

- 什么是机密推理，为什么"加密传输"远远不够
- 推理服务器的分层架构：不可信主体 + 极小可信加载器
- TPM 可信平台模块如何生成不可伪造的环境证明书
- 密钥服务器的角色：证明通过才给钥匙，一步都不能少
- 多方独立密钥管理的设想，以及它对企业合规的意义
- 机密推理的现实局限：硬件依赖、性能开销、它保护的边界在哪里

---

原文：Confidential Inference via Trusted Virtual Machines
链接：https://www.anthropic.com/research/confidential-inference-trusted-vms
发表时间：2025-06-18
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
