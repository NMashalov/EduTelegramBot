import asyncio
import logging
import sys
import os
import datetime

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from handlers import common_router, task_router


TOKEN = os.getenv('TELEGRAM_TOKEN')


dp = Dispatcher()

async def periodic():
    while True:
        print('periodic')
        await asyncio.sleep(1)
        


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_routers(common_router, task_router)
    await dp.start_polling(bot)
    #await periodic()
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())#,periodic())