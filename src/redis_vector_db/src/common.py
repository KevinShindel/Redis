from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

REDIS_USER = getenv("REDIS_USER", "redis")
REDIS_PASSWORD = getenv("REDIS_PASSWORD", "redis")
REDIS_HOST = getenv("REDIS_HOST", "localhost")
REDIS_PORT = getenv("REDIS_PORT", 6379)
REDIS_DB = getenv("REDIS_DB", 0)
REDIS_SOCKET_TIMEOUT = getenv("REDIS_SOCKET_TIMEOUT", 0.1)
REDIS_SOCKET_CONNECT_TIMEOUT = getenv("REDIS_SOCKET_CONNECT_TIMEOUT", 0.1)
REDIS_SOCKET_KEEPALIVE = getenv("REDIS_SOCKET_KEEPALIVE", True)
REDIS_SSL = getenv("REDIS_SSL", False)
