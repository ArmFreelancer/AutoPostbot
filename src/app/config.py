from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # --- Gemini ---
    gemini_api_key: str = Field(alias="GEMINI_API_KEY", default="")
    gemini_model: str = Field(alias="GEMINI_MODEL", default="gemini-3-pro-preview")

    # --- Telegram ---
    telegram_bot_token: str = Field(alias="TELEGRAM_BOT_TOKEN", default="")

    # --- Database ---
    sqlite_path: str = Field(alias="SQLITE_PATH", default="db/autopostbot.sqlite3")

    
settings = Settings()
