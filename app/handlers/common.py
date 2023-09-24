from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from app.models.user import User
from sqlalchemy import select

from app.keyboard import make_row_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession


from app.handlers.task import Task
from app.handlers.test import Test
from app.handlers.auth import Auth

router = Router(name="commands-router")

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext, session: AsyncSession):
    id, name = message.from_user.id, message.from_user.first_name
    user = await session.merge(User(id=id, name = name,))
    await session.commit()
    print(id,name)
    await message.answer(
        text="Бот курса по Python для кафедры педагогики"
    )
    if user:
        await state.set_state(Test.question)
    else:
        await state.set_state(Auth.question)



@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )