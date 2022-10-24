import json
import socket
import time

from redis import ResponseError

from config.client import get_redis_connection


def write_to_data_warehouse(results):
    if len(results) > 0:
        print("Wrote " + json.dumps(results) + " to data warehouse.")


def main():
    stream_key = "stream:weather"
    group_name = "data_warehouse_writer"
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
        results = redis.xreadgroup(groupname=group_name, consumername=consumer_name, streams=stream_offsets, count=None, block=block_ms)
        write_to_data_warehouse(results)
        time.sleep(1)


if __name__ == '__main__':
    main()
