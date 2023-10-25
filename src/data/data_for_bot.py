import datetime

from aiogram import Bot
from aiogram.types import Message

from src.database.db_usage import Database
from src.keyboards.inlinemarkup import InlineKeyboards


class HelloMessage:
    """
    Всё, что связано с приветственным сообщением на /start
    Предлагаю хранить его в БД, чтобы оперативно менять через админку в случае чего.
    """
    def __init__(self, username: str):
        """
        text - текст приветственного сообщения
        photo_id - id приветственного фото
        video_id - id приветственного видео
        video_note_id - id приветственного кружка
        """
        self.text: str = f"<b>Hello, {username}</b>!\n\nРады приветствовать тебя в нашем <i>боте</i>."
        self.photo_id: str = ''
        self.video_id: str = ''
        self.video_note_id: str = ''

    async def send_to_user(self, bot: Bot, tg_id: int) -> None:
        """
        Кто придумает оптимизацию этого дерьма, максимально кастомную и удобную, как тут - куплю пиво.
        Если вкратце, это отправки необычного сообщения, чаще всего приветственного/поста в канал.
        Она рассчитана на то, что сообщение может быть максимально кастомным: содержать в себе текст, фото,
        видео, кружок, что-то одно из этого или вообще ничего.
        :param bot: Bot
        :param tg_id: int
        :return: None
        """
        if self.photo_id:
            if self.text:
                if not self.video_id and not self.video_note_id:
                    await bot.send_photo(tg_id, self.photo_id, caption=self.text,
                                         reply_markup=await InlineKeyboards().start_keyboard())
                elif self.video_id:
                    await bot.send_photo(tg_id, self.photo_id, caption=self.text)
                    await bot.send_video(tg_id, self.video_id,
                                         reply_markup=await InlineKeyboards().start_keyboard())
                elif self.video_note_id:
                    await bot.send_photo(tg_id, self.photo_id, caption=self.text)
                    await bot.send_video_note(tg_id, self.video_note_id,
                                              reply_markup=await InlineKeyboards().start_keyboard())
            elif self.video_id:
                await bot.send_photo(tg_id, self.photo_id)
                await bot.send_video(tg_id, self.video_id,
                                     reply_markup=await InlineKeyboards().start_keyboard())
            elif self.video_note_id:
                await bot.send_photo(tg_id, self.photo_id)
                await bot.send_video_note(tg_id, self.video_note_id,
                                          reply_markup=await InlineKeyboards().start_keyboard())
        elif self.video_id:
            if self.text:
                await bot.send_video(tg_id, self.video_id, caption=self.text,
                                     reply_markup=await InlineKeyboards().start_keyboard())
            else:
                await bot.send_video(tg_id, self.video_id, reply_markup=await InlineKeyboards().start_keyboard())
        elif self.video_note_id:
            if self.text:
                await bot.send_message(tg_id, self.text)
                await bot.send_video_note(tg_id, self.video_note_id,
                                          reply_markup=await InlineKeyboards().start_keyboard())
            else:
                await bot.send_video_note(tg_id, self.video_note_id,
                                          reply_markup=await InlineKeyboards().start_keyboard())
        elif self.text:
            await bot.send_message(tg_id, self.text, reply_markup=await InlineKeyboards().start_keyboard())
        else:
            await bot.send_message(tg_id, "Приветственное сообщение не установлено",
                                   reply_markup=await InlineKeyboards().start_keyboard())

    # async def set_data(self, db: Database):
    #     data = (await db.get_hello_message())[0]
    #     self.text = data["hello_text"]
    #     self.photo_id = data["hello_photo"]
    #     self.video_id = data["hello_video"]
    #     self.video_note_id = data["hello_video_note"]


