import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import registration, exchange, tips, finances
from keyboards.default import main_keyboard
import json
import logging

# Загрузка конфигурации из файла config.json
with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

API_TOKEN = config['API_TOKEN']

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs/bot.log'), logging.StreamHandler()]
)

# Создание объекта бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Регистрация хэндлеров
dp.include_router(registration.router)
dp.include_router(exchange.router)
dp.include_router(tips.router)
dp.include_router(finances.router)

# Команда /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я ваш личный финансовый помощник. Выберите одну из опций в меню.", reply_markup=main_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
