import json
import unittest

from src.redis_stream.pub_sub.publisher import RedisPublisher
from src.redis_stream.pub_sub.subscriber import RedisSubscriber


class TestSubscriber(unittest.TestCase):

    def setUp(self) -> None:
        self.channel = 'redis-channel'
        self.publisher = RedisPublisher(channel=self.channel)
        self.subscriber = RedisSubscriber(channel=self.channel)
        self.subscriber.redis.xdel(self.channel, '*')

    def test_get_msg(self):
        expected = {'data': 'message'}
        expected_connected = 1
        self.subscriber.subscribe()
        self.publisher.publish(message=expected)
        actual_connected = self.subscriber.get_message()
        actual = self.subscriber.get_message()

        self.assertEqual(expected_connected, actual_connected)
        self.assertEqual(actual, expected)

    def test_listen(self):
        expected = {'data': 'message'}
        expected_connected = 1
        self.subscriber.subscribe()
        self.publisher.publish(message=expected)

        actual_connected = next(self.subscriber.listen())['data']
        actual = json.loads(next(self.subscriber.listen())['data'])

        self.assertEqual(expected_connected, actual_connected)
        self.assertEqual(actual, expected)

    def tearDown(self) -> None:
        self.publisher.redis.xdel(self.channel, '*')
