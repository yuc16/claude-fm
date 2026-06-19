# Claude FM 📻

把 Anthropic 的技术博客做成约 25 分钟一期的中文播客：抓取原文 → Claude 生成口语化中文解读稿 → edge-tts 合成音频 → 产出小宇宙上传包。通勤路上积累最前沿的 AI 知识。

## 数据源

| 源 | 发现方式 |
|---|---|
| anthropic.com/engineering | sitemap |
| anthropic.com/research | sitemap |
| anthropic.com/news | sitemap |
| claude.com/blog | 列表页解析 |

加新源：编辑 [src/claude_fm/config.py](src/claude_fm/config.py) 的 `SOURCES`。

## 使用

```bash
# 看各源有多少新文章
uv run claude-fm discover

# 日常增量更新：有新文章就全流程跑完（抓取→解读→TTS→上传包）
uv run claude-fm run

# 只跑某个源、限制篇数（批量回填用）
uv run claude-fm run --source engineering --limit 5

# 只跑指定一篇
uv run claude-fm run --url https://www.anthropic.com/engineering/building-effective-agents

# 查看进度
uv run claude-fm status

# 生成音色试听样品
uv run claude-fm voices
```

所有阶段幂等：中途失败直接重跑 `run`，已完成的阶段自动跳过。

## 产出物（content/ 目录，与代码分离）

按数据源分目录，文件名统一为 `发表日期-文章完整标题`：

```
content/
├── anthropic/
│   ├── engineering/
│   │   ├── articles/2024-12-19-Building Effective AI Agents.md   # 英文原文
│   │   ├── scripts/...   # 中文解读稿（开头报出文章发表时间）
│   │   ├── audio/...     # 成品音频 mp3，约 25 分钟
│   │   └── episodes/...  # 小宇宙上传包：集标题 + shownotes + 音频路径
│   ├── research/         # 同上四个子目录
│   └── news/
├── claude/
│   └── blog/
├── samples/              # 音色试听样品
└── state.json            # 流水线状态
```

## 上传小宇宙

1. 打开小宇宙创作者中心（podcaster.xiaoyuzhoufm.com）
2. 上传对应源目录下 `audio/` 里的 mp3
3. 标题和 shownotes 从同名的 `episodes/*.md` 复制

## 配置（src/claude_fm/config.py）

- `TTS_VOICE`：音色。先 `claude-fm voices` 生成样品试听再选
- `TTS_RATE`：语速微调（如 `"+10%"`）
- `CLAUDE_MODEL`：解读模型，默认 `claude-sonnet-4-6`（走 Claude 订阅的 `claude -p` 无头模式，不需要 API key）
- 解读风格 / 时长：改 [prompts/interpret.md](prompts/interpret.md)（字数目标 6200–7200 汉字 ≈ 25 分钟）

## 依赖

Python ≥3.11，[uv](https://docs.astral.sh/uv/) 管理（`uv add <pkg>` 加依赖），需要本机已登录 Claude Code CLI。
