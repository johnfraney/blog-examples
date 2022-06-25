from typing import Iterator, Optional, TypedDict

from boto3.dynamodb.conditions import Key
from mypy_boto3_dynamodb.service_resource import Table

from news.type_guards import guard_news_item
from news.types import NewsItem


class PutNewsItemsResponse(TypedDict):
    saved_item_count: int


class NewsController:
    def __init__(self, dynamo_table: Table):
        self.dynamo_table = dynamo_table

    def get_newest_news_item(self) -> Optional[NewsItem]:
        newest_news_items = self.dynamo_table.query(
            KeyConditionExpression=Key("PK").eq("News"),
            ScanIndexForward=False,
            Limit=1,
        )["Items"]
        if not newest_news_items or not newest_news_items[0]:
            return None
        newest_item = guard_news_item(newest_news_items[0])
        return newest_item

    def put_items(self, items: Iterator[NewsItem]) -> PutNewsItemsResponse:
        saved_item_count = 0
        with self.dynamo_table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)
                saved_item_count += 1
        return {"saved_item_count": saved_item_count}
