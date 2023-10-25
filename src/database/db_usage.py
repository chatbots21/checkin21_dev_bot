from typing import Union
import asyncpg
from src.config.configuration import get_config


class Database:
    def __init__(self, pool: asyncpg.pool.Pool):
        self.pool = pool

    async def user_check(self, tg_id: int) -> bool:
        try:
            query: str = "SELECT tg_id from users WHERE tg_id=$1"
            result: Union[int, None] = await self.pool.fetchval(query, tg_id)
            return True if result else False
        except Exception as err:
            print(err)

    async def add_to_db(self, tg_id: int, username: str):
        try:
            query: str = "INSERT INTO users(tg_id, username) VALUES($1, $2)"
            await self.pool.execute(query, tg_id, username)
        except Exception as ex:
            print(f'Failed to add information: {ex}')


async def create_pool():
    config = get_config()
    return await asyncpg.create_pool(user=config.get_username(), password=config.get_db_password(),
                                     database=config.get_db_name(), host='127.0.0.1')
