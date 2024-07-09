import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
import json

from handlers import registration, exchange, tips, finances

# Загрузка конфигурации из файла config.json
with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

TOKEN = config['API_TOKEN']

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='logs/bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Регистрация хэндлеров
dp.include_router(registration.router)
dp.include_router(exchange.router)
dp.include_router(tips.router)
dp.include_router(finances.router)

# Команда /start
@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Привет! Я ваш личный финансовый помощник. Выберите одну из опций в меню.", reply_markup=registration.keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
