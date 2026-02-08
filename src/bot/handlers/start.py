"""Start command handler."""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_command(message: Message) -> None:
    await message.answer(
        "Это бот для автоматического постинга в Telegram. "
        "Используется Gemini API для генерации текста."
    )