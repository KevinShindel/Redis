import json
import random
import time

from src.config.client import get_redis_connection

idx = 0

class Measurement:

    def __init__(self):
        self.postal_codes = [94016, 80014, 60659, 10011]
        self.current_temp = 50
        self.max_temp = 100
        self.min_temp = 0

    def get_next(self):
        if random.random() >= 0.5:
            if self.current_temp + 1 <= self.max_temp:
                self.current_temp += 1
        elif self.current_temp - 1 >= self.min_temp:
            self.current_temp -= 1
        global idx
        idx += 1

        return {'idx': idx, 'postal_code': random.choice(self.postal_codes), 'temp_f': self.current_temp}


def main():
    stream_key = "stream:weather"
    measurement = Measurement()
    redis = get_redis_connection()

    while True:
        entry = measurement.get_next()
        id = redis.xadd(name=stream_key, fields=entry, id='*')
        print("Wrote " + json.dumps(entry) + " with ID " + id)
        time.sleep(1)


if __name__ == '__main__':
    main()
