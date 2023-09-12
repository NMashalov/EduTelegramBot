import os 
from aiogram.filters import BaseFilter
from aiogram import Router,F
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


COURSE_PASS = 'NN_is_the_best'

class Auth(StatesGroup):
    check_pass = State()
    input_mipt_email = State()

router = Router(name='auth')

@router.message(
    Auth.check_pass, 
    F.text == COURSE_PASS
)
async def good_pass(message: Message, state: FSMContext, session:  AsyncSession):
    await state.update_data(chosen_task=message.text.lower())
    id = message.from_user.id,
    await message.answer(
        text="Отлично, пароль верный!"
    )
    await message.answer(
        text="Введи свою почту МФТИ"
    )
    await state.set_state(Auth.input_mipt_email)

# error handling
@router.message(
    Auth.check_pass, 
)
async def bad_pass(message: Message, state: FSMContext, session:  AsyncSession):
    await message.answer(
        text="Пароль неверный"
    )


@router.message(
    Auth.input_mipt_email, 
)
async def good_pass(message: Message, state: FSMContext, session:  AsyncSession):
    id = message.from_user.id
    await state.set_state(Auth.first_question)

    # get user info
    get_user_info = select(User).filter(User.id == message.from_user.id).first()
    db_query = await session.execute(get_user_info)
    authed_user:User = db_query.scalar()

    authed_user.mipt_mail = message.text
    await session.commit()
    await state.clear()
    await message.answer(
        text=f"Отлично, {User.name}."
            "Теперь ты зарегестрирован 🎉"
    )

