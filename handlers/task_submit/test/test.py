from aiogram import Router, F
from aiogram.types import Message

from keyboard import make_row_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class Test(StatesGroup):
    question = State()
    answer = State()

router = Router()



@router.message(
        
        
)
async def cmd_upload_task(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите неделю",
    )
    await state.set_state(Task.choose_task_week)