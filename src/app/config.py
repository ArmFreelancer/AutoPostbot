from typing import Any

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # --- App ---
    env: str = Field(alias="ENV", default="dev")
    run_in_docker: bool = Field(alias="RUN_IN_DOCKER", default=False)
    debug: bool = Field(alias="DEBUG", default=False)

    # --- Gemini ---
    gemini_api_key: SecretStr = Field(alias="GEMINI_API_KEY")
    gemini_model: str = Field(alias="GEMINI_MODEL", default="gemini-3-pro-preview")

    # --- Telegram ---
    bot_token: SecretStr = Field(alias="BOT_TOKEN")

    # --- Database ---
    database_url: str = Field(alias="DATABASE_URL")

    # --- Logging ---
    log_level: str = Field(alias="LOG_LEVEL", default="info")
    log_format: str = Field(
        alias="LOG_FORMAT",
        default=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
    )
    log_date_format: str = Field(alias="LOG_DATE_FORMAT", default="%Y-%m-%d %H:%M:%S")
    log_path: str = Field(alias="LOG_PATH", default="logs")
    log_max_bytes: int = Field(alias="LOG_MAX_BYTES", default=10485760)
    log_backup_count: int = Field(alias="LOG_BACKUP_COUNT", default=5)
    log_encoding: str = Field(alias="LOG_ENCODING", default="utf-8")
    log_mode: str = Field(alias="LOG_MODE", default="w")
    log_rotate: str = Field(alias="LOG_ROTATE", default="daily")
    log_to_stdout: bool = Field(alias="LOG_TO_STDOUT", default=True)


class _SettingsInstance(Settings):
    """Subclass so that settings = _SettingsInstance() has no required args for strict checkers."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


settings = _SettingsInstance()
