# AutoPostbot

Telegram-бот для автоматизации постинга: помогает готовить и публиковать посты в каналы. Тексты генерируются через **Gemini API**, настройки и черновики хранятся в **SQLite**.

## Требования

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) — менеджер зависимостей и окружений

## Установка

Клонируй репозиторий и установи зависимости через uv:

```bash
git clone https://github.com/ArmFreelancer/AutoPostbot.git
cd AutoPostbot
uv sync
```

Создай файл окружения из примера и заполни переменные:

```bash
cp .env.example .env
```

В `.env` укажи:

| Переменная | Описание |
|------------|----------|
| `TELEGRAM_BOT_TOKEN` | Токен бота от [@BotFather](https://t.me/BotFather) |
| `GEMINI_API_KEY` | API-ключ [Google AI Studio](https://aistudio.google.com/apikey) |
| `GEMINI_MODEL` | Модель Gemini (по умолчанию `gemini-3-pro-preview`) |
| `SQLITE_PATH` | Путь к файлу БД (по умолчанию `db/autopostbot.sqlite3`) |

## Запуск

```bash
uv run python -m src.main
```

Бот запустится в режиме long polling.

## Лицензия

AGPL-3.0 — см. [LICENSE](LICENSE).
