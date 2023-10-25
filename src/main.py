import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import config

from routers.start_router import start_router


async def main():
    token = config.get('Telegram', 'token')
    # Включаем логирование
    logging.basicConfig(level=logging.INFO)
    # Объект бота
    bot = Bot(token=token)
    # Диспетчер
    dp = Dispatcher()

    # Регистрируем обработчики
    dp.include_router(start_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
