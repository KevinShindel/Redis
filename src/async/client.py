from aioredis import Redis as AsyncRedis

from src.config.common import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD, REDIS_USERNAME


async def get_async_redis_connection():
    """ ASYNC version Redis client using aioredis library"""
    client = await AsyncRedis(host=REDIS_HOST,
                              port=REDIS_PORT,
                              db=REDIS_DB,
                              password=REDIS_PASSWORD,
                              username=REDIS_USERNAME,
                              decode_responses=True)
    return client
