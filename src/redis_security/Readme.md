## Installing Redis Securely

````shell
sudo apt-get update -y
sudo apt install build-essential tcl -y
sudo apt install tcl-tls libssl-dev -y
sudo adduser --system --group --no-create-home redis
sudo mkdir /var/lib/redis
sudo chown redis:redis /var/lib/redis
sudo chmod 770 /var/lib/redis
sudo mkdir /var/log/redis
sudo touch /var/log/redis/redis.log
sudo chmod 660 /var/log/redis
sudo chmod 640 /var/log/redis/redis.log
````

````shell
cd /tmp
wget https://download.redis.io/redis-stable.tar.gz
wget https://download.redis.io/redis-stable.tar.gz.SHA256SUM
cat redis-stable.tar.gz.SHA256SUM
sha256sum redis-stable.tar.gz
tar -xzvf redis-stable.tar.gz
cd redis-stable
sudo make BUILD_TLS=yes install
````

````shell
sudo mkdir /etc/redis
sudo cp /tmp/redis-stable/redis.conf /etc/redis
sudo chown -R redis:redis /etc/redis
sudo chown 640 /etc/redis/redis.conf
sudo runuser -u redis /usr/local/bin/redis-server /etc/redis/redis.conf &
````

## Basic Redis Security

````shell
sed -i 's/protected-mode yes/protected-mode no/g' /etc/redis/redis.conf
sed -i 's/bind 127.0.0.1/# bind 127.0.0.1/g' /etc/redis/redis.conf
````

## Basic Authentication

````shell
echo 'user default on >your_secret_password allcommands allkeys' >> /etc/redis/redis.conf
````

````shell
redis-cli AUTH default your_secret_password
redis-cli PING
````

## Securing Redis Client Code
## Disaster Recovery and Availability

### Save Configurations
````shell
> config set dbfilename rdb.rdb # You can set the filename by setting the dbfilename.
> config set dir /var/lib/redis # And then the directory by setting the dir.
> config set save "900 1 300 10 60 1000" # Lastly, we need to define a save policy.  In this example, a snapshot will be taken if one key is changed every 900 seconds, if 10 keys are changed within 300 seconds or if 1000 keys are changed within 60 seconds.
````

### Append-only Files
````shell
config set appendonly yes # First turn on appendonly mode by setting it to yes. Append-only is turned off by default.
> config set appendfsync always # We’re going to set this one to always because our application has a low data loss tolerance.
> config set appendfsync everysec  # This policy balances performance and durability and should be used when minimal data loss is acceptable in the event of a failure
> config set appendfsync no  # This policy favors performance over durability and will provide some, although minimal performance enhancements over fsync everysec
````

## Access Control List
Documentation <a href="https://redis.io/docs/management/security/acl/">Link</a>
Commands <a href="https://redis.io/commands/?group=server">Link</a>
### List all users
````shell
redis:6379> ACL LIST
1) "user default on nopass ~* &* +@all"
redis:6379>                            
````

### Create user with Read-only rules with specified keys [cached:] and hashed password [secret]
````shell
ACL SETUSER alice on #2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b ~cached:* +get
````

### Create admin profile
````shell
ACL SETUSER kevin on #2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b +@admin
````

### Create application profile with read-write permission only with cache: key-space
````shell
ACL SETUSER cache_service on #2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b +set +get ~cache:*
````

### Get user information
````shell
> ACL GETUSER alice
````

## Redis logging

### Redis comes with two types of logs relevant to security:
- the ACL log
- Redis server log files.

The ACL log is stored in memory, in Redis itself. By default, the log stores 128 entries, but this is configurable.

We can call ACL LOG to view these failed access attempts.

````shell
> ACL LOG
````

Since the ACL log is stored in memory, there are two ways to limit it: resetting the log or setting a maximum length.
To clear the log, you can call the ACL LOG RESET command:

````shell
> ACL LOG RESET
````

### To set a maximum length, you can set the acllog-max-len directive in the redis.conf file:
````shell
acllog-max-len 10
````

### Setting up and using the Redis Log File

The Redis log file is the other important log you need to be aware of. The Redis log file contains useful information for troubleshooting errors configuration and deployment errors. If you don't configure Redis logging, troubleshooting will be significantly harder.

Redis has four logging levels, which you can configure directly in redis.conf file.

Log Levels:
- WARNING
- NOTICE
- VERBOSE
- DEBUG

Let's set up logging on our Redis deployment. First we'll open our redis.conf file

$ sudo vi /etc/redis/redis.conf
The redis.conf file has an entire section dedicated to logging.

First, find the logfile directive in the redis.conf file. This will allow you to define the logging directory. For this example lets use /var/log/redis/redis.log.

If you'd like to use a remote logging server, then you'll need to uncomment the lines syslog-enabled, syslog-ident and syslog-facility, and ensure that syslog-enabled is set to yes.

Next, we'll restart the Redis server.

## TLS encryption channel

### Prepare keys
````shell
openssl genrsa -out redis.key 2048
openssl req -new -sha256 -nodes -sha256 -key redis.key
mv ca.crt /usr/local/share/ca-certificates
mv ca.key /etc/ssl/private
mv redis.key /etc/ssl/private
mv redis.crt /etc/ssl 
update-ca-certificates

chown redis:redis /etc/ssl/private/*.key
chmod 400 /etc/ssl/private/*.key
chown redis:redis /usr/local/share/ca-certificates/ca.crt
chown redis:redis /etc/ssl/redis.crt
chmod 644 /usr/local/share/ca-certificates/ca.crt
chmod 644 /etc/ssl/redis.crt
````

### prepare redis.conf

````shell
port 0
tls-port 6379

tls-cert-file /etc/ssl/redis.crt
tls-key-file /etc/ssl/private/redis.key
tls-ca-cert-file /usr/local/share/ca-certificates/ca.crt
tls-auth-clients no
tls-protocols "TLSv1.2 TLSv1.3"
tls-ciphers ...
tls-ciphersuites ...
tls-prefer-server-ciphers no
````

### Run secure connection
````shell
redis-server /etc/redis/redis.conf 2>&1 > redis.out &
redis-cli --tls --cacert /usr/local/share/ca-certificates/ca.crt
````

### Enforce TLSv1.3 connection

prepare client
````shell
openssl genrsa -out client.key 2048

openssl req -new -sha256 -key client.key
 -subj '/O=Redislabs/CN=Redis Client' | openssl x509 -req -sha256
  -CA /usr/local/share/ca-certificates/ca.crt
  -CAkey /etc/ssl/private/ca.key
  -CAserial /etc/ssl/private/ca.txt -CAcreateserial -days 365 
  -out client.crt

mv client.* /etc/ssl/clients
chown app:app /etc/ssl/clients/*
chmod 400 /etc/ssl/clients/*
````

prepare server configuration file
````shell
tls-protocols "TLSv1.3"
# tls-ciphers ...
tls-ciphersuites ...
````

connect to server 
````shell
redis-server /etc/redis/redis.conf 2>&1 > redis.out &
redis-cli --tls 
  --cacert /usr/local/share/ca-certificates/ca.crt 
  --cert /etc/ssl/clients/client.crt
  --key /etc/ssl/clients/client.key
````

### Redis Production Security Checklist

````text
Standalone and Cluster Mode
Ensure Redis is always deployed inside a trusted network.

Ensure protected mode is on unless ACLs or AUTH is enabled.

Ensure the Redis Log file is configured.

Ensure Redis is run as a non-privileged user.

Ensure Redis files are given a non-privileged group

Ensure Redis logs, files and configurations are not readable or writable by others on the operating system.

Ensure the Redis Log file is rotated.

Ensure Redis configuration files are not accessible by others, such as 740 permissions.

Ensure you leverage the latest Redis client and server version.

Consider IP restrictions through the network or operating system to ensure only trusted IPs can connect to Redis.

Consider using client side encryption to encrypt sensitive data.

Consider if TLS is right for your use case.

Consider changing the default Redis port

Consider backing up RDB and AOF files to a remote external location.

Ensure you select the right persistence method for your use case.

Consider sending Redis log files to syslog.

Cluster Mode Only
Ensure that an odd number of at least 3 nodes are deployed in the cluster

Ensure any reboot schedules do not reboot enough nodes at the same time to lose quorum.


Account Management
Standalone and Cluster Mode
Ensure AUTH or ACLs are enabled.

Ensure all users have a strong password.

Ensure the default user is disabled, unless required for backwards compatibility.

Ensure the @dangerous command category is excluded from all users and dangerous commands are given on a case by case basis.

Ensure that an external ACL file is used to configure ACLs.

Ensure that users configured in an external ACL file or the redis.conf file store passwords in hashed format.

Ensure that the requirepass is only set if backwards compatibility is required.

Consider if all ACL users are configured to least privilege.

Consider renaming commands to disable them entirely

Cluster Mode Only
Ensure that masteruser is used for authentication to masters.

Ensure that sentinel auth-user is used if you are using sentinel.


Transport layer Security
Standalone & Cluster Mode
Ensure non-TLS ports are disabled.

Ensure strong cipher suites are used with Redis.

Ensure appropriate modern TLS protocols are used.

Ensure client authentication is used.

Ensure server ciphers are prefered.

Ensure TLS is configured for replication

Ensure key files are given 400 permissions.

Ensure key files are owned by the Redis user.

Cluster Mode Only
Ensure TLS is enabled on the cluster bus
````