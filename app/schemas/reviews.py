from pydantic import BaseModel, HttpUrl


class Reviews(BaseModel):
    business_url: HttpUrl
