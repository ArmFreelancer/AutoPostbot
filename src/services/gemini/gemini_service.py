"""Gemini API service."""

from google import genai
from tenacity import retry, stop_after_attempt, wait_exponential

from src.app.config import settings
from src.app.logging import logger
from src.domain.errors.domain_error import GeminiProviderError
from src.services.gemini.prompts import default_prompt


class GeminiService:
    """Gemini API service for post generation."""
    def __init__(self) -> None:
        self.client = genai.Client(api_key=settings.gemini_api_key.get_secret_value())
        self.gemini_model = settings.gemini_model

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True,
    )
    async def generate_post(self, topic: str | None = None) -> str:
        logger.info(f"Requesting content generation from model: {self.gemini_model}")
        logger.debug(f"Generating post with topic: {topic}")
        try:
            response = await self.client.aio.models.generate_content(
                model=self.gemini_model,
                contents=[default_prompt(topic)],
            )
            if not response.text:
                logger.error("Gemini API returned an empty response or blocked content.")
                raise GeminiProviderError("Empty response from AI provider.")

            generated_content = response.text.strip()
            logger.info("Successfully received generated content from Gemini.")
            return generated_content

        except Exception as error:
            logger.error(f"Failed to generate content with Gemini: {error}")
            raise GeminiProviderError(f"AI generation failed: {error}") from error
