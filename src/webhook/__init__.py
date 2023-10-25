import logging
import uvicorn
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from src.config.configuration import get_config, Config
from src.database.db_usage import create_pool, Database
from src.handlers import get_all_routers


async def check_webhook_exists(bot: Bot):
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url:
        await bot.delete_webhook()


class WebAppTelegram:
    config = get_config()

    def __init__(self, config: Config = config):
        self.app = FastAPI()
        self.bot: Bot = Bot(config.get_token())
        self.dp: Dispatcher = Dispatcher()
        self.app.on_event("startup")(self.on_startup)
        self.app.post(config.get_webhook_path())(self.bot_webhook)
        self.app.on_event("shutdown")(self.on_shutdown)

    async def on_startup(self):
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
        self.dp["db_pool"] = await create_pool()
        self.dp.include_router(await get_all_routers(self.dp["db_pool"]))
        await self.bot.set_webhook(url=self.config.get_webhook_url())

    async def bot_webhook(self, update: dict):
        telegram_update = Update(**update)
        await self.dp.feed_update(bot=self.bot, update=telegram_update)

    async def on_shutdown(self):
        await self.dp["db_pool"].close()
        await self.bot.session.close()

    def run_bot(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8080)
