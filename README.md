<div align="center">

# Claude FM 📻

**把 Anthropic 的前沿技术内容，做成中文解读，装进你的通勤路上。**

智能体 · 可解释性 · 模型发布 · 安全研究 —— 一周更新一次，碎片时间听懂最前沿的 AI

![episodes](https://img.shields.io/badge/已更新-448%20集-1DB954)
![update](https://img.shields.io/badge/更新频率-每周日-FF8800)
![language](https://img.shields.io/badge/语言-中文解读-blue)

</div>

---

## 这是什么

[Anthropic](https://www.anthropic.com)（Claude 背后的公司）在 engineering、research、news 和官方 blog 上持续发布大量高质量的 AI 技术内容，但几乎全是英文长文，跟起来很累。

**Claude FM 把它们逐篇做成口语化的中文解读**，整理成一档可以随时收听的播客——通勤、健身、做家务的时候听一听，用碎片时间把最前沿的 AI 进展听懂。我把 Anthropic 这几年（2021 至今）的内容系统梳理了一遍，**共 448 集，按发表时间排成一条 AI 技术演进的时间线**，并且每周日持续更新。

## 🎧 收听

> **在小宇宙收听** 👉 **[点这里听 Claude FM](https://www.xiaoyuzhoufm.com/podcast/6a37f2bcdd580cf9cf4bf121)**

或者，用**任意播客 App**（Apple Podcasts、Pocket Casts 等）粘贴下面的 RSS 地址订阅：

```
https://fm.yccode.xyz/feed.xml
```

## 📖 也可以直接读文字版

不方便听？每一集的**中文解读全文**都在这个仓库里，点开即读（开头都会注明文章发表时间）：

- 🛠️ [构建高效 AI 智能体](content/anthropic/engineering/scripts/2024-12-19-Building%20Effective%20AI%20Agents.md) · *Building Effective AI Agents*
- 🔬 [叠加态的玩具模型](content/anthropic/research/scripts/2022-09-14-Toy%20Models%20of%20Superposition.md) · *Toy Models of Superposition*
- 🔬 [宪法式 AI](content/anthropic/research/scripts/2022-12-15-Constitutional%20AI%20-%20Harmlessness%20from%20AI%20Feedback.md) · *Constitutional AI*
- 📝 [Agent Skills 发布](content/claude/blog/scripts/2025-10-16-Introducing%20Agent%20Skills.md) · *Introducing Agent Skills*
- 📝 [Prompt 工程最佳实践](content/claude/blog/scripts/2025-11-10-Prompt%20engineering%20best%20practices.md)
- 📰 [Anthropic 一周快讯示例](content/anthropic/news/scripts/2026-06-14-Anthropic一周快讯.md)

📋 **完整 448 集目录(可点开每集文字稿)** 👉 **[CATALOG.md](CATALOG.md)**

全部解读稿也在 [`content/`](content/) 下按来源分目录存放（`scripts/` 是中文解读，`articles/` 是英文原文）。

## 📚 内容概览

| 来源 | 集数 | 内容 |
|---|:---:|---|
| 🛠️ Engineering | 25 | 工程实践深度解读（智能体、Claude Code、评测…） |
| 🔬 Research | 142 | 研究论文深度解读（可解释性、对齐、安全…） |
| 📝 Blog | 171 | 官方博客深度解读（产品、技能、最佳实践…） |
| 📰 News 周报 | 115 | 「一周快讯」合集，速览每周官方动态 |
| | **448 集** | 覆盖 2021 至今，每周日更新 |

前四个源逐篇做约 25 分钟的深度解读；news 时效性强、多为公告，按周聚合成几分钟的「一周快讯」。

## 🔄 更新节奏（维护者备忘）

每周日跑一条命令即可完成本周更新：

```bash
uv run claude-fm weekly      # 抓三源新文章并解读 + 把上周 news 打包成「一周快讯」
                             # 同时刷新 RSS(feed.xml) 和本目录(CATALOG.md / README 集数)
```

它会产出本周新增的解读稿与音频；之后把音频和 `feed.xml` 同步到服务器（部署细节见本地私有文档），小宇宙会自动拉到新集。所以本 README 的集数和 [CATALOG.md](CATALOG.md) 每周都会随之更新。

---

<div align="center">

## 关于版权

本项目为个人**非商业**的学习用途整理，**与 Anthropic 无任何官方关联**。<br>
所有原文版权归 [Anthropic](https://www.anthropic.com) 所有；中文解读由 Claude 生成，仅供学习参考，请以英文原文为准。

<sub>用 ❤️ 和 Claude 构建 · 让前沿 AI 知识更易获取</sub>

</div>
