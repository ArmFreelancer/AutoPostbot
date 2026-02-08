"""Base domain error."""

class DomainError(Exception):
    """Base domain error."""

class GeminiProviderError(DomainError):
    """Gemini provider error."""

class OllamaProviderError(DomainError):
    """Ollama provider error."""
