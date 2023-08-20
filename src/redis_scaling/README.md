# RU301 - Running Redis at Scale

This repository contains files used in the exercises for the Redis University [RU301 Running Redis at Scale](https://university.redis.com/courses/ru301/) course.


# Redis command reference

### Connect to Redis

```
redis-cli -h <host> -p <port> -a <password>
```

### Run commands in a file

```
redis-cli -h <host> -p <port> -a <password> --eval <file>
redis-cli -h <host> -p <port> -a <password> --pipe <file>
```

### Run commands in a file and save output

``` 
redis-cli -h <host> -p <port> -a <password> MONITOR | tee <file>
```

### Run commands in a file and save output with timestamps

```
redis-cli -h <host> -p <port> -a <password> --raw MONITOR | awk '{ print strftime("%Y-%m-%d %H:%M:%S"), $0; fflush(); }' | tee <file>
```

### Run commands in a file and save output with timestamps and milliseconds

``` 
redis-cli -h <host> -p <port> -a <password> --raw MONITOR | awk '{ print strftime("%Y-%m-%d %H:%M:%S"), $0; fflush(); }' | sed -e 's/\([0-9][0-9]\) \([0-9][0-9]\) \([0-9][0-9]\)\.\([0-9][0-9][0-9]\)/\1 \2 \3 \4/' | tee <file>
```

# Redis-server configuration reference

### Redis-server configuration file

```
redis-server /path/to/redis.conf
```

# Work with Redis configuration due console

### Get configuration

```
redis-cli -h <host> -p <port> -a <password> CONFIG GET <parameter>
```

### Set configuration

```
redis-cli -h <host> -p <port> -a <password> CONFIG SET <parameter> <value>
```

## Get all configuration

```
redis-cli -h <host> -p <port> -a <password> CONFIG GET *
```

# Work with Redis clients

### Max number of clients

```
redis-cli -h <host> -p <port> -a <password> CONFIG GET maxclients
```

### Set max number of clients in config file

```
    maxclients 10000
```

### Set max volume of RAM in config file

usually 25% of RAM
```
    maxmemory 100mb
```


### Set read-only mode for replica

```
    replica-read-only yes
```

### Disable transparent huge pages on high load

```
    echo never > /sys/kernel/mm/transparent_hugepage/enabled
```

### Tuning kernel network stack for high-load connections

````text
vm.swappiness=0                       # turn off swapping
net.ipv4.tcp_sack=1                   # enable selective acknowledgements
net.ipv4.tcp_timestamps=1             # needed for selective acknowledgements
net.ipv4.tcp_window_scaling=1         # scale the network window
net.ipv4.tcp_congestion_control=cubic # better congestion algorithm
net.ipv4.tcp_syncookies=1             # enable syn cookies
net.ipv4.tcp_tw_recycle=1             # recycle sockets quickly
net.ipv4.tcp_max_syn_backlog=NUMBER   # backlog setting
net.core.somaxconn=NUMBER             # up the number of connections per port
net.core.rmem_max=NUMBER              # up the receive buffer size
net.core.wmem_max=NUMBER              # up the buffer size for all connections
````

## Persistence and Durability

### Snapshotting ( save 60 seconds 10000 keys changed )

```
    save 60 10000
```

### AOF ( appendonly yes )

```
    appendonly yes
```
