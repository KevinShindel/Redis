import random
import time
import json

from src.config.client import get_redis_connection


def main():
    client = get_redis_connection()
    channel = 'redis-channel'
    for idx in range(100):
        secs = random.uniform(0.1, 1.0)
        time.sleep(secs)
        message = {'data': f'value_{idx}'}
        client.publish(channel=channel, message=json.dumps(message))
        print(f'[{idx}] Message: {message} hase published')


if __name__ == '__main__':
    main()
