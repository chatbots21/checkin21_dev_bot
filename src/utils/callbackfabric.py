"""
Фабрика коллбеков. Значительно упрощает обработку коллбеков + написание инлайн-клавиатур
"""
from aiogram.filters.callback_data import CallbackData


class Info(CallbackData, prefix="Info"):
    important: bool

