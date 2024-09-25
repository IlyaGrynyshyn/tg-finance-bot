from sqlalchemy import String, Column, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from infrastructure.database.models.base import Base, TimestampMixin, TableNameMixin


class Category(Base, TimestampMixin, TableNameMixin):
    codename: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    aliases: Mapped[str]

    expenses = relationship("Expense", back_populates="category")
