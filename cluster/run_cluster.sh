#!/bin/bash
mkdir cluster-test
cd cluster-test
echo "port 7000
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes" > redis.conf
mkdir 7000 7001 7002 7003 7004 7005
redis-cli --cluster create 127.0.0.1:7000 \
                           127.0.0.1:7001 \
                           127.0.0.1:7002 \
                           127.0.0.1:7003 \
                           127.0.0.1:7004 \
                           127.0.0.1:7005 \
                           --cluster-replicas 1
redis-cli --cluster fix localhost:7000
redis-server redis.conf
