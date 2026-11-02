import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BufferedInputFile
from dotenv import load_dotenv

from Ai import generate_image
from translater import translate_text



load_dotenv()

Token = os.getenv("TOKEN")  

bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("image"))
async def handle_image_command(message: Message):

    try:
        prompt = await translate_text(message.text.removeprefix("/image").strip())
    except Exception as e:
        await message.answer(f"Ошибка при переводе текста: {str(e)}")
        prompt = message.text.removeprefix("/image").strip()

    if not prompt:
        await message.answer("Напишите описание: /image (описание)")
        return

    status = await message.answer("Генерирую изображение...")
    try:
        image_bytes = await generate_image(prompt)
    except Exception as e:
        if "NSFW" in str(e):
            await status.edit_text("Ошибка: Запрос содержит NSFW контент. Пожалуйста, попробуйте другой запрос.")
        else:
            await status.edit_text(f"Ошибка при генерации изображения: {str(e)}")

        return

    photo = BufferedInputFile(image_bytes, filename="res.png")
    await status.delete()
    await status.answer_photo(photo=photo)

@dp.message(CommandStart())
async def handle_message(message):
    await message.answer("Hello! I am your bot.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())