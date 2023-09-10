import asyncio
import logging
import sys
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from handlers import common_router, task_router
from app.middleware.db_session import DbSessionMiddleware
from app.ui_commands import set_ui_commands


DB_PATH = Path(__file__).parent.parent / 'database' / "test.db"
TOKEN = os.getenv('TELEGRAM_TOKEN')
ADMIN_USER = os.getenv('ADMIN_USER')


from aiogram import Bot



async def main():
    engine = create_async_engine('sqlite+aiosqlite:///' + str(DB_PATH) , echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    dp.include_routers(common_router, task_router)

    #await set_ui_commands(bot)
    await dp.start_polling(bot)
    #await periodic()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())#,periodic())