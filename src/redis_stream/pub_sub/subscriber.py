import json

from src.config.client import get_redis_connection


def main():
    client = get_redis_connection()
    channel = 'redis-channel'
    subscription = client.pubsub()
    subscription.subscribe(channel)
    while True:
        for msg in subscription.listen():
            data = msg['data']
            if isinstance(data, str):
                data = json.loads(data)
            print(f'Message: {data} accepted!')


if __name__ == '__main__':
    main()
