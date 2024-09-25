from sqlalchemy import String, Column, Text, Integer, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from infrastructure.database.models.base import Base, TimestampMixin, TableNameMixin


class Expense(Base, TimestampMixin, TableNameMixin):
    expense_id = Column(Integer, primary_key=True)
    owner_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    amount = Column(Integer, nullable=False)
    raw_text = Column(Text)
    category_codename = Column(
        String(255), ForeignKey("categorys.codename"), nullable=False
    )

    owner = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
