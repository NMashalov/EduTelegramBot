import asyncio
import os 
import sys 
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv('TELEGRAM_TOKEN')

hello_router = Router(name='hello')

@hello_router.message(Command(commands=["hello"]))
async def hello(message:Message):
    # получаем уникальный id пользователя в телеграме
    # и его имя
    id, name = message.from_user.id, message.from_user.first_name
    # rкогда отправляем сообщение дергается API и мы просто ждем, пока там
    # разберутся, что делать дальше. Пишем await, чтобы 
    # в это время заниматься чем-то более интересным :)
    await message.answer(
        text="Бот курса по Python для кафедры педагогики"
    )

@hello_router.message(Command(commands=["goodbye"]))
async def hello(message:Message):
    """
        Напиши здесь функцию для прощания с пользователем
    """
    pass


async def main():

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(hello_router )
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())