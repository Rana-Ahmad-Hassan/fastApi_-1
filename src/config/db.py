from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.models.books import Book

DATABASE_URL = (
    "postgresql+asyncpg://neondb_owner:npg_M5zP2EVFbSqh@ep-nameless-truth-a4d27dsm-pooler.us-east-1.aws.neon.tech/neondb"
)

# Create the async engine
engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

# Session maker
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Initialize the database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# Dependency for FastAPI routes
async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
