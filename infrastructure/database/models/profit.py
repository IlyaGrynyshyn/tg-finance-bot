from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.database.models.base import Base, TimestampMixin, TableNameMixin


class Profit(Base, TimestampMixin, TableNameMixin):
    profit_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    amount = Column(Integer, nullable=False)
    raw_text = Column(Text)

    owner = relationship("User", back_populates="profits")
