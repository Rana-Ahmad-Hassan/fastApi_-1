from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlmodel import SQLModel
from src.models.books import Book

DATABASE_URL = (
    "postgresql+asyncpg://neondb_owner:npg_M5zP2EVFbSqh@ep-nameless-truth-a4d27dsm-pooler.us-east-1.aws.neon.tech/neondb"
)

# Correct way to create async engine
engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
