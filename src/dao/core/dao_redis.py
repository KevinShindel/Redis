from redis import Redis

from redis_dao.shema.schema import KeySchema
from settings.client import get_redis_connection


class RedisDaoBase:

    def __init__(self, client: Redis = get_redis_connection(),
                 key_schema = KeySchema()):
        self.redis = client
        self.key_schema = key_schema
