from fastapi import APIRouter

router = APIRouter()


@router.get("/reviews/{business_url}")
async def list_reviews(business_url: str):
    return {"business_url": business_url}
