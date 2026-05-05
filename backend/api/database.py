from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from typing import AsyncGenerator
from models.schemas import UploadedFile, AnalysisResultDB  # Import models to register them

# Database URL
import os
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    # Local fallback
    DATABASE_URL = "sqlite+aiosqlite:///./subsiguard.db"
elif DATABASE_URL.startswith("postgres://"):
    # Fix for SQLAlchemy/asyncpg which requires postgresql://
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://") and not DATABASE_URL.startswith("postgresql+asyncpg://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
# If it's already a correct sqlite+aiosqlite or postgresql+asyncpg URL, it will be used as is

# Create Async Engine
# check_same_thread=False is needed ONLY for SQLite
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False

engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
    future=True,
    connect_args=connect_args
)

# Create Async Session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
