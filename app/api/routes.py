from fastapi import APIRouter

from app.routers import reviews

api_router = APIRouter()
api_router.include_router(reviews.router)
