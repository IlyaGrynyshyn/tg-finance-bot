from datetime import datetime

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    String,
    Integer,
    ForeignKey,
    Numeric,
    DateTime,
)
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///sqlite3.db")

metadata = MetaData()

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    username = Column(String(255))
    address = Column(String(255))
    town = Column(String(255))
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    cost_price = Column(Numeric(10, 2), nullable=True)
    selling_price = Column(Numeric(10, 2), nullable=True)
    quantity = Column("quantity", Integer, nullable=True)


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    date_placed = Column(DateTime, default=datetime.now)
    date_shipped = Column(DateTime, nullable=True)


class OrderLines(Base):
    __tablename__ = "order_lines"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    items_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer, nullable=True)


Session = sessionmaker(bind=engine)
session = Session()

new_customer = Customer(
    first_name="Jane",
    last_name="Smith",
    email="jane.smith@example.com",
    username="janesmith",
    address="456 Oak St",
    town="Anywhere",
)

session.add(new_customer)
session.commit()
