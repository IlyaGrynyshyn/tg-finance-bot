import re
from dataclasses import dataclass

from aiogram import types, Router

from infrastructure.database.db import DataBase
from tgbot.handlers.categories import Categories, Category
from tgbot.handlers.errors import error_handler
from tgbot.handlers.errors.error_handler import NotCorrectMassage

# from tgbot.handlers.errors.error_handler import NotCorrectMassage
from tgbot.misc.datetime_now import _get_now_formatted

db = DataBase()
expenses_router = Router()
expenses_router.message()


@dataclass
class Expense:
    id: int | None
    owner: int
    amount: int
    category_name: Category


@expenses_router.message()
async def add_expense(message: types.Message):
    """
    Додає нову витрату
    :param message:
    :return: message.answer
    """
    try:
        expense = add_expenses(message.text, message.from_user.id)
    except error_handler.NotCorrectMassage as e:
        await message.answer(str(e))
        return
    answer_message = f"Додана трана {expense.amount} грн на {expense.category_name}"
    await message.answer(answer_message)


def add_expenses(raw_message: str, owner: int):
    """
    Додавання витрати до дази даних
    :param owner:
    :param user_id:
    :param raw_message:
    :return: Expense
    """
    parsed_message = _parce_message(raw_message)
    categories = parsed_message[1]
    category = Categories().get_categories(categories)
    inserted_row_id = db.add_expense(
        owner=owner,
        amount=parsed_message[0],
        created=_get_now_formatted(),
        category_codename=str(category),
        raw_text=raw_message,
    )
    return Expense(
        id=None, owner=owner, amount=parsed_message[0], category_name=category
    )


def _parce_message(message: str):
    """
    Парсить текст повідомлення про витрати
    :param message:
    :return: total, category
    """
    parce_result = re.match(r"([\d ]+) (.*)", message)
    if (
        not parce_result
        or not parce_result.group(0)
        or not parce_result.group(1)
        or not parce_result.group(2)
    ):
        raise NotCorrectMassage(
            "Не можу зрозуміти ваше повідомлення. Спробуйте ще раз, використовуючи формат, наприклад:\n "
            "50 кава "
        )

    total = parce_result.group(1)
    category = parce_result.group(2)
    return total, category
