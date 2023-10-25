import asyncpg.pool
from aiogram import Router
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.handlers.message_handlers import router as form_router
from src.handlers.admin_handlers import router as admin_router
from src.handlers.start_stop import router as start_stop_router
from src.handlers.callback import router as callback_router
from src.handlers.inline_mode import router as inline_mode_router
from src.middlewares.db_middleware import DatabaseMessageMiddleware, DatabaseCallbackMiddleware


async def get_all_routers(db_pool: asyncpg.pool.Pool) -> Router:
    form_router.message.middleware.register(DatabaseMessageMiddleware(db_pool))
    admin_router.message.middleware.register(DatabaseMessageMiddleware(db_pool))
    callback_router.callback_query.middleware.register(DatabaseCallbackMiddleware(db_pool))
    router: Router = Router()
    router.include_routers(
        form_router, admin_router, start_stop_router, callback_router, inline_mode_router
    )
    return router
