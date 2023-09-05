from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboard import make_row_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from aiogram import Bot

from .test import test_router, Test
from .upload_file import upload_router, TaskUpload




TASKS_WEEK = [str(i) for i in range(1,13)]

TASKS_DESCRIPTION = [
    "Introduction. Python and VSCode installation. Git",
    "Basic types. If condition. Modules.",
    "Cycles",
    "Collections: sets, strings, lists, tuples",
] +[' ']*8

TASK_OPTIONS = [
    'Homework',
    'Test',
    'Description'
]

HW_AVAILABLE_OPTIONS = ['Jupyter Notebook','Github']

TEST_AVAILABLE_OPTIONS = ['']


class Task(StatesGroup):
    choose_task_week = State()
    choose_task_type = State()


router = Router()

router.include_routers(test_router,upload_router)


@router.message(Command("upload_task"))
async def cmd_upload_task(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите неделю",
    )
    await state.set_state(Task.choose_task_week)

###############


@router.message(
    Task.choose_task_week, 
    F.text.in_(TASKS_WEEK)
)
async def week_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_week=message.text.lower())
    await message.answer(
        text="Выберите тип задания",
        reply_markup=make_row_keyboard(TASK_OPTIONS)
    )
    await state.set_state(Task.choose_task_type)


@router.message(
    Task.choose_task_week
)
async def week_chosen(message: Message):
    await message.answer(
        text="Неверный ввод. Укажите номер цифрами",
    )

###### Description


@router.message(
    Task.choose_task_type, 
    F.text == 'Description'
)
async def week_description(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Описание недели {TASKS_DESCRIPTION[int(user_data['chosen_week'])]}"
    )
    await state.clear()


### TEST


@router.message(
    Task.choose_task_type, 
    F.text == 'Test'
)
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_task=message.text.lower())
    await message.answer(
        text="Начинаем тест"
    )
    await state.set_state(Test.question)


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

