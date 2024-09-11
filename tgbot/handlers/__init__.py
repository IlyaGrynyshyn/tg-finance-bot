"""Import all routers and add them to routers_list."""

from .start import start_router
from .add_expenses import expenses_router
from .list_expenses import list_expenses_router
from .delete_expenses import delete_expense_router

routers_list = [
    start_router,
    list_expenses_router,
    delete_expense_router,
    expenses_router,
]

__all__ = [
    "routers_list",
]
