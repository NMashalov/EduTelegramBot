import pytest
import pytest_asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from rtsu_students_bot.service import user
from rtsu_students_bot.models import Base

from .config import settings

pytest_plugins = ('pytest_asyncio',)

engine = create_async_engine(
    settings.db_url,
)

SessionLocal = sessionmaker(autoflush=True, bind=engine, class_=AsyncSession)


@pytest_asyncio.fixture()
async def session():
    """
    Initializes client
    :return: Prepared `RTSUApi` client
    """

    async with SessionLocal() as e, e.begin():
        yield e


@pytest.mark.asyncio
async def test_tables_creating():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)