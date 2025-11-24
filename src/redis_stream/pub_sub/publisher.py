import json
import random
import time

from src.dao.core.dao_redis import RedisDaoBase


class RedisPublisher(RedisDaoBase):

    def __init__(self, channel='redis-channel'):
        super().__init__()
        self.channel = channel

    def publish(self, **kwargs):
        pipeline = kwargs.get('pipeline', self.redis)
        channel = kwargs.get('channel', self.channel)
        is_published = pipeline.publish(channel=channel, message=json.dumps(kwargs['message']))
        return bool(is_published)


def main():  # pragma: no cover
    publisher = RedisPublisher()
    channel = 'redis-channel'
    for idx in range(100):
        secs = random.uniform(0.1, 2.0)
        time.sleep(secs)
        message = {'data': f'value_{idx}'}
        publisher.publish(channel=channel, message=message)
        print(f'[{idx}] Message: {message} hase published')


if __name__ == '__main__':
    main()   # pragma: no cover
