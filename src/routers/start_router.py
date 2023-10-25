from aiogram import Router, types
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    """
    Обработчик команды /start
    """
    await message.answer("Hello!")
