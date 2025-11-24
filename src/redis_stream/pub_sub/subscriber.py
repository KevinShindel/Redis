import json

from redis.client import PubSub

from src.dao.core.dao_redis import RedisDaoBase


class RedisSubscriber(RedisDaoBase):

    def __init__(self, channel='redis-channel'):
        super().__init__()
        self.channel = channel
        self.subscription = None

    def subscribe(self, **kwargs):
        self.subscription: PubSub = self.redis.pubsub()
        self.subscription.subscribe(kwargs.get('channel', self.channel))

    def get_message(self):
        response: dict = self.subscription.get_message()
        data = response['data']

        if isinstance(data, str):
            data = json.loads(data)
            return data

        return data

    def listen(self):
        yield from self.subscription.listen()


def main():    # pragma: no cover
    subscriber = RedisSubscriber()
    for d in iter(subscriber.listen()):
        print(d)


if __name__ == '__main__':
    main()  # pragma: no cover
