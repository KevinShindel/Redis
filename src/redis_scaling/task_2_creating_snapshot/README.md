# Create a folder named task_2_creating_snapshot
# Create a Redis config file named redis.conf
# Modify the config file to set the snapshotting frequency to 60 seconds
```
dbfilename my_backup_file.rdb
save 20 3
```

# Run the Redis server with the config file
````shell
docker run -d --name redis-server -v ./redis.conf:/usr/local/etc/redis/ -p 6379:6379 redis redis-server /usr/local/etc/redis/redis.conf
````
````shell
docker build -t redis-server .
docker run -d --name redis-server -p 6379:6379 redis-server
````

# Run redis-cli to connect to the server
````shell
docker exec -it redis-server redis-cli
````

# Run commands to set some keys
```
127.0.0.1:6379> SET a 1
127.0.0.1:6379> SET b 2
127.0.0.1:6379> SET c 3
```

# Check AOF (AOF contains only final state of the database)
````shell
docker exec -it redis-server cat /data/appendonly.aof
````

# Set AOF in shell
````shell
CONFIG SET appendonly yes
CONFIG SET appendfsync always
````

# Write changes 
````shell
CONFIG REWRITE
````

# Restart Redis server and check data persistence
````shell
docker restart redis-server
docker exec -it redis-server redis-cli
````

````shell
SCAN 0
````

# High Availability

# Create a folder named task_3_high_availability

# Create a main Redis server with the config file named primary.conf and expose port 6379
````shell
docker run -d --name redis-primary -v ./primary.conf:/usr/local/etc/redis/redis.conf -p 6379:6379 redis redis-server /usr/local/etc/redis/redis.conf
````
# Create a replica Redis server with the config file named replica.conf and expose port 6380
````shell
docker run -d --name redis-replica -v ./replica.conf:/usr/local/etc/redis/redis.conf -p 6380:6379 redis redis-server /usr/local/etc/redis/redis.conf
````
# Run redis-cli to connect to the server
````shell
docker exec -it redis-primary redis-cli -p 6380
````
# Run the command to check the replication status
````shell
INFO replication
````

# Connect to replica server and run the command to check the replication status
````shell
docker exec -it redis-replica redis-cli
INFO replication
````


# Run the Redis server with the config file
````shell   
docker run -d --name redis-server -v ./redis.conf:/usr/local/etc/redis/redis.conf -p 6379:6379 redis redis-server /usr/local/etc/redis/redis.conf
````
# Run redis-cli to connect to the server
````shell   
docker exec -it redis-server redis-cli
````

# Execute command on primary server

````shell
SET foo bar
````

# Execute command on replica server
````shell
GET foo
````
