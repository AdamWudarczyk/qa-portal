from fastapi import FastAPI
from backend.app.api.routes import router  # Import API routes

# Initialize the FastAPI app
app = FastAPI(
    title="QA Portal",       # Title for Swagger UI
    version="0.1.0"          # Version number shown in docs
)

# Include the API router under root path
# This allows endpoints defined in routes.py to be accessible
app.include_router(router)