# Need running Redis primary server and replica from previous task

# 1. Create sentinel config file sentinel_1.conf
````text
port 5000
sentinel monitor myprimary 127.0.0.1 6379 2
sentinel down-after-milliseconds myprimary 5000
sentinel failover-timeout myprimary 60000
sentinel auth-pass myprimary a_strong_password
````

# 2. Create sentinel config file sentinel_2.conf ( just change port to 5001 )
# 3. Create sentinel config file sentinel_3.conf ( just change port to 5002 )
# 4. Run sentinels in separate terminals
````bash
redis-server sentinel_1.conf --sentinel
redis-server sentinel_2.conf --sentinel
redis-server sentinel_3.conf --sentinel
````
# 5. Check sentinels status
````text
# Provides information about the Primary
SENTINEL master myprimary

# Gives you information about the replicas connected to the Primary
SENTINEL replicas myprimary

# Provides information on the other Sentinels
SENTINEL sentinels myprimary

# Provides the IP address of the current Primary
SENTINEL get-master-addr-by-name myprimary
````

# 6. Kill primary server
````bash
redis-cli -p 6379 DEBUG sleep 30
````

# 7. Check sentinels status
````text
# Provides information about the Primary
SENTINEL get-master-addr-by-name myprimary
````

