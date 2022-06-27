from typing import TypedDict


class NewsItem(TypedDict):
    PK: str
    SK: str
    title: str
    description: str | None
    published: str
    link: str
