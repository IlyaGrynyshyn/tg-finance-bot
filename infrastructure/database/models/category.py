from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from infrastructure.database.models.base import Base, TimestampMixin, TableNameMixin


class Category(Base, TimestampMixin, TableNameMixin):
    codename: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    aliases: Mapped[str] = mapped_column(String(255))

    expenses = relationship("Expense", back_populates="category")
