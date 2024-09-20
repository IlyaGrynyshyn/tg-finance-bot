from aiogram import Router
from aiogram import types
from aiogram.filters import CommandStart

from infrastructure.database import db
from tgbot.keyboards.inline import menu_keyboard

db = db.DataBase()

start_router = Router()


@start_router.message(CommandStart())
async def bot_start(message: types.Message):
    """Відправляємо вітальне повідомлення і допомога по боту"""
    if db.check_user(message.from_user.id):
        text = f"Вітаємо,ви індитифіковані як існуючий користувач під іменем {message.from_user.username}"
    else:
        text = (
            f"Привіт, {message.from_user.username} ! Я тебе індитифікував як нового користувача. Ти можеш дізнатися "
            f"про мій функціонал через команду /help. "
        )
        db.add_user(message.from_user.id)

    await message.answer(text, reply_markup=menu_keyboard())
