import httpx


def handler(event, context):
    response = httpx.get(
        "http://stapi.co/api/v1/rest/character/search",
    )
    response_as_dict = response.json()
    characters = response_as_dict.get("characters")
    return characters


if __name__ == "__main__":
    print(handler(None, None))
