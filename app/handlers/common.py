from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboard import make_row_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import aiosqlite


router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
 msg.from_user.id, msg.from_user.first_name

    db = await aiosqlite.connect(...)
    cursor = await db.execute('SELECT * FROM some_table')
    row = await cursor.fetchone()
    rows = await cursor.fetchall()
    await cursor.close()
    await db.close()

    msg.from_user.id, msg.from_user.first_name

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