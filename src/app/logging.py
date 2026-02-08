import logging
import sys
from pathlib import Path
from types import FrameType

from loguru import logger

from src.app.config import settings

__all__ = ["logger", "setup_logging"]

_logging_configured = False


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame: FrameType | None = logging.currentframe()
        depth = 2

        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logging() -> None:
    global _logging_configured
    if _logging_configured:
        return
    _logging_configured = True

    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(settings.log_level.upper())

    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger.remove()

    if settings.debug:
        logger.add(
            sys.stderr,
            level=settings.log_level.upper(),
            format=settings.log_format,
            colorize=True,
        )

    log_path = Path(settings.log_path)
    log_path.mkdir(parents=True, exist_ok=True)

    logger.add(
        str(log_path / "autopostbot.log"),
        rotation=settings.log_rotate,
        retention=settings.log_backup_count,
        compression="zip",
        level=settings.log_level.upper(),
        format=settings.log_format,
        encoding=settings.log_encoding,
        enqueue=True,
        backtrace=settings.debug,
        diagnose=settings.debug,
    )

    logger.info("Logging configured successfully.")
