from aiogram import F
from aiogram import types, Router

from infrastructure.database.db import DataBase
from tgbot.keyboards.inline import expenses_menu_keyboard

# from tgbot.handlers.errors.error_handler import NotCorrectMassage

db = DataBase()
expenses_router = Router()
expenses_router.message()

delete_expense_router = Router()


@delete_expense_router.message(F.text.regexp("^/del"))
async def del_expense(message: types.Message):
    row_id = int(message.text[4:])
    db.delete("expense", row_id)
    await message.answer(f"Запис №{row_id} удалена", reply_markup=expenses_menu_keyboard())
