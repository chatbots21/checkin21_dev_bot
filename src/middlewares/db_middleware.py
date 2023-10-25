from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, callback_query
from src.database.db_usage import Database
import asyncpg


class DatabaseMessageMiddleware(BaseMiddleware):
    def __init__(self, db_pool) -> None:
        self.db_pool: asyncpg.pool.Pool = db_pool
        print("Success message middleware")

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data['db'] = Database(self.db_pool)
        data['status'] = await data['db'].user_check(event.chat.id)
        return await handler(event, data)


class DatabaseCallbackMiddleware(BaseMiddleware):
    def __init__(self, db_pool) -> None:
        self.db_pool: asyncpg.pool.Pool = db_pool
        print("Success callback middleware")

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: callback_query,
            data: Dict[str, Any]
    ) -> Any:
        data['db'] = Database(self.db_pool)
        data['status'] = await data['db'].user_check(event.message.chat.id)
        return await handler(event, data)
