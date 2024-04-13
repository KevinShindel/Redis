from redis import Redis
from common import *


def get_redis_connection():
    return Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        socket_timeout=REDIS_SOCKET_TIMEOUT,
        socket_connect_timeout=REDIS_SOCKET_CONNECT_TIMEOUT,
        socket_keepalive=REDIS_SOCKET_KEEPALIVE,
        ssl=REDIS_SSL,
        decode_responses=True,
        encoding='utf-8',
    )


def test_get_redis_connection():
    conn = get_redis_connection()
    print(conn.ping())
    assert conn is not None
    conn.close()


if __name__ == '__main__':
    test_get_redis_connection()
