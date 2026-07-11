import sys
from pathlib import Path

from loguru import logger

Path("logs").mkdir(exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | {message}",
)

logger.add(
    "logs/polymarket.log",
    rotation="20 MB",
    retention="10 days",
    level="INFO",
)

__all__ = ["logger"]