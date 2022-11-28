from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from pydantic import HttpUrl

from app import schemas
from app.services.reviews import ReviewsService

router = InferringRouter()


@cbv(router)
class ReviewsListRouter:
    reviews_service = ReviewsService()

    @router.get("/reviews/{business_url:path}", response_model=schemas.Reviews)
    async def read_reviews(self, business_url: HttpUrl):
        """
        Retrieve all reviews.
        """
        reviews = await self.reviews_service.find_reviews(business_url)
        return reviews
