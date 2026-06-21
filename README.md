<div align="center">

# Claude FM 📻

**把 Anthropic 的前沿技术内容，做成中文播客，装进你的通勤路上。**

抓取原文 → Claude 中文解读 → 合成语音 → 一键上传小宇宙

![python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/managed%20by-uv-DE5FE9)
![TTS](https://img.shields.io/badge/TTS-edge--tts-0078D4)
![episodes](https://img.shields.io/badge/已产出-453%20集-1DB954)
![license](https://img.shields.io/badge/内容版权-归%20Anthropic-lightgrey)

</div>

---

## 这是什么

[Anthropic](https://www.anthropic.com) 在 engineering、research、news 和 [claude.com/blog](https://claude.com/blog) 上持续发布大量高质量的 AI 技术内容——智能体设计、可解释性研究、模型发布、安全框架……但大多是英文长文，很难跟上。

**Claude FM 是一条全自动流水线**，把这些文章抓下来，让 Claude 逐篇做成口语化的**中文技术解读**，再用 TTS 合成音频，产出可直接上传到[小宇宙](https://www.xiaoyuzhoufm.com)的成品。通勤路上听一听，就能积累最前沿的 AI 知识。

> 💡 不想听音频？仓库里每一集的**中文文字稿**都在，可以直接当文章读 —— 见下方[「📖 在线阅读文字版」](#-在线阅读文字版)。

### 内容概览

| 数据源 | 集数 | 形式 | 覆盖时间 |
|---|:---:|---|---|
| 🛠️ **engineering** | 25 | 单篇深度解读（约 25 分钟） | 2024.09 – 2026.05 |
| 🔬 **research** | 142 | 单篇深度解读（约 25 分钟） | 2021.12 – 2026.06 |
| 📝 **claude.com/blog** | 171 | 单篇深度解读（约 25 分钟） | 2023.08 – 2026.06 |
| 📰 **news** | 115 | 按周「一周快讯」合集 | 2021.05 – 至今 |
| | **453 集** | | |

engineering / research / blog 是技术干货，逐篇做 25 分钟的深度解读；news 多为公告、时效性强，按**自然周**聚合成「一周快讯」，轻重分明、几分钟一集。

---

## 📖 在线阅读文字版

每一集的中文解读稿都在仓库里，GitHub 直接可读（开头会注明文章发表时间，便于判断时效）：

```
content/<来源>/scripts/<发表日期-标题>.md
```

随便点几集尝尝：

- 🛠️ [构建高效 AI 智能体](content/anthropic/engineering/scripts/2024-12-19-Building%20Effective%20AI%20Agents.md) · *Building Effective AI Agents*
- 🔬 [叠加态的玩具模型](content/anthropic/research/scripts/2022-09-14-Toy%20Models%20of%20Superposition.md) · *Toy Models of Superposition*
- 🔬 [宪法式 AI](content/anthropic/research/scripts/2022-12-15-Constitutional%20AI%20-%20Harmlessness%20from%20AI%20Feedback.md) · *Constitutional AI*
- 📝 [Agent Skills 发布](content/claude/blog/scripts/2025-10-16-Introducing%20Agent%20Skills.md) · *Introducing Agent Skills*
- 📝 [Prompt 工程最佳实践](content/claude/blog/scripts/2025-11-10-Prompt%20engineering%20best%20practices.md)
- 📰 [Anthropic 一周快讯示例](content/anthropic/news/scripts/2026-06-14-Anthropic一周快讯.md)

> 文字稿是为「听」优化的口语体（数字、术语都按口播习惯写），读起来像一篇讲稿。每篇旁边还有英文**原文**（`articles/`）和**节目简介**（`episodes/`）。

---

## ⚙️ 工作原理

```
        ┌─ anthropic.com/engineering ─┐
        ├─ anthropic.com/research ────┤   ①发现+抓取      ②Claude 解读        ③合成语音        ④打包
        ├─ anthropic.com/news ────────┤   ──────────►  原文.md  ──────────►  解读稿.md  ──────►  音频.mp3  ──────►  上传包.md
        └─ claude.com/blog ───────────┘   httpx+trafilatura   claude -p 无头模式    edge-tts        标题+shownotes
```

- **解读**走本机已登录的 **Claude Code CLI**（`claude -p` 无头模式），不需要 API key、不花 API 费用。
- **TTS** 用免费的 **edge-tts**，多个中文男声轮换，避免审美疲劳。
- 全流程**幂等**：中途撞限额 / 断网 / 关机，重跑即可，已完成的自动跳过。
- 撞 Claude 订阅**会话限额**会自动等重置再续；撞**每周限额**会停下提示换号。

---

## 🗓️ 每周更新

新内容每周更一次。**每周日跑这一条命令**，就会：增量解读三个深度源的新文章 + 把上一周（周日–周六）的 news 打包成一期周报：

```bash
uv run claude-fm weekly
```

它会自动发现新文章、抓取、解读、合成、产出上传包；连「某条 news 延迟几天才收录、落进上周」这种情况也会自动补做该周。跑完后，**待上传的成品**都在各来源的 `episodes/` 目录里。

> ⏰ 想完全自动化？可以把这条命令配进本机 `cron` / `launchd` 定时任务。注意：**上传小宇宙这一步仍需手动**（平台没有开放上传 API）。

### 上传到小宇宙

1. 打开[小宇宙创作者后台](https://podcaster.xiaoyuzhoufm.com)
2. 上传对应 `audio/` 目录里的 `.mp3`
3. 标题与 shownotes 从同名的 `episodes/*.md` 里复制粘贴

---

## 🧰 全部命令

```bash
uv run claude-fm weekly        # ★ 每周更新：三源增量 + news 上周周报
uv run claude-fm discover      # 看各源有多少新文章（只读，不处理）
uv run claude-fm status        # 查看各集处理进度

# 按需 / 批量
uv run claude-fm autorun --source research   # 无人值守跑某个深度源（撞限额自动续）
uv run claude-fm run --url <文章URL>          # 只跑指定一篇
uv run claude-fm news                         # 只跑 news 周报
uv run claude-fm voices                       # 生成音色试听样品
```

---

## 📂 目录结构

代码与内容彻底分离；内容按来源分目录，文件名统一为 `发表日期-标题`：

```
claude-fm/
├── src/claude_fm/         # 流水线代码
│   ├── sources.py         #   文章发现（sitemap / 列表页分页）
│   ├── fetch.py           #   抓正文 + 解析发表日期
│   ├── interpret.py       #   调 claude -p 生成深度解读
│   ├── digest.py          #   news 按周聚合成「一周快讯」
│   ├── tts.py             #   edge-tts 合成
│   └── cli.py             #   命令行入口
├── prompts/
│   ├── interpret.md       #   深度解读 prompt（可调风格/篇幅）
│   └── news_digest.md     #   news 周报 prompt
└── content/               # 全部产出（音频不入 git，见下）
    ├── anthropic/
    │   ├── engineering/{articles,scripts,audio,episodes}/
    │   ├── research/{articles,scripts,audio,episodes}/
    │   └── news/{articles,scripts,audio,episodes}/
    └── claude/blog/{articles,scripts,audio,episodes}/
```

每篇文章/每期节目有四件套：`articles/` 英文原文 · `scripts/` 中文解读稿 · `audio/` 音频 · `episodes/` 上传包。

> ⚠️ **音频不入仓库**：成品 `.mp3` 共约 1.7 GB，已通过 `.gitignore` 排除；仓库里只保留**文字内容**。需要音频时本地跑流水线由解读稿合成，或上小宇宙收听。

---

## 🔧 配置

集中在 [`src/claude_fm/config.py`](src/claude_fm/config.py)：

| 项 | 说明 |
|---|---|
| `CLAUDE_MODEL` | 解读模型，默认 `claude-sonnet-4-6`（走订阅，无需 API key） |
| `TTS_VOICES` | 轮换音色列表（默认两个中文男声）；`claude-fm voices` 可试听候选 |
| `TTS_RATE` | 语速微调，如 `"+10%"` |
| `SOURCES` | 数据源；加新源在此扩展 |

解读风格 / 篇幅在 [`prompts/`](prompts/) 里改：[interpret.md](prompts/interpret.md)（深度解读，目标 ~7000 汉字）、[news_digest.md](prompts/news_digest.md)（周报，弹性篇幅）。

---

## 🚀 运行环境

- **Python ≥ 3.11**，依赖用 [uv](https://docs.astral.sh/uv/) 管理：`uv sync` 安装
- 本机已安装并**登录 Claude Code CLI**（解读靠它跑）
- 联网（抓取原文 + edge-tts 在线合成）

```bash
git clone <repo> && cd claude-fm
uv sync
uv run claude-fm status     # 看看现有进度
```

---

## 📜 关于版权

本项目仅做**个人学习用途**的二次解读与转述。所有原文版权归 [Anthropic](https://www.anthropic.com) 所有；中文解读由 Claude 生成，仅供学习参考，请以英文原文为准。

<div align="center">
<sub>用 ❤️ 和 Claude 构建 · 让前沿 AI 知识更易获取</sub>
</div>
