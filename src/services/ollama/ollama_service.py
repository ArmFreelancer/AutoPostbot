"""Ollama API service for local post generation."""

import httpx

from src.app.config import settings
from src.app.logging import logger
from src.domain.errors.domain_error import OllamaProviderError
from src.services.gemini.prompts import default_prompt


class OllamaService:
    """Ollama service for post generation (local, no API key)."""

    def __init__(self) -> None:
        self.base_url = settings.ollama_url.rstrip("/")
        self.model = settings.ollama_model

    async def generate_post(self, topic: str | None = None) -> str:
        logger.info(f"Requesting content generation from Ollama model: {self.model}")
        logger.debug(f"Generating post with topic: {topic}")
        prompt = default_prompt(topic)
        url = f"{self.base_url}/api/generate"
        payload = {"model": self.model, "prompt": prompt, "stream": False}

        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
            data = response.json()
            text = data.get("response")
            if not text or not str(text).strip():
                logger.error("Ollama returned an empty response.")
                raise OllamaProviderError("Empty response from Ollama.")
            generated: str = str(text).strip()
            logger.info("Successfully received generated content from Ollama.")
            return generated
        except httpx.HTTPError as error:
            logger.error(f"Failed to generate content with Ollama: {error}")
            raise OllamaProviderError(f"Ollama request failed: {error}") from error
