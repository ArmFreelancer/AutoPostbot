"""Generation handler."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.app.config import settings
from src.domain.errors.domain_error import GeminiProviderError, OllamaProviderError
from src.services.gemini.gemini_service import GeminiService
from src.services.ollama.ollama_service import OllamaService

router = Router()

QUOTA_MESSAGE = (
    "Квота API исчерпана. Попробуйте позже или проверьте лимиты в Google AI Studio."
)
OLLAMA_ERROR_MESSAGE = (
    "Ошибка Ollama. Проверьте, что Ollama запущена (localhost:11434) и модель загружена."
)


def _get_gen_service() -> GeminiService | OllamaService:
    if settings.ai_provider.strip().lower() == "gemini":
        return GeminiService()
    return OllamaService()

GEN_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пропустить", callback_data="gen_skip")],
        [InlineKeyboardButton(text="Написать тему", callback_data="gen_write_topic")],
    ]
)


@router.message(Command("gen"))
async def cmd_gen(message: Message) -> None:
    text = message.text or ""
    args = text.split(maxsplit=1)
    topic = args[1].strip() if len(args) > 1 else None

    if topic is not None:
        try:
            service = _get_gen_service()
            post = await service.generate_post(topic)
            await message.answer(post)
        except GeminiProviderError:
            await message.answer(QUOTA_MESSAGE)
        except OllamaProviderError:
            await message.answer(OLLAMA_ERROR_MESSAGE)
        return

    await message.answer("Выберите действие:", reply_markup=GEN_KEYBOARD)


@router.callback_query(lambda c: c.data == "gen_skip")
async def gen_skip(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is None:
        return
    try:
        service = _get_gen_service()
        post = await service.generate_post(None)
        await callback.message.answer(post)
    except GeminiProviderError:
        await callback.message.answer(QUOTA_MESSAGE)
    except OllamaProviderError:
        await callback.message.answer(OLLAMA_ERROR_MESSAGE)


@router.callback_query(lambda c: c.data == "gen_write_topic")
async def gen_write_topic(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is None:
        return
    await callback.message.answer("Отправьте тему поста командой: /gen ваша тема")
