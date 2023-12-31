from aiogram.filters import Command
from aiogram.types import Message

from app.keyboard import make_row_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import F,Router

from .upload_task import TaskUpload

TASKS_WEEK = [i for i in range(1,13)]

HW_AVAILABLE_OPTIONS = ['Jupyter Notebook','Github']



class Task(StatesGroup):
    task_week = State()
    choose_task_type = State()

router = Router(name='task')

@router.message(Command("task"))
async def cmd_upload_task(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите неделю",
        reply_markup=make_row_keyboard(TASKS_WEEK)
    )
    await state.set_state(Task.task_week)

###############


@router.message(
    Task.task_week, 
    F.text.in_(TASKS_WEEK)
)
async def week_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_week=int(message.text))
    await message.answer(
        text=f"Описание недели {TASKS_DESCRIPTION[int(message['chosen_week'])]}",
        reply_markup=make_row_keyboard(TASK_OPTIONS)
    )
    await state.set_state(Task.choose_task_type)

@router.message(
    Task.choose_task_type, 
    F.text == 'Homework'
)
async def homework_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_task=message.text.lower())
    await message.answer(
        text="Выбери способ сдачи задания",
        reply_markup=make_row_keyboard(HW_AVAILABLE_OPTIONS)
    )
    await state.set_state(TaskUpload.select_uploading_type)
    user_data = await state.get_data()
    


### Homework


