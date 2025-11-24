from redis import Redis

from src.config.client import get_redis_connection
from src.dao.shema.schema import KeySchema


class RedisDaoBase:

    def __init__(self, client: Redis = get_redis_connection(),
                 key_schema=KeySchema()):
        self.redis = client
        self.key_schema = key_schema
