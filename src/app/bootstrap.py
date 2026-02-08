"""Application bootstrap and initialization."""

from aiogram import Bot, Dispatcher

from src.app.config import settings
from src.bot.router import router as bot_router


async def bootstrap() -> tuple[Bot, Dispatcher]:
    """
    Initialize all application components.
    """
    bot = Bot(token=settings.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(bot_router)
    return bot, dp
