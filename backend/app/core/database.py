# database.py – Sets up the asynchronous database connection using SQLAlchemy and asyncpg

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings  # Import project settings loaded from .env

# Build the full async PostgreSQL connection URL
DATABASE_URL = (
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# Create an asynchronous SQLAlchemy engine (echo=True logs queries to console)
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a sessionmaker that will be used for dependency injection in FastAPI
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # Keeps objects alive after commit
)

# Dependency to be injected into routes/services to access the DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session