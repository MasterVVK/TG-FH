from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.database import get_cursor, get_conn

router = Router()


class FinancesForm(StatesGroup):
    category1 = State()
    expenses1 = State()
    category2 = State()
    expenses2 = State()
    category3 = State()
    expenses3 = State()


@router.message(F.text == "Личные финансы")
async def finances(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    cursor = get_cursor()
    cursor.execute('''SELECT * FROM users WHERE telegram_id = ?''', (telegram_id,))
    user = cursor.fetchone()

    if not user:
        await message.reply(
            "Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь, отправив сообщение 'Регистрация в телеграм боте'.")
        return

    await state.set_state(FinancesForm.category1)
    await message.reply("Введите первую категорию расходов:")


@router.message(FinancesForm.category1)
async def finances_category1(message: Message, state: FSMContext):
    await state.update_data(category1=message.text)
    await state.set_state(FinancesForm.expenses1)
    await message.reply(f"Введите расходы для категории '{message.text}':")


@router.message(FinancesForm.expenses1)
async def finances_expenses1(message: Message, state: FSMContext):
    try:
        expenses1 = float(message.text)
    except ValueError:
        await message.reply("Пожалуйста, введите числовое значение для расходов.")
        return

    await state.update_data(expenses1=expenses1)
    await state.set_state(FinancesForm.category2)
    await message.reply("Введите вторую категорию расходов:")


@router.message(FinancesForm.category2)
async def finances_category2(message: Message, state: FSMContext):
    await state.update_data(category2=message.text)
    await state.set_state(FinancesForm.expenses2)
    await message.reply(f"Введите расходы для категории '{message.text}':")


@router.message(FinancesForm.expenses2)
async def finances_expenses2(message: Message, state: FSMContext):
    try:
        expenses2 = float(message.text)
    except ValueError:
        await message.reply("Пожалуйста, введите числовое значение для расходов.")
        return

    await state.update_data(expenses2=expenses2)
    await state.set_state(FinancesForm.category3)
    await message.reply("Введите третью категорию расходов:")


@router.message(FinancesForm.category3)
async def finances_category3(message: Message, state: FSMContext):
    await state.update_data(category3=message.text)
    await state.set_state(FinancesForm.expenses3)
    await message.reply(f"Введите расходы для категории '{message.text}':")


@router.message(FinancesForm.expenses3)
async def finances_expenses3(message: Message, state: FSMContext):
    try:
        expenses3 = float(message.text)
    except ValueError:
        await message.reply("Пожалуйста, введите числовое значение для расходов.")
        return

    await state.update_data(expenses3=expenses3)
    data = await state.get_data()
    telegram_id = message.from_user.id
    cursor = get_cursor()
    conn = get_conn()
    cursor.execute('''
        UPDATE users SET category1 = ?, expenses1 = ?, category2 = ?, expenses2 = ?, category3 = ?, expenses3 = ? WHERE telegram_id = ?
    ''', (
    data['category1'], data['expenses1'], data['category2'], data['expenses2'], data['category3'], data['expenses3'],
    telegram_id))
    conn.commit()
    await state.clear()
    await message.answer("Категории и расходы сохранены!")

    result_message = (
        f"Ваши расходы:\n"
        f"Категория 1: {data['category1']} - {data['expenses1']} руб.\n"
        f"Категория 2: {data['category2']} - {data['expenses2']} руб.\n"
        f"Категория 3: {data['category3']} - {data['expenses3']} руб."
    )
    await message.answer(result_message)
