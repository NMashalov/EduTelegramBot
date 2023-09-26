import asyncio
import os 
import sys 
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import BaseMiddleware


#нужно установить пакет apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler



TOKEN = os.getenv('TELEGRAM_TOKEN')

hello_router = Router(name='hello')


## позволяет доставать scheduler из агрументов фунции
class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        super().__init__()
        self._scheduler = scheduler

    async def __call__(self,handler,event,data):
        data["scheduler"] = self._scheduler
        return await handler(event, data)


@hello_router.message(Command(commands=["remind"]))
async def hello(message:Message, bot: Bot, scheduler: AsyncIOScheduler):
    id, name = message.from_user.id, message.from_user.first_name
    await message.answer(
        text="Бот будет напоминать каждые 20 секунд и каждый день в 1.10"
    )
    # задаём выполнение задачи в равные промежутки времени
    scheduler.add_job(bot.send_message,'interval',seconds=20 ,args=(id,"Я напоминаю каждые 20 секунд"))
    # задаём выполнение задачи по cron - гибкий способ задавать расписание. Подробнеее https://crontab.guru/#8_*_*_4
    scheduler.add_job(bot.send_message,'cron',hour=1,minute=10,args=(id,"Я напомнил в 1.10 по Москве"))


async def main():
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.start()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    # регистрируем middleware c scheduler
    dp.update.middleware(
        SchedulerMiddleware(scheduler=scheduler),
    )
    dp.include_routers(hello_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    asyncio.run(main())