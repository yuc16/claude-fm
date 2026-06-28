"""生成每集上传包：content/episodes/<slug>.md，手动上传小宇宙时直接复制。"""

from . import config


def write_episode(
    slug: str,
    episode_no: int,
    episode_title: str,
    shownotes: str,
    article_meta: dict,
    duration_sec: float,
) -> None:
    source = article_meta.get("source", "")
    minutes, seconds = divmod(int(duration_sec), 60)
    title = f"EP{episode_no} | {episode_title}"
    mp3 = config.audio_path(source, slug)
    body = f"""# {title}

- 音频文件：`{mp3}`
- 时长：{minutes} 分 {seconds:02d} 秒

## Shownotes（复制到小宇宙）

{shownotes}

---

原文：{article_meta.get('title', '')}
链接：{article_meta.get('url', '')}
发表时间：{article_meta.get('published', '未知')}
本期解读由模型（{config.interpret_model()}）生成，音频由 edge-tts 合成。
"""
    out = config.episode_path(source, slug)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
