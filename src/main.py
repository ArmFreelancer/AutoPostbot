import asyncio

from aiogram import Bot, Dispatcher

from src.app.config import settings
from src.bot.router import router as bot_router

bot = Bot(token=settings.telegram_bot_token.get_secret_value())
dp = Dispatcher()
dp.include_router(bot_router)


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
