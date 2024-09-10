from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types

from infrastructure.database import db

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

    await message.answer(text)
