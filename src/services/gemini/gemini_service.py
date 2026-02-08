"""Gemini API service."""

from src.app.config import settings


class GeminiService:
    def __init__(self) -> None:
        self.gemini_api_key = settings.gemini_api_key.get_secret_value()
        self.gemini_model = settings.gemini_model

    async def generate_text(self, prompt: str) -> None:
        ...
