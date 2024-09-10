"""Import all routers and add them to routers_list."""
from .error_handler import router
routers_list = [
    router

]

__all__ = [
    "routers_list",
]
