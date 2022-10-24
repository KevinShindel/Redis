from redis import Redis

from config.common import REDIS_HOST, REDIS_USERNAME, REDIS_PASSWORD, REDIS_DB


def get_cluster_redis_connection(hostname=REDIS_HOST,
                                 port=7000,
                                 username=REDIS_USERNAME,
                                 password=REDIS_PASSWORD,
                                 db=REDIS_DB):
    """ cluster Redis client using redis client """
    client_kwargs = {
        "host": hostname,
        "port": port,
        "decode_responses": True,
        "db": db
    }
    if password:
        client_kwargs["password"] = password
    if username:
        client_kwargs["username"] = username
        return Redis(**client_kwargs)
