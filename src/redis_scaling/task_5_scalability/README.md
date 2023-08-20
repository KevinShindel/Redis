# Create a Redis Cluster

## Create a minimum configuration file
````text
port 7000
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
````

# Create cluster with 3 primary shards and 3 replicas
# Create a 6 folders
````shell
mkdir 7000 7001 7002 7003 7004 7005
````
# Put the configuration file in each folder and change the port in each file to the corresponding folder name
````shell
cp redis.conf 7000
cp redis.conf 7001
cp redis.conf 7002
cp redis.conf 7003
cp redis.conf 7004
cp redis.conf 7005
````

# Run a cluster 
````shell
redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 \
127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 \
--cluster-replicas 1
````

# Add a new node to the cluster
````shell
mkdir 7006
cp redis.conf 7006
redis-server 7006/redis.conf
redis-cli --cluster add-node
````

# Find a node ID of the new node
````shell
redis-cli cluster nodes
redis-cli -p 7000 --cluster add-node 127.0.0.1:7007 127.0.0.1:7000 --cluster-slave --cluster-master-id 46a768cfeadb9d2aee91ddd882433a1798f53271
````
# Resharding
````shell
redis-cli --cluster reshard
redis-cli -p 7000 --cluster reshard 127.0.0.1:7000
````
 
# Rebalancing
````shell
redis-cli --cluster rebalance
redis-cli -p 7000 --cluster rebalance
````

# Show current cluster configuration
````shell
redis-cli --cluster info
redis-cli -p 7000 --cluster info
redis-cli -p 7000 cluster slots
````    
