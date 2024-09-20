"""Import all routers and add them to routers_list."""

from .add_expenses import expenses_router
from .add_profit import add_profit_router
from .delete_expenses import delete_expense_router
from .echo import echo_router
from .menu import menu_router
from .start import start_router

routers_list = [
    start_router,
    menu_router,
    expenses_router,
    delete_expense_router,
    echo_router,
    # add_profit_router,
]

__all__ = [
    "routers_list",
]
