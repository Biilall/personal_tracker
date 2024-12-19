from .user_router import router as user_router
from .expense_router import router as expense_router
ROUTERS = [
    {"router": user_router, "prefix": "/auth"},
    {"router": expense_router, "prefix": "/expense"},

]
def include_routers(app):
    for route in ROUTERS:
        prefix = route.get("prefix", "")
        app.include_router(route["router"], prefix=prefix)
