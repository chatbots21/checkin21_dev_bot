"""
Хендлеры всех текстовых, фото-. видео-. кружочко- сообщений
"""


from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Router
from src.data.data_for_bot import HelloMessage
from src.database.db_usage import Database

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, db: Database, bot: Bot, status: bool):
    hello_message = HelloMessage(message.chat.username)
    if not status:
        await db.add_to_db(message.chat.id, message.chat.username)
    await hello_message.send_to_user(bot, message.chat.id)
