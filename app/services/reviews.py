from pydantic import HttpUrl


class ReviewsService:
    async def find_reviews(self, business_url):
        return {"business_url": business_url}
