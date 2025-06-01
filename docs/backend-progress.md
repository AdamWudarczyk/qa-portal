# Development Notes – Backend (FastAPI)
This document outlines the step-by-step setup of the backend for the QA Portal project using FastAPI. It explains what was done, in what order, and why — to make the project understandable and maintainable.

___
### Date of developlent: 01.06.2025
## 1 Step - Initializing the project
### Project Structure

I created the backend/ folder with a nested app/ directory to hold all FastAPI logic.
I also added frontend/, postgres/, test-playwright/, cypress/ folders for future use.

> 🔵 Why?\
Separation of concerns – this structure makes import paths clean (e.g., from app.core.config import settings) and keeps backend isolated from frontend and tests.


## 2 Step – Create `.env.example`

Created a `.env.example` file at the project root to document required environment variables.

⚪ **Purpose**:
- Document which variables are needed (e.g., DB credentials, secret key).

🔵 **Why?**  
- Makes the project easier to clone, set up and run for other developers or in CI environments.

## 3 Step – `main.py` (FastAPI App Entry Point)

```python
from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(title="QA Portal", version="0.1.0")
app.include_router(router)
```

**⚪ Purpose:**
- Initializes the FastAPI application.
- Sets up Swagger UI metadata.
- Includes API routes from routes.py.

🔵 Why?\
+ This is the root of the backend — the file that Uvicorn runs.

## Step 4 – `api/routes.py` (Router & First Endpoint)

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}
```

**⚪ Purpose:**
- Defines an APIRouter object.
- Adds a simple GET /ping endpoint to verify the backend is responsive.

> 🔵 Why?\
It's a minimal health-check endpoint and confirms that the API is live.

## Step 5 – `core/config.py` (Environment Configuration)

```python
from pydantic import BaseSettings
class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
       env_file = ".env"

    settings = Settings()
 ```

**⚪ Purpose:**

- Loads environment variables from a .env file.
- Centralizes all config values (DB, JWT, etc.).

🔵 **Why?**\
- Keeps sensitive or environment-specific values outside the codebase, following the 12-factor app pattern.

## Step 6 – `core/database.py` (Async DB Connection)

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

⚪**Purpose**:

- Sets up a SQLAlchemy engine using asyncpg for PostgreSQL.
- Provides a reusable get_db() dependency to inject into route handlers.

>🔵**Why**?  
This makes database access consistent and testable, and works with FastAPI’s dependency injection system.

## Step 7 – Running the Backend

From the project root (web-app-project/), run:

```bash
uvicorn backend.app.main:app --reload
```

⚪**Purpose**:
- Start the FastAPI backend server locally with hot-reloading enabled.

>🔵**Why**?\
> This allows you to test endpoints in real time during development. The Swagger UI provides an interactive interface for API testing.

- --reload enables auto-restart on file changes.
- Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/ping

## Step 8 – First Commit
```bash
git commit -m "feat: initial FastAPI setup with config, DB, router and /ping endpoint"
```
⚪**Purpose**:
- Save the current working state of the backend setup with a clear commit message using Conventional Commits.

>🔵**Why**?\
Keeping small, descriptive commits improves code history, helps in debugging, and is a strong indicator of professional workflow (especially in portfolio projects).