from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# This is a simple keyboard, that contains 2 buttons
def very_simple_keyboard():
    buttons = [
        [
            InlineKeyboardButton(
                text="📝 Створити замовлення", callback_data="create_order"
            ),
            InlineKeyboardButton(text="📋 Мої замовлення", callback_data="my_orders"),
        ],
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons,
    )
    return keyboard


# This is the same keyboard, but created with InlineKeyboardBuilder (preferred way)
def simple_menu_keyboard():
    # First, you should create an InlineKeyboardBuilder object
    keyboard = InlineKeyboardBuilder()

    # You can use keyboard.button() method to add buttons, then enter text and callback_data
    keyboard.button(text="📝 Створити замовлення", callback_data="create_order")
    keyboard.button(
        text="📋 Мої замовлення",
        # In this simple example, we use a string as callback_data
        callback_data="my_orders",
    )

    # If needed you can use keyboard.adjust() method to change the number of buttons per row
    # keyboard.adjust(2)

    # Then you should always call keyboard.as_markup() method to get a valid InlineKeyboardMarkup object
    return keyboard.as_markup()


def menu_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.max_width: int = 2
    keyboard.button(text="💸 expenses 💸", callback_data="expenses")
    keyboard.button(text="💰 profit 💰", callback_data="profit")
    keyboard.button(text="📈 investment 📈", callback_data="investment")
    return keyboard.as_markup()


def expenses_menu_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Expenses last 30 days", callback_data="expenses_30_days")
    keyboard.button(text="Expenses last 7 days", callback_data="expenses_7_days")
    return keyboard.as_markup()


def profit_menu_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="show profit", callback_data="show_profit")
    keyboard.button(text="add profit", callback_data="add_profit")
    return keyboard.as_markup()


def come_back_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Exit", callback_data="exit")
    return keyboard.as_markup()


# For a more advanced usage of callback_data, you can use the CallbackData factory
class OrderCallbackData(CallbackData, prefix="order"):
    """
    This class represents a CallbackData object for orders.

    - When used in InlineKeyboardMarkup, you have to create an instance of this class, run .pack() method, and pass to callback_data parameter.

    - When used in InlineKeyboardBuilder, you have to create an instance of this class and pass to callback_data parameter (without .pack() method).

    - In handlers you have to import this class and use it as a filter for callback query handlers, and then unpack callback_data parameter to get the data.

    # Example usage in simple_menu.py
    """

    order_id: int


def my_orders_keyboard(orders: list):
    # Here we use a list of orders as a parameter (from simple_menu.py)

    keyboard = InlineKeyboardBuilder()
    for order in orders:
        keyboard.button(
            text=f"📝 {order['title']}",
            # Here we use an instance of OrderCallbackData class as callback_data parameter
            # order id is the field in OrderCallbackData class, that we defined above
            callback_data=OrderCallbackData(order_id=order["id"]),
        )

    return keyboard.as_markup()
