from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from app.models.user import User
from sqlalchemy import select

from app.keyboard import make_row_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from pathlib import Path


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


router = Router(name="commands-router")

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext, session: AsyncSession):
    id, name = message.from_user.id, message.from_user.first_name
    await session.merge(User(id=message.from_user.id, name = name,))
    await session.commit()
    print(id,name)
    await message.answer(
        text="Бот курса по Python для кафедры педагогики"
    )

@router.message(Command(commands=['profile']))
async def show_profile(message: Message, session: AsyncSession):
    get_user_info = select(User).filter(User.id == message.from_user.id).first()
    user = session.execute(get_user_info)

    await message.answer(f"Name: {user.name}\n",
                            f"Mipt mail: {user.mipt_mail}\n",
                        f"Admin: {'Да' if user.admin else 'Нет'}")

@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )