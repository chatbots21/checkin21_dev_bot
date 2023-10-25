from aiogram import Bot, Router
from src.config.configuration import get_config

router = Router()


@router.startup()
async def notify_start(bot: Bot):
    config = get_config()
    await bot.send_message(config.get_developer_id(), "Бот запущен!")


@router.shutdown()
async def stop_bot(bot: Bot):
    config = get_config()
    await bot.send_message(config.get_developer_id(), "Бот остановлен!")
