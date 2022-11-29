from pydantic import HttpUrl
from requests_html import HTMLSession


class WebScraperService:
    def __init__(self):
        self.session = HTMLSession()

    async def get_pages(self, index_page: HttpUrl):
        pages = []
        response = self.session.get(index_page)

        for html in response.html:
            pages.append(html.url)

        return pages

    async def find_page_elements(
        self,
        url: HttpUrl,
        selector: str = None,
        first: bool = False,
    ):
        response = self.session.get(url)
        elements = response.html.find(selector, first=first)

        return elements

    async def find_page_element(self, url: HttpUrl, selector: str = None):
        return await self.find_page_elements(url, selector, first=True)
