"""Import all routers and add them to routers_list."""

from .menu import menu_router
from .start import start_router
from .add_expenses import expenses_router
from .list_profit import list_profit_router
from .list_expenses import list_expenses_router
from .delete_expenses import delete_expense_router
from .add_profit import add_profit_router
from .echo import echo_router

# from .simple_menu import menu_router

routers_list = [
    start_router,
    menu_router,
    echo_router,
    # expenses_router,
    # list_expenses_router,
    # delete_expense_router,
    # add_profit_router,
    # list_profit_router,
]

__all__ = [
    "routers_list",
]
