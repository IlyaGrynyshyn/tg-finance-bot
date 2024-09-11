from aiogram import types, Router
from aiogram.filters import Command
from infrastructure.database.db import DataBase

db = DataBase()
list_expenses_router = Router()


@list_expenses_router.message(Command(commands=["expenses"]))
async def list_expenses(message: types.Message):
    last_expenses = db.last_expenses(message.from_user.id)
    if not last_expenses:
        await message.answer("Росходів ще не має")
    last_expenses_rows = [
        f"{expense[2]} грн в категорії  {expense[3]} — натисни "
        f"/del{expense[0]} для видалення"
        for expense in last_expenses
    ]
    answer_message = "Останні витрати:\n\n * " + "\n* ".join(last_expenses_rows)
    await message.answer(answer_message)
