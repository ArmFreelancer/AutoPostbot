import asyncio

from src.app.bootstrap import bootstrap


async def main() -> None:
    bot, dp = await bootstrap()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
