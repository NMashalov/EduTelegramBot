from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboard import make_row_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import aiosqlite
from pathlib import Path

path_to_db = Path(__file__).parent.parent.parent / 'database' / "telegram.db"

router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    id, first_name, last_name = message.from_user.id, message.from_user.first_name, message.from_user.last_name


    if 

    print(id,first_name,last_name)
    db = await aiosqlite.connect(path_to_db)
    cursor = await db.execute(
    '''
        insert into user (user_name,user_surname,telegram_id)
        VALUES 
        (?,?,?)
    ''',(id,first_name,last_name))
    await db.commit()

    await state.update_data(cursor=cursor)                    
    await state.clear()
    await message.answer(
        text="Бот для загрузки заданий "
             "Используй команду /upload_task",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )