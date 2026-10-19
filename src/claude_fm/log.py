"""结构化日志：每个事件一行 JSON 写到 stderr，供无人值守运行事后查询。

stdout 仍保留面向人的中文进度输出；本模块只补充机器可查询的事件，
每条事件是固定消息 + 若干字段（URL、来源、阶段、耗时、异常栈），
以便在 autorun.log 里按字段过滤、聚合失败。

消息是常量字符串，动态值一律放进字段，不要插进消息本身——
观测工具按消息模板聚类事件，插值会把同一类事件拆成无数模板。
"""

import json
import logging
import sys

_LOGGER_NAME = "claude_fm"

# LogRecord 自带字段，不作为事件字段输出
_RESERVED = frozenset({
    "name", "msg", "args", "levelname", "levelno", "pathname", "filename",
    "module", "exc_info", "exc_text", "stack_info", "lineno", "funcName",
    "created", "msecs", "relativeCreated", "thread", "threadName",
    "processName", "process", "taskName", "message", "asctime",
})


class _JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload: dict = {
            "ts": self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
            "level": record.levelname,
            "event": record.getMessage(),
            "logger": record.name,
        }
        for key, value in record.__dict__.items():
            if key not in _RESERVED:
                payload[key] = value
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False, default=str)


def setup() -> None:
    """给 claude_fm 日志器挂一个 JSON stderr handler；重复调用无副作用。"""
    logger = logging.getLogger(_LOGGER_NAME)
    if logger.handlers:
        return
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(_JsonFormatter())
    logger.addHandler(handler)
    logger.propagate = False


def get_logger(name: str = "") -> logging.Logger:
    return logging.getLogger(f"{_LOGGER_NAME}.{name}" if name else _LOGGER_NAME)
