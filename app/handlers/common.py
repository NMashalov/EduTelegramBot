from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from app.keyboard import make_row_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from sqlalchemy.ext.asyncio import AsyncSession

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.handlers.test import Test

from app.services.reminder import sheduled_message
from aiogram import Bot

from services.reminder import TelegramMethodJob



router = Router(name="commands-router")

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext, session: AsyncSession):
    await message.answer(
        text="Бот курса по Python для кафедры педагогики"
    )

@router.message(Command(commands=["remind"]))
async def cmd_start(message: Message, scheduler: AsyncIOScheduler, bot: Bot):
    id= message.from_user.id
    await message.answer(
        text=f"Я буду напоминать о занятии {id} "
    )
    scheduler.add_job(TelegramMethodJob(sheduled_message).provide_bot,'interval',seconds=3,kwargs={'user_id':id},max_instances=5)



@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )