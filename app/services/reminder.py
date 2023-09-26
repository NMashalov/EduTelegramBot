from datetime import datetime
import time
from aiogram import Bot

from typing import Optional

class TelegramMethodJob:
    _bot = None

    def __init__(self,method):
        self.method = method

    async def provide_bot(self,*args,**kwargs):
        await self.method(*args,bot=TelegramMethodJob._bot,**kwargs)

    @classmethod
    def set_bot(cls, bot: Optional[Bot]):
        cls._bot = bot

async def sheduled_message(bot: Bot, user_id: int):
    await bot.send_message( user_id, "Я подождал 3 секунды")

