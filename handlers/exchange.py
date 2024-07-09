import aiohttp
from aiogram import Router, F
from aiogram.types import Message
import json
import logging

router = Router()

# Загрузка конфигурации из файла config.json
with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

EXCHANGE_API_KEY = config['EXCHANGE_API_KEY']

@router.message(F.text == "Курс валют")
async def exchange_rates(message: Message):
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD"
    logging.info(f"Отправка запроса к API курса валют: {url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                logging.info(f"Получен ответ от API курса валют: статус {response.status}, URL запроса {response.url}")
                if response.status == 200:
                    data = await response.json()
                    logging.info(f"Ответ от exchangerate-ap: {data}")
                    usd_to_rub = data['conversion_rates']['RUB']
                    eur_to_usd = data['conversion_rates']['EUR']
                    euro_to_rub = eur_to_usd * usd_to_rub

                    await message.answer(f"1 USD - {usd_to_rub:.2f} RUB\n1 EUR - {euro_to_rub:.2f} RUB")
                else:
                    logging.error(f"Ошибка получения данных о курсе валют: {response.status} - {await response.text()}")
                    await message.answer("Не удалось получить данные о курсе валют!")
    except Exception as e:
        logging.error(f"Произошла ошибка при обращении к API курса валют: {e}")
        await message.answer("Произошла ошибка при получении данных о курсе валют.")
