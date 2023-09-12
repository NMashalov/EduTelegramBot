from aiogram import Router, F
from aiogram.types import Message

from app.keyboard import make_row_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from aiogram import Bot


import pathlib

MEDIA_PATH = pathlib.Path.home() / 'edu_telegram_bot' / 'media'

class TaskUpload(StatesGroup):
    select_uploading_type = State()
    uploading_task = State()

router = Router()

### Download file

@router.message(
    TaskUpload.select_uploading_type,
    F.text == "Jupyter Notebook"
)
async def jup_note_chosen(message: Message,state: FSMContext):
    await message.answer(
        "Приложи свой Jupyter Notebook. Он должен весить меньше 10Мб",
    )
    await state.set_state(TaskUpload.uploading_task)


@router.message(
    TaskUpload.uploading_task
)
async def jup_upload(message: Message,state: FSMContext, bot: Bot):
    if file_id := message.document.file_id:
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, MEDIA_PATH / "jup_note.ipynb")
    await message.answer(
        "Спасибо. Я проверю твой ноутбук :)",
    )
    await state.clear()


### Github link

@router.message(
    TaskUpload.select_uploading_type,
    F.text == "Github"
)
async def gihub_chosen(message: Message, state: FSMContext):
    await message.answer(
        "Укажи ссылку на свой Jupyter Notebook на github.",
    )
    await state.set_state(TaskUpload.uploading_task)