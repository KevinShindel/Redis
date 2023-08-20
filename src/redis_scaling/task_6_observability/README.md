# Redis Observability module

## Get redis metrics info   
```shell
> INFO
```

## Get redis info of clients
```shell
> CLIENT LIST
```

````shell
> INFO CLIENTS
````

## Warning table
| Warning | Description |
| --- | --- |
| `maxmemory` | The maxmemory warning is triggered when the memory used by Redis is greater than the maxmemory configuration. |
| `maxmemory_policy` | The maxmemory_policy warning is triggered when the memory used by Redis is greater than the maxmemory configuration. |
| `maxmemory_samples` | The maxmemory_samples warning is triggered when the memory used by Redis is greater than the maxmemory configuration. |
| `maxmemory_eviction` | The maxmemory_eviction warning is triggered when the memory used by Redis is greater than the maxmemory configuration. |
| `maxmemory_human` | The maxmemory_human warning is triggered when the memory used by Redis is greater than the maxmemory configuration. |
| `maxmemory_policy` | The maxmemory_policy warning is triggered when the memory used by Redis is greater than the maxmemory configuration. |
| `uptime_in_seconds` |	< 300 seconds: to ensure the server is staying up |
| `connected_clients` |	< minimum number of expected application connections|
| `master_link_down_since` | > 30 seconds: replication should be operational |
| `rdb_last_save_time` | 	> maximum acceptable interval without taking a snapshot |

## Redis latency metrics

````shell
Continuously sample latency

$ redis-cli --latency
min: 1, max: 17, avg: 4.03 (927 samples) # latency in milliseconds
````

````shell
$ redis-cli --latency-history -i 60 
min: 1, max: 30, avg: 4.84 (328 samples) -- 60 seconds range
````

````shell
$ redis-cli --latency-history -i 60 --csv
13,13,13.00,1
5,13,9.00,2
3,13,7.00,3
3,13,6.00,4
3,13,5.60,5
2,13,5.00,6
2,13,5.43,7
2,13,5.62,8
2,13,5.22,9
2,13,5.00,10
1,13,4.64,11
````

## Redis stats options

````text
$ redis-cli --stat 
------- data ------ --------------------- load -------------------- - child -
keys       mem      clients blocked requests            connections
4          9.98M    51      0       8168035 (+0)        4132
4          9.98M    51      0       8181542 (+13507)    4132
4          9.98M    51      0       8196100 (+14558)    4132
4          9.98M    51      0       8209794 (+13694)    4132
4          9.98M    51      0       8223420 (+13626)    4132
4          9.98M    51      0       8236624 (+13204)    4132
4          9.98M    51      0       8251376 (+14752)    4132
4          9.98M    51      0       8263417 (+12041)    4182
4          9.98M    51      0       8276781 (+13364)    4182
4          9.90M    51      0       8289693 (+12912)    4182
````

## Redis memory stats

````text
127.0.0.1:6379> memory stats
 1) "peak.allocated"
 2) (integer) 11912984
 3) "total.allocated"
 4) (integer) 8379168
 5) "startup.allocated"
 6) (integer) 5292168
 7) "replication.backlog"
 8) (integer) 0
 9) "clients.slaves"
10) (integer) 0
11) "clients.normal"
12) (integer) 16986
13) "aof.buffer"
14) (integer) 0
````

## Latency monitoring

````shell
127.0.0.1:6379> CONFIG SET latency-monitor-threshold 10 # 10 milliseconds 
````

````shell
127.0.0.1:6379> CONFIG SET latency-monitor-threshold 0 # disable
````

### The latency data can be viewed using the LATENCY command with it's subcommands:
- LATENCY LATEST - latest samples for all events
- LATENCY HISTORY - latest time series for a given event
- LATENCY RESET - resets the time series data
- LATENCY GRAPH - renders an ASCII-art graph
- LATENCY DOCTOR - analysis report

## Create Redis Benchmark 

- Create Redis server with docker:
````shell
$ docker run --rm  -d -n redis_server --network host redis 
````
- Run the following command to create a benchmark with 100000 requests and 10 concurrent clients:

````shell
$docker exec -it redis_server redis-benchmark -n 100000 -c 10
````

- Check metrics via separate terminal:
````shell
$ docker exec -it redis_server redis-cli --stat
````
- Check latency via separate terminal:
````shell
$ docker exec -it redis_server redis-cli --latency
````
- Check latency history via separate terminal:
````shell
$ docker exec -it redis_server redis-cli --latency-history -i 1
````
- Check hit ratio via separate terminal:
````shell
$ docker exec -it redis_server redis-cli --stat  | grep keyspace 
````
- Check workload via separate terminal:
````shell
$ docker exec -it redis_server redis-cli --stat  | grep | egrep "^total_" 
````

# Identify issues

### Availability
````text
The redis server will respond to the PING command when running properly:

$ redis-cli -h redis.example.com -p 6379 PING
PONG
````

### Slowlog
````text
Redis Slow Log is a system to log queries that exceed a specific execution time which does not include I/0 operations like client communication. It is enabled by default with two configuration parameters.

slowlog-log-slower-than 1000000
This indicates if there is an execution time longer than the time in microseconds, in this case one second, it will be logged. The slowlog can be disabled using a value of -1. It can also be set to log every command with a value of 0.

slowlog-max-len 128
This sets the length of the slow log. When a new command is logged the oldest one is removed from the queue.

These values can also be changed at runtime using the CONFIG SET command.

You can view the current length of the slow log using the LEN subcommand:

redis.cloud:6379> slowlog len
(integer) 11
Entries can be pulled off of the slow log using the GET subcommand.

redis.cloud:6379> slowlog get 2
1) 1) (integer) 10
   2) (integer) 1616372606
   3) (integer) 600406
   4) 1) "debug"
      2) "sleep"
      3) ".6"
   5) "172.17.0.1:60546"
   6) ""
2) 1) (integer) 9
   2) (integer) 1616372602
   3) (integer) 600565
   4) 1) "debug"
      2) "sleep"
      3) ".6"
   5) "172.17.0.1:60546"
   6) ""
The slow log can be reset using the RESET subcommand.

redis.cloud:6379> slowlog reset
OK
redis.cloud:6379> slowlog len
(integer) 0
````

### Scanning keys

````text
There are a few options that can be passed to redis-cli that will trigger a keyspace analysis. They use the SCAN command so they should be safe to run without impacting operations. You can see in the output of all of them there is a throttling option if needed.

Big Keys: This option will scan the dataset for big keys and provide information about them.

$ redis-cli --bigkeys 

# Scanning the entire keyspace to find biggest keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Biggest string found so far '"counter:__rand_int__"' with 6 bytes
[00.00%] Biggest hash   found so far '"myhash"' with 1 fields
[00.00%] Biggest list   found so far '"mylist"' with 200000 items

-------- summary -------

Sampled 4 keys in the keyspace!
Total key length in bytes is 48 (avg len 12.00)

Biggest   list found '"mylist"' has 200000 items
Biggest   hash found '"myhash"' has 1 fields
Biggest string found '"counter:__rand_int__"' has 6 bytes

1 lists with 200000 items (25.00% of keys, avg size 200000.00)
1 hashs with 1 fields (25.00% of keys, avg size 1.00)
2 strings with 9 bytes (50.00% of keys, avg size 4.50)
0 streams with 0 entries (00.00% of keys, avg size 0.00)
0 sets with 0 members (00.00% of keys, avg size 0.00)
0 zsets with 0 members (00.00% of keys, avg size 0.00)
Mem Keys: Similarly to big keys mem keys will look for the biggest keys but also report on the average sizes.

$ redis-cli --memkeys

# Scanning the entire keyspace to find biggest keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Biggest string found so far '"counter:__rand_int__"' with 62 bytes
[00.00%] Biggest string found so far '"key:__rand_int__"' with 63 bytes
[00.00%] Biggest hash   found so far '"myhash"' with 86 bytes
[00.00%] Biggest list   found so far '"mylist"' with 860473 bytes

-------- summary -------

Sampled 4 keys in the keyspace!
Total key length in bytes is 48 (avg len 12.00)

Biggest   list found '"mylist"' has 860473 bytes
Biggest   hash found '"myhash"' has 86 bytes
Biggest string found '"key:__rand_int__"' has 63 bytes

1 lists with 860473 bytes (25.00% of keys, avg size 860473.00)
1 hashs with 86 bytes (25.00% of keys, avg size 86.00)
2 strings with 125 bytes (50.00% of keys, avg size 62.50)
0 streams with 0 bytes (00.00% of keys, avg size 0.00)
0 sets with 0 bytes (00.00% of keys, avg size 0.00)
0 zsets with 0 bytes (00.00% of keys, avg size 0.00)
Hot Keys: The hot keys scan is only available when the maxmemory-policy is set to volatile-lfu or allkeys-lfu.
 If you need to identity hot keys you can add this argument to redis-cli.

$ redis-cli --hotkeys

# Scanning the entire keyspace to find hot keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Hot key '"key:__rand_int__"' found so far with counter 37

-------- summary -------

Sampled 5 keys in the keyspace!
hot key found with counter: 37  keyname: "key:__rand_int__"
Monitor: The MONITOR command allows you to see a stream of every command running against your Redis instance.

127.0.0.1:6379 > monitor
OK
1616541192.039933 [0 127.0.0.1:57070] "PING"
1616541276.052331 [0 127.0.0.1:57098] "set" "user:2398423hu" "KutMo"
Note: because MONITOR streams back all commands, its use comes at a cost. It has been known to reduce performance by up to 50% so use with caution!
````

### Setting up and using the Redis Log File

````text
The Redis log file is the other important log you need to be aware of. It contains useful information for troubleshooting configuration and deployment errors. If you don't configure Redis logging, troubleshooting will be significantly harder.

Redis has four logging levels, which you can configure directly in redis.conf file.

Log Levels:

WARNING
NOTICE
VERBOSE
DEBUG
Redis also supports sending the log files to a remote logging server through the use of syslog.

Remote logging is important to many security professionals. These remote logging servers are frequently used to monitor security events and manage incidents. These centralized log servers perform three common functions: ensure the integrity of your log files, ensure that logs are retained for a specific period of time, and to correlate logs against other system logs to discover potential attacks on your infrastructure.

Let's set up logging on our Redis deployment. First we'll open our redis.conf file

$ sudo vi /etc/redis/redis.conf
The redis.conf file has an entire section dedicated to logging.

First, find the logfile directive in the redis.conf file. This will allow you to define the logging directory. For this example lets use /var/log/redis/redis.log.

If you'd like to use a remote logging server, then you'll need to uncomment the lines syslog-enabled, syslog-ident and syslog-facility, and ensure that syslog-enabled is set to yes.

Next, we'll restart the Redis server.

You should see the log events indicating that Redis is starting.

$ sudo tail -f /var/log/redis/redis.log
And next let's check that we are properly writing to syslog. You should see these same logs.

$ less /var/log/syslog | grep redis
Finally, you’ll need to send your logs to your remote logging server to ensure your logs will be backed up to this server. To do this, you’ll also have to modify the rsyslog configuration. This configuration varies depending on your remote logging server provider.
````