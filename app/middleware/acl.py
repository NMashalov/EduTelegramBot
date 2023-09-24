from typing import Callable, Awaitable, Dict, Any
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy import select

import logging

from app.models.user import User


class ACLMiddleware(BaseMiddleware):
    def __init__(self):
        self._logger = logging.getLogger("ACLMiddleware")
        super().__init__()

    async def __call__(self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
        ):
        user_data = data['event_from_user']
        user_id, username = user_data.id, user_data.username 
        session = data["session"] 

        get_user_info = await session.execute(select(User).filter_by(id= user_id))

        user: User = await get_user_info.scalar().first()

        if user is None:
            await event.answer(
                "Вы не авторизованы",
                show_alert=True
            )

            await session.merge(User(id=user_id,name=username))
            await session.commit()
            await state.set_state(Auth.question)
            return 
        elif user.mipt_mail is None:
            await event.answer(
                "Вы не указали mipt почту. Пройдите авторизацию",
                show_alert=True
            )
            return
        else:
            return await handler(event, data)

