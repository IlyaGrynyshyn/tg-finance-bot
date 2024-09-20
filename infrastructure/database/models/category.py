from sqlalchemy import String, Column, Text
from sqlalchemy.orm import relationship

from infrastructure.database.models.base import Base, TimestampMixin, TableNameMixin


class Category(Base, TimestampMixin, TableNameMixin):
    codename = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    aliases = Column(Text)

    expenses = relationship("Expense", back_populates="category")
