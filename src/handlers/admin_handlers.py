"""
Хендлеры для админки (без коллбеков, хотя это можно пересмотреть)
"""


from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.keyboards.inlinemarkup import InlineKeyboards
from src.database.db_usage import Database


router: Router = Router()


