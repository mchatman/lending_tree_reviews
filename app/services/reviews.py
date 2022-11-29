import re

from pydantic import HttpUrl

from app.services.web_scraper import WebScraperService


class ReviewsService:
    def __init__(self):
        self.web_scraper_service = WebScraperService()

    async def find_reviews(self, business_url: HttpUrl):
        reviews = []
        pages = await self.web_scraper_service.get_urls(business_url)

        for page in pages:
            reviews_elements = await self.web_scraper_service.find_page_elements(
                page, selector="div.mainReviews"
            )

            for element in reviews_elements:
                review_title = element.find("p.reviewTitle", first=True)
                review_content = element.find("p.reviewText", first=True)
                review_author = element.find("p.consumerName", first=True)
                review_star_rating = element.find("div.numRec", first=True)
                review_date_reviewed = element.find("p.consumerReviewDate", first=True)
                reviews.append(
                    {
                        "title": review_title.text,
                        "content": review_content.text,
                        "author": review_author.text.strip().split()[0],
                        "star_rating": re.search(
                            r"\d+", review_star_rating.text.strip()
                        ).group(),
                        "date_reviewed": review_date_reviewed.text.split("in ")[1],
                    }
                )

        return reviews
