from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.utils.callbackfabric import Info


class InlineKeyboards:
    def __init__(self):
        """
        инициализация объекта класса InlineKeyboardBuilder, который позволяет очень удобно строить клавиатуры
        """
        self.keyboard = InlineKeyboardBuilder()

    async def start_keyboard(self):
        self.keyboard.button(text="Получить важную информацию о боте", callback_data=Info(important=True))
        self.keyboard.button(text="Получить информацию о себе", callback_data=Info(important=False))
        self.keyboard.adjust(1)     # количество кнопок в одном ряду
        return self.keyboard.as_markup()
