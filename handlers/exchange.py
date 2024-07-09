import aiohttp
import json
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

# Загрузка конфигурации из файла config.json
with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

EXCHANGE_API_URL = f"https://v6.exchangerate-api.com/v6/{config['EXCHANGE_API_KEY']}/latest/USD"

@router.message(Command("exchange"))
async def exchange_rates(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(EXCHANGE_API_URL) as response:
            data = await response.json()
            if response.status == 200:
                usd_to_rub = data['conversion_rates']['RUB']
                eur_to_usd = data['conversion_rates']['EUR']
                euro_to_rub = eur_to_usd * usd_to_rub
                await message.answer(f"1 USD - {usd_to_rub:.2f} RUB\n1 EUR - {euro_to_rub:.2f} RUB")
            else:
                await message.answer("Не удалось получить данные о курсе валют. Попробуйте позже.")
