import pytest
from news.type_guards import guard_news_item, guard_string, guard_optional_string
from news.types import NewsItem


def test_guard_string_with_string():
    assert guard_string("string!") == "string!"


def test_guard_string_without_string():
    with pytest.raises(Exception) as exception_info:
        guard_string(100)
    assert exception_info.match("Received unexpected type")


def test_guard_optional_string_with_string():
    assert guard_optional_string("string!") == "string!"


def test_guard_optional_string_with_none():
    assert guard_optional_string(None) is None


def test_guard_optional_string_with_int():
    with pytest.raises(Exception) as exception_info:
        guard_optional_string(100)
    assert exception_info.match("Received unexpected type")


def test_guard_news_item_valid():
    assert guard_news_item(
        {
            "PK": "News",
            "SK": "AMD#2022-06-25#news-slug",
            "title": "Interesting News",
            "published": "2022-06-25",
            "link": "https://amd.com/",
        }
    )


def test_guard_news_item_invalid():
    with pytest.raises(Exception) as exception_info:
        guard_news_item({})
    assert exception_info.match("Received unexpected type")
