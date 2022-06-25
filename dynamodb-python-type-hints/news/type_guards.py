from typing import Any, Optional
from news.types import NewsItem


def guard_optional_string(value: Any) -> Optional[str]:
    if value is None:
        return value
    if isinstance(value, str):
        return value
    raise Exception(
        f"Received unexpected type: "
        f"expected Optional[str] but received value of type {type(value)}: {value}"
    )


def guard_string(value: Any) -> str:
    if isinstance(value, str):
        return value

    raise Exception(
        f"Received unexpected type: "
        f"expected str but received value of type {type(value)}: {value}"
    )


def guard_news_item(item: dict) -> NewsItem:
    return NewsItem(
        PK=guard_string(item.get("PK")),
        SK=guard_string(item.get("SK")),
        title=guard_string(item.get("title")),
        description=guard_optional_string(item.get("description")),
        published=guard_string(item.get("published")),
        link=guard_string(item.get("link")),
    )
