import unittest

from src.redis_stream.pub_sub.publisher import RedisPublisher


class TestRedisPublisher(unittest.TestCase):

    def setUp(self) -> None:
        self.publisher = RedisPublisher()

    def test_publish_message(self):
        message = {'field': 'data'}
        response = self.publisher.publish(message=message)
        self.assertFalse(response)
