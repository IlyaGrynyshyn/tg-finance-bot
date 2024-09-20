from typing import Optional

from sqlalchemy import BIGINT, Boolean, true
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import Base, TimestampMixin, TableNameMixin


class User(Base, TimestampMixin, TableNameMixin):
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    username: Mapped[Optional[str]] = mapped_column(String(128))
    telegram_id: Mapped[int] = mapped_column(BIGINT, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, server_default=true())

    expenses = relationship("Expense", back_populates="owner")
    profits = relationship("Profit", back_populates="owner")

    def __repr__(self):
        return f"<User {self.user_id} | {self.telegram_id} | {self.username}>"
