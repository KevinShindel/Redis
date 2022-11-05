import random
import time
from multiprocessing import Process
from threading import Thread
from typing import List, Tuple

from src.config.client import get_redis_connection
from src.redis_stream.concurent_consumers.producer import setup, GROUP, STREAM_NAME

MEMBER_CNT = 3


def prime(a):
    time.sleep(random.random())
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))


def consumer_func(consumername):
    redis = get_redis_connection()
    timeout = 100
    retries = 0
    recovery = True
    from_id = '0'

    while True:
        count = random.randint(1, 5)
        reply = redis.xreadgroup(groupname=GROUP,
                                 consumername=consumername,
                                 streams={STREAM_NAME: from_id},
                                 count=count, block=timeout)
        if not reply:
            if retries == 5:
                print(f'{consumername}: Waited long enough - bye bye ...')
                break
            retries += 1
            timeout *= 2
            continue

        timeout = 100
        retries = 0

        if recovery:

            if reply[0][1]:
                print(f'{consumername}: Recovering pending messages...')
            else:
                recovery = False
                from_id = '>'
                continue
        for _, messages in reply:
            for message in messages:
                n = int(message[1]['n'])
                if prime(n):
                    print(f'{consumername}: {n} is a prime number')
                redis.xack(STREAM_NAME, GROUP, message[0])


def new_consumer(consumer_name: str):
    consumer = Process(target=consumer_func, args=(consumer_name,))
    consumer.start()
    return consumer_name, consumer


def chaos_func(consumers_list: List[Tuple[str, Process]]):
    while True:
        # Roll a pair of dice to determine the verdict
        if random.randint(2, 12) == 2:
            # And another dice to find the victim
            idx = random.randrange(0, stop=len(consumers_list))
            consumer_name = consumers_list[idx][0]
            consumer = consumers_list[idx][1]
            consumer.terminate()
            consumers_list[idx] = new_consumer(consumer_name)
            print(f'CHAOS: Restarted {consumer_name}')
        time.sleep(random.random())


if __name__ == '__main__':
    setup()

    consumers = []
    for i in range(MEMBER_CNT):
        name = f'BOB-{i}'
        consumers.append(new_consumer(name))
    Thread(target=chaos_func, args=(consumers, )).start()
