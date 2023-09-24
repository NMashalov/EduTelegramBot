from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User

async def get_user_by_tg_id(
        session: AsyncSession,
        telegram_id: int,
) -> Optional[User]:
    """
    Returns user by tg-id
    :param session: An `AsyncSession` object
    :param telegram_id: A telegram-ID
    :return: `User` or `None`
    """

    stmt = select(User).where(User.telegram_id == telegram_id)

    result = await session.execute(stmt)

    return result.scalars().first()

async def init_user_homework(
        session: AsyncSession,
        telegram_id: int,
) -> Optional[User]:
    """
    Returns user by tg-id
    :param session: An `AsyncSession` object
    :param telegram_id: A telegram-ID
    :return: `User` or `None`
    """

    stmt = select(User).where(User.telegram_id == telegram_id)

    result = await session.execute(stmt)

    return result.scalars().first()