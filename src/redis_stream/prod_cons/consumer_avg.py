import json
import socket
import time

from redis import ResponseError

from src.config.client import get_redis_connection


def get_rolling_average(results):
    top_10_records = results[0][1][-10:]
    top_10_temp = list(map(lambda item: int(item[1]["temp_f"]), top_10_records))
    avg_temp = sum(top_10_temp) / len(top_10_temp)
    return avg_temp


def get_rolling_mean(results):
    top_10_records = results[0][1][-10:]
    top_10_temp = list(map(lambda item: int(item[1]["temp_f"]), top_10_records))
    sorted_temp = sorted(top_10_temp)
    if len(sorted_temp) % 2 == 0:
        middle = int(len(sorted_temp) / 2)
        m_1, m_2 = sorted_temp[middle - 1:middle + 1]
        mean = (m_1 + m_2) / 2
    else:
        middle = int((len(sorted_temp) - 1) / 2)
        mean = sorted_temp[middle]
    return mean


def write_to_data_warehouse(results):
    if len(results) > 0:
        print("Wrote " + json.dumps(results) + " to data warehouse.")
        print("Rolling Average: " + str(get_rolling_average(results)))
        print("Rolling Mean: " + str(get_rolling_mean(results)))


def main():
    stream_key = "stream:weather"
    group_name = "rolling_average_printer"
    consumer_name = "consumer-" + socket.gethostname() + "-a"
    block_ms = 5000
    stream_offsets = {stream_key: ">"}
    redis = get_redis_connection()

    if not redis.exists(stream_key):
        print(f"Stream {stream_key} does not exist.  Try running the producer first.")
        exit(0)

    try:
        redis.xgroup_create(stream_key, group_name)
    except ResponseError:
        print("Group already exists.")

    while True:
        results = redis.xreadgroup(group_name, consumer_name,
                                   stream_offsets, None, block_ms)
        write_to_data_warehouse(results)
        time.sleep(1)


if __name__ == '__main__':
    main()
