import asyncio
from dotenv import load_dotenv
import os 
from aiogram import Bot, Dispatcher
from aiogram.types import Message 
from aiogram.filters import CommandStart

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
  await message.answer("Привет! Я твой бот")

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())
