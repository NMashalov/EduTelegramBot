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
        event = data['event_from_user']
        session = data["session"] 
        user_id = user.id

        user = await User.get(user_id)

        get_user_info = select(User).filter_by(id= message.from_user.id).first()

        user: User = await get_user_info.scalar().first()

        if user is None:

            await event.answer(
                "Бот по выходным не работает!",
                show_alert=True
            )

        if user is None:
            user = await User.create(id=user_id)
        chat = await Chat.get(chat_id)
        if chat is None:
            chat = await Chat.create(id=chat_id, type=chat_type)

        data["user"] = user
        data["chat"] = chat

        db_session: AsyncSession = data.get("db_session")

        self._logger.debug(f"Getting user with ID {user_id}")

        u = await user.get_user_by_tg_id(db_session, user_id)

        if u is None:
            self._logger.debug(f"User with ID {user_id} not found, creating...")
            u = await user.create_user(db_session, telegram_id=user_id)