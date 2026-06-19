# EP181 | 告别静态密钥：Anthropic 正式开放工作负载身份联合，企业级 AI 认证进入新时代

- 音频文件：`/Users/wangyc/Desktop/projects/claude-fm/content/claude/blog/audio/2026-06-17-Workload Identity Federation (WIF) is now generally available on the Claude Platform.mp3`
- 时长：26 分 24 秒

## Shownotes（复制到小宇宙）

Anthropic 于二〇二六年六月十七日宣布，工作负载身份联合（WIF）在 Claude 平台正式全面开放。这项功能让开发者再也不需要创建、保管或轮换静态 API 密钥，而是直接用 AWS IAM Role、GitHub Actions Token、GCP 服务账号等已有身份来认证 Claude API，彻底改变企业级 AI 集成的安全基础设施范式。

本期节目将深入拆解 WIF 的工作原理、OIDC 身份联合的技术基础、各云平台的实际接入场景，以及如何从静态密钥平滑迁移，适合所有在企业里构建 Claude 应用的工程师收听。

- WIF 用短命令牌替代静态 API 密钥，彻底消灭密钥泄露、轮换、共用三大痛点
- 兼容所有 OIDC 合规身份提供商：AWS IAM、GCP 服务账号、Azure 托管标识、GitHub Actions、Okta 等
- 引入服务账号概念，每个工作负载有独立身份、独立权限范围、独立审计日志
- 联合规则支持细粒度声明匹配，真正落实最小权限原则
- API 密钥与 WIF 可以并存，支持逐个工作负载渐进式迁移
- 联合配置完全支持 Admin API 程序化管理，适合大规模组织的 IaC 集成

---

原文：Workload Identity Federation (WIF) is now generally available on the Claude Platform.
链接：https://claude.com/blog/workload-identity-federation
发表时间：2026-06-17
本期解读由 Claude（claude-sonnet-4-6）生成，音频由 edge-tts 合成。
