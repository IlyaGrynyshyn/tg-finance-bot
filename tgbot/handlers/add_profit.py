from aiogram import types, F
import re
from typing import NamedTuple, Optional
from aiogram import Router
from dataclasses import dataclass

from tgbot.handlers.errors import error_handler
from tgbot.handlers.errors.error_handler import NotCorrectMassage
from tgbot.misc.datetime_now import _get_now_formatted
from infrastructure.database.db import DataBase
add_profit_router = Router()

db = DataBase()

@dataclass
class Profit:
    """Структура додавання в БД нового доходу"""

    id: int | None
    owner: int
    amount: int


@add_profit_router.message(F.text.regexp(r"^\++"))
async def add_profit(message: types.Message):
    """
    :param message:
    :return: message.answer
    """
    try:
        profit = save_profit_to_db(message.text, message.from_user.id)
    except error_handler.NotCorrectMassage as e:
        await message.answer(str(e))
        return
    answer_message = f"Доданий прибуток в {profit.amount} грн"
    await message.answer(answer_message)


def _parce_message(message: str):
    """
    Парсить текст повідомлення про витрати
    :param message:
    :return: total, category
    """
    parce_result = re.match(r"[+-]?(\d[\d ]*) (.*)", message)
    if (
            not parce_result
            or not parce_result.group(0)
            or not parce_result.group(1)
            or not parce_result.group(2)
    ):
        raise NotCorrectMassage(
            "Не можу зрозуміти ваше повідомлення. Спробуйте ще раз, використовуючи формат, наприклад:\n "
            "+600 кава "
        )
    total = parce_result.group(1)
    return total


def save_profit_to_db(raw_message: str, owner: int) -> Profit:
    """
    Додавання витрати до дази даних
    :param owner:
    :param user_id:
    :param raw_message:
    :return: Expense
    """
    parsed_message = _parce_message(raw_message)
    db.add_profit(
        owner=owner,
        amount=parsed_message,
        created=_get_now_formatted(),
        row_text=raw_message,
    )
    return Profit(id=None, owner=owner, amount=parsed_message)
