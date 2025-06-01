from fastapi import APIRouter

# Create a router object to define and group API endpoints
router = APIRouter()

# Simple health check endpoint
# Useful for checking if the backend is up and responding
@router.get("/ping")
async def ping():
    return {"message": "pong"}