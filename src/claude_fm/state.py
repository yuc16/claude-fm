"""content/state.json 读写：记录每篇文章的流水线进度，保证幂等重跑。"""

import json
from typing import Any

from . import config

# state 结构：
# {
#   "next_episode": 1,
#   "articles": {
#     "<url>": {
#       "slug": "...", "source": "engineering", "title": "...",
#       "published": "2024-12-19", "episode": 3, "duration_sec": 1502.3,
#       "stages": {"fetched": true, "interpreted": true, "synthesized": true, "packaged": true}
#     }
#   }
# }


def load() -> dict[str, Any]:
    if config.STATE_FILE.exists():
        return json.loads(config.STATE_FILE.read_text(encoding="utf-8"))
    return {"next_episode": 1, "articles": {}}


def save(state: dict[str, Any]) -> None:
    config.CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    config.STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def get_article(state: dict[str, Any], url: str) -> dict[str, Any]:
    return state["articles"].setdefault(url, {"stages": {}})


def assign_episode(state: dict[str, Any], url: str) -> int:
    art = get_article(state, url)
    if "episode" not in art:
        art["episode"] = state["next_episode"]
        state["next_episode"] += 1
    return art["episode"]
