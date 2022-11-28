from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/reviews/{business_url}", response_model=schemas.Reviews)
async def list_reviews(business_url: str):
    return {"business_url": business_url}
