import redis


REDIS_URL = "redis://localhost:6379/"
BOOK_KEY = "ru204:book:666"
BOOK = {
    "author": "Kevin",
    "pages": 1000,
    "tags": ["codding", "python"],
    "sold": False
}


def main():
    client = redis.from_url(REDIS_URL)
    updated = client.json().set(BOOK_KEY, "$", BOOK)
    print(updated)
    data = client.json().get(BOOK_KEY, '$')
    print(data)
    client.json().set(BOOK_KEY.replace('666', '777'), '$', BOOK)
    # Task 1 - STRAPPEND
    client.json().strappend(BOOK_KEY, ' shindel', '$.author')
    data = client.json().get(BOOK_KEY, '$')
    print(data)
    # Task 2 - MGET
    mget_data = client.json().mget(['ru204:book:777', BOOK_KEY], '$.author')
    print(mget_data)
    # Task 3 - ARRINSERT
    # data = {"status": "maintenance", "stock_id": "10542_5"}
    data = 'epam'
    client.json().arrinsert(BOOK_KEY, '$.tags', 2, data)
    data = client.json().get(BOOK_KEY)
    print(data)


if __name__ == '__main__':
    main()
