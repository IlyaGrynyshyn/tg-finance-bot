from aiogram import Bot, types, Router, F
from aiogram.filters import Command
from infrastructure.database.db import DataBase

db = DataBase()

list_profit_router = Router()


@list_profit_router.message(Command(commands=["/profit"]))
async def profit(message: types.Message):
    last_profit = db.last_expenses(message.from_user.id)
    if not last_profit:
        await message.answer("Доходів ще не має")
    last_profit_row = [
        f"{profit[2]} грн в категорії"
        f"/del{profit[0]} для видалення"
        for profit in last_profit
    ]
    answer_message = "Останні доходи:\n\n *" + "\n".join(last_profit_row)
    await message.answer(answer_message)
