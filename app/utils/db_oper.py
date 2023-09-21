from app.models import (
    User,
    UserQuizResults,
    UserHomeworkResults,
    Homework, 
)

from sqlalchemy import select,desc
from sqlalchemy.ext.asyncio import AsyncSession

async def init_user(
        user_id : int,
        user_name: str,
        session: AsyncSession,
        ):
    get_user_info = (
        select(UserQuizResults)
        .filter(UserQuizResults.user_id == user_id)
        .order_by(desc(UserQuizResults.week))
    )
    db_query = await session.execute(get_user_info)
    if db_query is None:
        user = User(
            user_id=user_id,
            name = user_name,
        )
        user.homework_results = [UserHomeworkResults(
            result = 0,
            week = H,
            homework = [for result in zip(range(1,13))]
        ) ]
        session.merge(user)
    else:

    user = db_query.scalar()

    if db.session.query(User.id).filter_by(name='davidism').first() is not None

