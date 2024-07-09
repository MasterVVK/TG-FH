import random
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

TIPS = [
    "Совет 1: Ведите бюджет и следите за своими расходами.",
    "Совет 2: Откладывайте часть доходов на сбережения.",
    "Совет 3: Покупайте товары по скидкам и распродажам."
]

@router.message(Command("tips"))
async def send_tips(message: Message):
    tip = random.choice(TIPS)
    await message.answer(tip)
