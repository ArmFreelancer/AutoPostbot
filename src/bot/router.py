"""Bot router and registration of handlers."""

from aiogram import Router

from src.bot.handlers import gen, start

router = Router()
router.include_router(start.router)
router.include_router(gen.router)
