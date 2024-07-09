# db/database.py

import sqlite3

# Создание соединения с базой данных и создание курсора
conn = sqlite3.connect('db/user.db')
cursor = conn.cursor()

# Создание таблицы пользователей, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER UNIQUE,
    name TEXT,
    category1 TEXT,
    category2 TEXT,
    category3 TEXT,
    expenses1 REAL,
    expenses2 REAL,
    expenses3 REAL
)
''')
conn.commit()

# Функция для получения курсора
def get_cursor():
    return cursor

# Функция для получения соединения
def get_conn():
    return conn
