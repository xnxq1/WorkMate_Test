from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker, AsyncSession

from app.infra.config import settings


class DB:

    def __init__(self):
        self.engine = create_async_engine(
            url=settings.DATABASE_URL,
            echo=True
        )
        self.session_factory = async_sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)



db = DB()