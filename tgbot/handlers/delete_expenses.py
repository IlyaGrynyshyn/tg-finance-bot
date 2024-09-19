import re
from dataclasses import dataclass
from aiogram import types, Router
from aiogram.filters import Filter
from aiogram import F

from infrastructure.database.db import DataBase
from tgbot.handlers.categories import Categories, Category
from tgbot.handlers.errors import error_handler
from tgbot.handlers.errors.error_handler import NotCorrectMassage

# from tgbot.handlers.errors.error_handler import NotCorrectMassage
from tgbot.misc.datetime_now import _get_now_formatted

db = DataBase()
expenses_router = Router()
expenses_router.message()

delete_expense_router = Router()


@delete_expense_router.message(F.text.regexp("^/del"))
async def del_expense(message: types.Message):
    row_id = int(message.text[4:])
    db.delete("expense", row_id)
    await message.answer(f"Запис №{row_id} удалена")
