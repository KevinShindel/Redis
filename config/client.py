import urllib.parse

from redis import Redis


def get_redis_connection():
    url_schema = urllib.parse.urlparse('redis://localhost:6379')
    client = Redis(host=url_schema.hostname,
                   port=url_schema.port,
                   password=url_schema.password,
                   username=url_schema.username,
                   decode_responses=True, encoding="utf8")
    return client
