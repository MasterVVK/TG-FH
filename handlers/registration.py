# handlers/registration.py

import logging
from aiogram import Router, F
from aiogram.types import Message
from db.database import get_cursor, get_conn  # Импорт функций для получения курсора и соединения

router = Router()


@router.message(F.text == "Регистрация в телеграм боте")
async def registration(message: Message):
    telegram_id = message.from_user.id
    name = message.from_user.full_name
    cursor = get_cursor()
    conn = get_conn()

    cursor.execute('''SELECT * FROM users WHERE telegram_id = ?''', (telegram_id,))
    user = cursor.fetchone()
    logging.debug(f"Результат запроса SELECT: {user}")
    if user:
        await message.answer("Вы уже зарегистрированы!")
    else:
        cursor.execute('''INSERT INTO users (telegram_id, name) VALUES (?, ?)''', (telegram_id, name))
        conn.commit()
        await message.answer("Вы успешно зарегистрированы!")
