import os 
from aiogram.filters import BaseFilter
from aiogram import Router
from aiogram.types import Message
import json
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class Task(StatesGroup):
    choose_task_week = State()
    choose_task_type = State()

admin_ids = json.loads(os.environ.get['admins'])
router = Router(name = 'admin_router')


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids): # [2]
        self.admin_ids = admin_ids
    async def __call__(self, message: Message):
        return message.from_user.id in self.admin_ids
        

@router.message(IsAdmin(admin_ids),commands=["admin"])
async def admin_menu(message: Message,state: FSMContext):
    FSMContext

    await state.set_state(Task.choose_task_week)



@router.message(
    Task.choose_task_week, 
    F.text.in_(TASKS_WEEK)
)
async def week_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_week=int(message.text))
    await message.answer(
        text="Выберите тип задания",
        reply_markup=make_row_keyboard(TASK_OPTIONS)
    )
    await state.set_state(Task.choose_task_type)

