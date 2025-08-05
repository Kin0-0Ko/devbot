import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USERS = set(map(int, os.getenv("ALLOWED_USERS", "").split(",")))

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Кнопка "Запустить деплой"
deploy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=" Запустить деплой", callback_data="deploy_now")]
    ]
)

@dp.message(F.text == "/start")
async def start_cmd(message: Message):
    if message.from_user.id not in ALLOWED_USERS:
        await message.answer(" У тебя нет прав.")
        return
    await message.answer("Привет! Нажми кнопку, чтобы запустить деплой:", reply_markup=deploy_btn)

@dp.callback_query(F.data == "deploy_now")
async def deploy_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in ALLOWED_USERS:
        await callback.answer(" Нет прав!", show_alert=True)
        return

    await callback.message.answer(" Запускаю деплой на dev-сервер...")

 
    # from deploy import run_deploy
    # result = run_deploy()
    result = "✅ Деплой успешно завершён (заглушка)"

    await callback.message.answer(f"<pre>{result}</pre>")
    await callback.answer()  

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
