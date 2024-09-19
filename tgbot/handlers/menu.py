from infrastructure.database.db import DataBase
from tgbot.keyboards.inline import (
    menu_keyboard,
    expenses_menu_keyboard,
    come_back_keyboard,
)
from aiogram import types, Router, F
from aiogram.filters import Command

menu_router = Router()

db = DataBase()


# @menu_router.message(Command("/start"))
# async def show_menu(message: types.Message):
#     await message.answer("Виберіть пункт меню:", reply_markup=menu_keyboard())


@menu_router.callback_query(F.data == "expenses")
async def show_expenses(query: types.CallbackQuery):
    await query.answer()
    await query.message.edit_text(
        "⏰ Обери за якій період хочеш переглянути свої витрати",
        reply_markup=expenses_menu_keyboard(),
    )


@menu_router.callback_query(F.data == "expenses_30_days")
async def show_month_expenses(query: types.CallbackQuery):
    text = db.get_month_statistic(query.from_user.id)
    await query.answer()
    await query.message.edit_text(text=text, reply_markup=come_back_keyboard())


@menu_router.callback_query(F.data == "expenses_7_days")
async def show_week_expenses(query: types.CallbackQuery):
    text = db.get_week_statistic(query.from_user.id)
    await query.answer()
    await query.message.edit_text(text=text, reply_markup=come_back_keyboard())


@menu_router.callback_query(F.data == "profit")
async def show_month_profit(query: types.CallbackQuery):
    last_profit = db.last_month_profit(query.from_user.id)
    if not last_profit:
        await query.answer("Доходів ще не має")
    last_profit_row = [
        f"{profit[2]} грн" f"/del{profit[0]} для видалення" for profit in last_profit
    ]
    answer_message = "Останні доходи:\n\n *" + "\n".join(last_profit_row)
    await query.answer()
    await query.message.edit_text(
        text=answer_message, reply_markup=come_back_keyboard()
    )


@menu_router.callback_query(F.data == "exit")
async def exit_handler(query: types.CallbackQuery):
    await query.answer(reply_markup=menu_keyboard())
    await query.message.edit_text(text="Обери операцію", reply_markup=menu_keyboard())
