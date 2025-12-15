import asyncio
from dotenv import load_dotenv
import os 
from aiogram import Bot, Dispatcher
from aiogram.types import Message 
from aiogram.filters import CommandStart

load_dotenv()

TOKEN = os.getenv("8538453663:AAFWKUWd07diMajjLUGfgfFn6cSwl4xGUUA")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
  await message.answer("Привет! Я твой бот)

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())
