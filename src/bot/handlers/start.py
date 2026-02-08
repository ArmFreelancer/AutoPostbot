"""Start command handler."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def start_command(message: Message) -> None:
    await message.answer(
        "Это бот для автоматического постинга в Telegram. "
        "Используется Gemini API для генерации текста."
    )
