import sys

from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    enqueue=True,
)

__all__ = ["logger"]