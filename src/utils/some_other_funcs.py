from aiogram.types import Message, InlineKeyboardMarkup
from aiogram import Bot
from src.keyboards.inlinemarkup import InlineKeyboards


async def delete_last_message(message: Message, bot: Bot, post_flag: bool = False,
                              delete_two: bool = True):
    try:
        if delete_two:
            purpose_id = message.message_id - 1 if post_flag else message.message_id
            await bot.delete_message(message.chat.id, message_id=purpose_id)
        else:
            await bot.delete_message(message.chat.id, message_id=message.message_id)
            await bot.delete_message(message.chat.id, message_id=message.message_id - 1)
    except Exception as err:
        print(err)
