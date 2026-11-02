# YanaAi

Telegram-бот, который генерирует изображения по текстовому описанию.
Запрос на русском автоматически переводится на английский, затем
отправляется в модель FLUX.1 schnell (Cloudflare Workers AI).

## Стек технологий

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-3.x-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![Cloudflare Workers AI](https://img.shields.io/badge/Cloudflare_Workers_AI-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![FLUX.1 schnell](https://img.shields.io/badge/FLUX.1-schnell-000000?style=for-the-badge)
![googletrans](https://img.shields.io/badge/googletrans-4.0.0--rc1-4285F4?style=for-the-badge&logo=google&logoColor=white)
![aiohttp](https://img.shields.io/badge/aiohttp-2C5BB4?style=for-the-badge&logo=aiohttp&logoColor=white)

## Запуск

1. Клонируйте репозиторий и создайте виртуальное окружение:

```PowerShell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Создайте файл `.env` в корне проекта (на основе `.env.example`):

```.env
TOKEN=токен_бота_от_BotFather
CLOUDFLARE_ACCOUNT_ID=ваш_account_id
CLOUDFLARE_API_TOKEN=ваш_api_токен
```

3. Запустите бота:

```PowerShell
python main.py
```

## Ограничения
- Бесплатная квота Workers AI ограничена и сбрасывается раз в сутки.
- Перевод через googletrans, однако это неофициальная библиотека и может работать нестабильно.
- Условия использования модели смотрите в документации Cloudflare и Black Forest Labs.

## Планы
- Возможность редактирования фотографии.
- Выбор между несколькими моделями в том числе и платных.
- Отправка в виде файла (без сжатия Telegram).
- Профили пользователей.

Следите за обновлениями: [@Cameon_projects](https://t.me/Cameon_projects)