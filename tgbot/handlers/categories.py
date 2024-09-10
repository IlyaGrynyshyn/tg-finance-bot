from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types
from dataclasses import dataclass

from infrastructure.database import db

db = db.DataBase()

category_router = Router()
category_router.message()


@dataclass
class Category:
    codename: str
    name: str
    aliases: list[str]


class Categories:
    def __init__(self):
        self._categories = db.select_all_categories()

    def get_all_categories(self) -> list[Category]:
        return self._categories

    def get_categories(self, category_name: str) -> Category:
        """Повертає категорію по одному з її aliases"""
        finded = None
        other_category = None
        for category in self._categories:
            if category[0] == "other":
                other_category = category
            for alias in category:
                if category_name in str(alias):
                    finded = category[1]
        if not finded:
            finded = other_category[1]
        return finded
