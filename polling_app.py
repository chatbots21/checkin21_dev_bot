from src.handlers import get_all_routers
from src.config.configuration import get_config
from aiogram import Dispatcher, Bot
from src.database.db_usage import create_pool, Database
from src.webhook import check_webhook_exists
import asyncio
import logging


async def run_bot():
    config = get_config()
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot: Bot = Bot(config.get_token(), parse_mode="HTML")
    dp: Dispatcher = Dispatcher(db_pool=await create_pool())
    dp.include_router(await get_all_routers(dp["db_pool"]))
    try:
        await check_webhook_exists(bot)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(run_bot())
