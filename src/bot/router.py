"""Bot router and registration of handlers."""

from aiogram import Router

from src.bot.handlers import start

router = Router()
router.include_router(start.router)
