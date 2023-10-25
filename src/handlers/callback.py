"""
Здесь можно разместить все коллбек-хендлеры
"""
from aiogram.types import callback_query
from src.utils.callbackfabric import Info
from aiogram import Router

router = Router()


@router.callback_query(Info.filter())
async def get_choice(callback: callback_query, callback_data: Info):
    if callback_data.important:
        await callback.message.edit_text("В папке с вебхуком Вы найдёте, на мой взгляд, "
                                         "не самый плохой код(аналогов почему-то не видел) по запуску бота "
                                         "через вебхук без глобалов.\n"
                                         "Если у кого-то есть предложения по доработке и улучшениям - милости прошу в "
                                         "лс: @hero_of")
    elif not callback_data.important:
        await callback.message.edit_text("<i>Вы замечательный человек, это на самом деле важно. </i> ❤️")
