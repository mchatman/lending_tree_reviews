import json

from app.services.reviews import ReviewsService

TEST_REVIEWS_1 = {
    "title": "Review Title 1",
    "content": "Review Content 1",
    "author": "Author 1",
    "star_rating": "1",
    "date_reviewed": "November 2022",
}

TEST_REVIEWS_2 = {
    "title": "Review Title 2",
    "content": "Review Content 2",
    "author": "Author 2",
    "star_rating": "2",
    "date_reviewed": "November 2022",
}


def test_list_reviews(test_app, monkeypatch):
    class MockReviewsService:
        async def find_reviews(self, business_url):
            assert business_url == "https://example.com"
            return [TEST_REVIEWS_1, TEST_REVIEWS_2]

    monkeypatch.setattr(
        ReviewsService,
        "find_reviews",
        MockReviewsService.find_reviews,
    )

    response = test_app.get("/reviews/https://example.com")
    assert response.status_code == 200

    reviews = json.loads(response.content)
    # reviews = document["data"]
    assert len(reviews) == 2
    assert reviews[0]["title"] == TEST_REVIEWS_1["title"]
    assert reviews[0]["content"] == TEST_REVIEWS_1["content"]
    assert reviews[0]["author"] == TEST_REVIEWS_1["author"]
    assert reviews[0]["star_rating"] == TEST_REVIEWS_1["star_rating"]
    assert reviews[1]["title"] == TEST_REVIEWS_2["title"]
    assert reviews[1]["content"] == TEST_REVIEWS_2["content"]
    assert reviews[1]["author"] == TEST_REVIEWS_2["author"]
    assert reviews[1]["star_rating"] == TEST_REVIEWS_2["star_rating"]
