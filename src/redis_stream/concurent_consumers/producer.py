import random
from time import sleep

from src.config.client import get_redis_connection


MEMBER_CNT = 3

STREAM_NAME = 'test_data'
GROUP = 'consumer_group'
redis = get_redis_connection()


def setup():
    global redis
    # redis = get_redis_connection()
    if not redis.exists(STREAM_NAME):
        # redis.delete(STREAM_NAME)
        redis.xgroup_create(STREAM_NAME, GROUP, mkstream=True)


def producer():
    client = get_redis_connection()
    idx = 0
    while True:
        data = {'n': idx}
        client.xadd(name=STREAM_NAME, fields=data)
        print('Item: %d added to %s' % (idx, STREAM_NAME))
        sleep(random.random() / MEMBER_CNT)
        idx += 1


if __name__ == '__main__':
    setup()
    producer()
