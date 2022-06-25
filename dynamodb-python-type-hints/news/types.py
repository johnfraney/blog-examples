from typing import Optional, TypedDict


class NewsItem(TypedDict):
    PK: str
    SK: str
    title: str
    description: Optional[str]
    published: str
    link: str
