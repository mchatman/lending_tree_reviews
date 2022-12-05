from pydantic import BaseModel


class Reviews(BaseModel):
    title: str
    content: str
    author: str
    star_rating: str
    date_reviewed: str
