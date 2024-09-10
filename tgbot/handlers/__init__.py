"""Import all routers and add them to routers_list."""
from .start import start_router
from .add_expenses import expenses_router

routers_list = [
    start_router,
    expenses_router
]

__all__ = [
    "routers_list",
]
