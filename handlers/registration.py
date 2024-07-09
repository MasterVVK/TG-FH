import sqlite3
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from db.database import get_cursor, get_conn

router = Router()

# Создание клавиатуры
button_registr = KeyboardButton(text="Регистрация в телеграм-боте")
button_exchange_rates = KeyboardButton(text="Курс валют")
button_tips = KeyboardButton(text="Советы по экономии")
button_finances = KeyboardButton(text="Личные финансы")

keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_registr, button_exchange_rates],
    [button_tips, button_finances]
], resize_keyboard=True)

@router.message(F.text == "Регистрация в телеграм-боте")
async def registration(message: Message):
    telegram_id = message.from_user.id
    name = message.from_user.full_name

    cursor = get_cursor()
    conn = get_conn()

    cursor.execute('''SELECT * FROM users WHERE telegram_id = ?''', (telegram_id,))
    user = cursor.fetchone()
    if user:
        await message.answer("Вы уже зарегистрированы!")
    else:
        cursor.execute('''INSERT INTO users (telegram_id, name) VALUES (?, ?)''', (telegram_id, name))
        conn.commit()
        await message.answer("Вы успешно зарегистрированы!")
