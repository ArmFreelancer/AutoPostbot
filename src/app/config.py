from typing import Any

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # --- Gemini ---
    gemini_api_key: SecretStr = Field(alias="GEMINI_API_KEY")
    gemini_model: str = Field(alias="GEMINI_MODEL", default="gemini-3-pro-preview")

    # --- Telegram ---
    bot_token: SecretStr = Field(alias="BOT_TOKEN")

    # --- Database ---
    database_url: str = Field(alias="DATABASE_URL")

    # --- Logging ---
    log_level: str = Field(alias="LOG_LEVEL", default="INFO")
    log_dir: str = Field(alias="LOG_DIR", default="logs")
    log_max_bytes: int = Field(alias="LOG_MAX_BYTES", default=10485760)
    log_backup_count: int = Field(alias="LOG_BACKUP_COUNT", default=5)
    log_format: str = Field(alias="LOG_FORMAT", default="{level} | {message}")
    log_to_stdout: bool = Field(alias="LOG_TO_STDOUT", default=False)


class _SettingsInstance(Settings):
    """Subclass so that settings = _SettingsInstance() has no required args for strict checkers."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


settings = _SettingsInstance()
