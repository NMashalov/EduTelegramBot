from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.keyboard import make_row_keyboard

from sqlalchemy import select,desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User, UserQuizResults


class Profile(StatesGroup):
    start_profile = State()
    select_option = State()
    question = State()
    results = State()

PROFILE_AVAILABLE_OPTIONS = [
    'Account',
    'Results',
    'Redact'
]

router = Router(name='profile')

@router.message(
    
)
async def show_profile(message: Message, session: AsyncSession, state: FSMContext,):

    await state.set_state(Profile.select_option)
    await message.answer(
        text="Что бы ты хотел узнать?",
        reply_markup=make_row_keyboard(PROFILE_AVAILABLE_OPTIONS)
    )


@router.message(
    Profile.select_option,
    F.text == 'Account'
)
async def show_profile(message: Message, session: AsyncSession, state: FSMContext):
    get_user_info = select(User).filter(User.id == message.from_user.id).first()
    db_query = await session.execute(get_user_info)
    user = db_query.scalar()
    await message.answer(
        text=f"Твой логин в TG: {user.name}\n"
            f"Твоя MIPT почта: {user.mipt_mail}\n"
            f"Администратор: {'Да' if user.admin else 'Нет'}"
    )
    await state.clear()



@router.message(
    Profile.select_option,
    F.text == 'Results'
)
async def show_profile(message: Message, session: AsyncSession, state: FSMContext):

    get_user_info = (
        select(UserQuizResults)
        .filter(UserQuizResults.user_id == message.from_user.id)
        .order_by(desc(UserQuizResults.week))
    )
    db_query = await session.execute(get_user_info)
    user_quiz_results = db_query.scalars().all()
    
    results = '\n'.join([
        f'Неделя {user_result.quiz_week}: {user_result.quiz_results}'
        for user_result in user_quiz_results
    ])

    await message.answer(results)
    await state.clear()
    




@router.message(
    Profile.select_option,
    F.text == 'Profile'
    )
async def show_profile(message: Message, session: AsyncSession, state: FSMContext):
    get_user_info = select(User).filter(User.id == message.from_user.id).first()
    db_query = await session.execute(get_user_info)

    user = session.execute(get_user_info)


    await message.answer(f"Name: {user.name}\n",
                            f"Mipt mail: {user.mipt_mail}\n",
                        f"Admin: {'Да' if user.admin else 'Нет'}")




