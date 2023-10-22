from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import asyncio
import logging
import kernel.bus as kern

API_TOKEN = '<insert your api-token>'

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    try:
        asyncio.run(kern.handle_all(dp))
    except (KeyboardInterrupt, SystemExit):
        pass
