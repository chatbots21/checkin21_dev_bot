"""
Хендлеры всех текстовых, фото-. видео-. кружочко- сообщений
"""


from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Bot, Router, F
from src.data.data_for_bot import HelloMessage
from src.database.db_usage import Database
from src.keyboards.replymarkup import ReplyKeyboards
from aiogram.fsm.context import FSMContext
from src.utils.validator import Validator
from src.keyboards.inlinemarkup import InlineKeyboards

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, db: Database, bot: Bot, status: bool):
    hello_message = HelloMessage(message.chat.username)
    if not status:
        await db.add_to_db(message.chat.id, message.chat.username)
    await hello_message.send_to_user(bot, message.chat.id)
