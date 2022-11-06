import os
from typing import Union

DEFAULT_DAO_KEY_PREFIX = 'redis-user-app'

REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_USERNAME = os.getenv('REDIS_USERNAME', None)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_PORT: Union[str, int] = os.getenv('REDIS_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)

REDIS_CLOUD_HOST = os.getenv('REDIS_CLOUD_HOST', '127.0.0.1')
REDIS_CLOUD_USERNAME = os.getenv('REDIS_CLOUD_USERNAME', None)
REDIS_CLOUD_PASS = os.getenv('REDIS_CLOUD_PASS', None)
REDIS_CLOUD_PORT = os.getenv('REDIS_CLOUD_PORT', 6379)
REDIS_CLOUD_DB = os.getenv('REDIS_CLOUD_DB', 0)
