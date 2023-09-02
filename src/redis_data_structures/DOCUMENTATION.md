# Redis docs


## Redis Lists Commands

### Set commands
- `LPUSH key value [value ...]` - Insert all the specified values at the head of the list stored at key. If key does not exist, it is created as empty list before performing the push operations. When key holds a value that is not a list, an error is returned.
- `RPUSH key value [value ...]` - Insert all the specified values at the tail of the list stored at key. If key does not exist, it is created as empty list before performing the push operation. When key holds a value that is not a list, an error is returned.
- `LPOP key` - Removes and returns the first element of the list stored at key.
- `RPOP key` - Removes and returns the last element of the list stored at key.
- `LSET key index value` - Sets the list element at index to value. For more information on the index argument, see List commands.
- `LTRIM key start stop` - Trim an existing list so that it will contain only the specified range of elements specified. Both start and stop are zero-based indexes, where 0 is the first element of the list (the head), 1 the next element and so on. For example: LTRIM foobar 0 2 will modify the list stored at foobar so that only the first three elements of the list will remain.
- `LINSERT key BEFORE|AFTER pivot value` - Inserts value in the list stored at key either before or after the reference value pivot. When key does not exist, it is considered an empty list and no operation is performed. An error is returned when key exists but does not hold a list value.
- `LREM key count value` - Removes the first count occurrences of elements equal to value from the list stored at key. The count argument influences the operation in the following ways: count > 0: Remove elements equal to value moving from head to tail. count < 0: Remove elements equal to value moving from tail to head. count = 0: Remove all elements equal to value.

### Get commands
- `LLEN key` - Returns the length of the list stored at key. If key does not exist, it is interpreted as an empty list and 0 is returned. An error is returned when the value stored at key is not a list.
- `LRANGE key start stop` - Returns the specified elements of the list stored at key. The offsets start and stop are zero-based indexes, with 0 being the first element of the list (the head of the list), 1 being the next element and so on. These offsets can also be negative numbers indicating offsets starting at the end of the list. For example, -1 is the last element of the list, -2 the penultimate, and so on. Note that if you have a list of numbers from 0 to 100, LRANGE list 0 10 will return 11 elements, that is, the rightmost item is included. This may or may not be consistent with behavior of range-related functions in your programming language of choice (think Ruby’s Range.new, Array#slice or Python’s range() function).
- `LINDEX key index` - Returns the element at index index in the list stored at key. The index is zero-based, so 0 means the first element, 1 the second element and so on. Negative indices can be used to designate elements starting at the tail of the list. Here, -1 means the last element, -2 means the penultimate and so forth.
- `LPOS key element [RANK rank] [COUNT num-matches] [MAXLEN len]` - Returns the index of matching elements inside a Redis list. By default, when no options are given, it will search for the first occurrence of element inside the list and return its index, or -1 if element cannot be found inside the list. When options are given, LPOS will return either the first occurrence of element inside the list, as an index, or the rank of element (its index plus one), depending on the option specified.
- `RPOPLPUSH source destination` - Atomically returns and removes the last element (tail) of the list stored at source, and pushes the element at the first element (head) of the list stored at destination.
- `BRPOPLPUSH source destination timeout` - BRPOPLPUSH is the blocking variant of RPOPLPUSH. When source contains elements, this command behaves exactly like RPOPLPUSH. When used inside a MULTI/EXEC block, this command behaves exactly like RPOPLPUSH. When source is empty, Redis will block the connection until another client pushes to it or until timeout is reached. A timeout of zero can be used to block indefinitely.
- `BLPOP key [key ...] timeout` - BLPOP is a blocking list pop primitive. It is the blocking version of LPOP because it blocks the connection when there are no elements to pop from any of the given lists. An element is popped from the head of the first list that is non-empty, with the given keys being checked in the order that they are given.
- `BRPOP key [key ...] timeout` - BRPOP is a blocking list pop primitive. It is the blocking version of RPOP because it blocks the connection when there are no elements to pop from any of the given lists. An element is popped from the tail of the first list that is non-empty, with the given keys being checked in the order that they are given.
- `RPOPLPUSH source destination` - Atomically returns and removes the last element (tail) of the list stored at source, and pushes the element at the first element (head) of the list stored at destination.
- `BRPOPLPUSH source destination timeout` - BRPOPLPUSH is the blocking variant of RPOPLPUSH. When source contains elements, this command behaves exactly like RPOPLPUSH. When used inside a MULTI/EXEC block, this command behaves exactly like RPOPLPUSH. When source is empty, Redis will block the connection until another client pushes to it or until timeout is reached. A timeout of zero can be used to block indefinitely.
- `BLPOP key [key ...] timeout` - BLPOP is a blocking list pop primitive. It is the blocking version of LPOP because it blocks the connection when there are no elements to pop from any of the given lists. An element is popped from the head of the first list that is non-empty, with the given keys being checked in the order that they are given.
- `BRPOP key [key ...] timeout` - BRPOP is a blocking list pop primitive. It is the blocking version of RPOP because it blocks the connection when there are no elements to pop from any of the given lists. An element is popped from the tail of the first list that is non-empty, with the given keys being checked in the order that they are given.


### Inspect commands
- `LREM key count value` - Removes the first count occurrences of elements equal to value from the list stored at key.
- `LPOS key element [RANK rank] [COUNT num-matches] [MAXLEN len]` - Returns the index of matching elements inside a Redis list.

## Redis Sets Commands

### Set commands
- `SADD key member [member ...]` - Add the specified members to the set stored at key. Specified members that are already a member of this set are ignored. If key does not exist, a new set is created before adding the specified members.
- `SREM key member [member ...]` - Remove the specified members from the set stored at key. Specified members that are not a member of this set are ignored. If key does not exist, it is treated as an empty set and this command returns 0.
- `SMOVE source destination member` - Move member from the set at source to the set at destination. This operation is atomic. In every given moment the element will appear to be a member of source or destination for other clients.
- `SPOP key [count]` - Removes and returns one or more random elements from the set value stored at key.

### Get commands
- `SISMEMBER key member` - Returns if member is a member of the set stored at key.
- `SMEMBERS key` - Returns all the members of the set value stored at key.
- `SRANDMEMBER key [count]` - When called with just the key argument, return a random element from the set value stored at key.
- `SSCAN key cursor [MATCH pattern] [COUNT count]` - Incrementally iterate Set elements.
- `SCARD key` - Returns the set cardinality (number of elements) of the set stored at key.
- `SDIFF key [key ...]` - Returns the members of the set resulting from the difference between the first set and all the successive sets.

### Inspect commands
- `SINTER key [key ...]` - Returns the members of the set resulting from the intersection of all the given sets.
- `SUNION key [key ...]` - Returns the members of the set resulting from the union of all the given sets.
- `SUNIONSTORE destination key [key ...]` - This command is equal to SUNION, but instead of returning the resulting set, it is stored in destination.
- `SINTERSTORE destination key [key ...]` - This command is equal to SINTER, but instead of returning the resulting set, it is stored in destination.
- `SDIFFSTORE destination key [key ...]` - This command is equal to SDIFF, but instead of returning the resulting set, it is stored in destination.


## Redis Sorted Sets Commands

### Set commands
- `ZADD key [NX|XX] [CH] [INCR] score member [score member ...]` - Add one or more members to a sorted set, or update its score if it already exists.
- `ZREM key member [member ...]` - Removes the specified members from the sorted set stored at key. Non existing members are ignored.
- `ZINCRBY key increment member` - Increments the score of member in the sorted set stored at key by increment. If member does not exist in the sorted set, it is added with increment as its score (as if its previous score was 0.0).
- `ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]` - Computes the union of numkeys sorted sets given by the specified keys, and stores the result in destination. It is mandatory to provide the number of input keys (numkeys) before passing the input keys and the other (optional) arguments.
- `ZINTERSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]` - Computes the intersection of numkeys sorted sets given by the specified keys, and stores the result in destination. It is mandatory to provide the number of input keys (numkeys) before passing the input keys and the other (optional) arguments.
- `ZREMRANGEBYRANK key start stop` - Removes all elements in the sorted set stored at key with rank between start and stop. Both start and stop are zero-based indexes with 0 being the element with the lowest score. These indexes can be negative numbers, where they indicate offsets starting at the element with the highest score. For example: -1 is the element with the highest score, -2 the element with the second highest score and so forth.
- `ZREMRANGEBYSCORE key min max` - Removes all elements in the sorted set stored at key with a score between min and max (inclusive).
- `ZREMRANGEBYLEX key min max` - Removes all elements in the sorted set stored at key between the lexicographical range specified by min and max.
- `ZREMRANGEBYSCORE key min max` - Removes all elements in the sorted set stored at key with a score between min and max (inclusive).

### Get commands

- `ZSCORE key member` - Returns the score of member in the sorted set at key.
- `ZCARD key` - Returns the sorted set cardinality (number of elements) of the sorted set stored at key.
- `ZCOUNT key min max` - Returns the number of elements in the sorted set at key with a score between min and max.
- `ZRANGE key start stop [WITHSCORES]` - Returns the specified range of elements in the sorted set stored at key. The elements are considered to be ordered from the lowest to the highest score. Lexicographical order is used for elements with equal score.
- `ZREVRANGE key start stop [WITHSCORES]` - Returns the specified range of elements in the sorted set stored at key. The elements are considered to be ordered from the highest to the lowest score. Descending lexicographical order is used for elements with equal score.
- `ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]` - Returns all the elements in the sorted set at key with a score between min and max (including elements with score equal to min or max). In contrary to the default ordering of sorted sets, for this command the elements are considered to be ordered from high to low scores.
- `ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]` - Returns all the elements in the sorted set at key with a score between max and min (including elements with score equal to max or min). In contrary to the default ordering of sorted sets, for this command the elements are considered to be ordered from high to low scores.
- `ZRANGEBYLEX key min max [LIMIT offset count]` - When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command returns all the elements in the sorted set at key with a value between min and max.
- `ZREVRANGEBYLEX key max min [LIMIT offset count]` - When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command returns all the elements in the sorted set at key with a value between max and min.
- `ZRANK key member` - Returns the rank of member in the sorted set stored at key, with the scores ordered from low to high. The rank (or index) is 0-based, which means that the member with the lowest score has rank 0.
- `ZREVRANK key member` - Returns the rank of member in the sorted set stored at key, with the scores ordered from high to low. The rank (or index) is 0-based, which means that the member with the highest score has rank 0.
- `ZLEXCOUNT key min max` - When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command returns the number of elements in the sorted set at key with a value between min and max.
- `ZSCAN key cursor [MATCH pattern] [COUNT count]` - Incrementally iterate sorted sets elements and associated scores.
- `ZINTERSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]` - Computes the intersection of numkeys sorted sets given by the specified keys, and stores the result in destination. It is mandatory to provide the number of input keys (numkeys) before passing the input keys and the other (optional) arguments.
- `ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]` - Computes the union of numkeys sorted sets given by the specified keys, and stores the result in destination. It is mandatory to provide the number of input keys (numkeys) before passing the input keys and the other (optional) arguments.


### Inspect commands
- `ZLEXCOUNT key min max` - When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command returns the number of elements in the sorted set at key with a value between min and max.
- `ZREMRANGEBYLEX key min max` - Removes all elements in the sorted set stored at key between the lexicographical range specified by min and max.
- `ZREMRANGEBYRANK key start stop` - Removes all elements in the sorted set stored at key with rank between start and stop.
- `ZREMRANGEBYSCORE key min max` - Removes all elements in the sorted set stored at key with a score between min and max (inclusive).
- `ZINTERSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]` - Computes the intersection of numkeys sorted sets given by the specified keys, and stores the result in destination. It is mandatory to provide the number of input keys (numkeys) before passing the input keys and the other (optional) arguments.
- `ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]` - Computes the union of numkeys sorted sets given by the specified keys, and stores the result in destination. It is mandatory to provide the number of input keys (numkeys) before passing the input keys and the other (optional) arguments.
- `ZSCAN key cursor [MATCH pattern] [COUNT count]` - Incrementally iterate sorted sets elements and associated scores.



## Redis Hashes Commands

### Set commands
- `HSET key field value` - Sets field in the hash stored at key to value. If key does not exist, a new key holding a hash is created. If field already exists in the hash, it is overwritten.
- `HSETNX key field value` - Sets field in the hash stored at key to value, only if field does not yet exist. If key does not exist, a new key holding a hash is created. If field already exists, this operation has no effect.
- `HMSET key field value [field value ...]` - Sets the specified fields to their respective values in the hash stored at key. This command overwrites any existing fields in the hash. If key does not exist, a new key holding a hash is created.
- `HINCRBY key field increment` - Increments the number stored at field in the hash stored at key by increment. If key does not exist, a new key holding a hash is created. If field does not exist or holds a string, the value is set to 0 before applying the operation. Since the value argument is signed you can use this command to perform both increments and decrements.
- `HINCRBYFLOAT key field increment` - Increment the specified field of a hash stored at key, and representing a floating point number, by the specified increment. If the field does not exist, it is set to 0 before performing the operation. An error is returned if one of the following conditions occur: The field contains a value of the wrong type (not a string). The current field content or the specified increment are not parsable as a double precision floating point number.
- `HDEL key field [field ...]` - Removes the specified fields from the hash stored at key. Specified fields that do not exist within this hash are ignored. If key does not exist, it is treated as an empty hash and this command returns 0.

### Get commands
- `HGET key field` - Returns the value associated with field in the hash stored at key.
- `HMGET key field [field ...]` - Returns the values associated with the specified fields in the hash stored at key.
- `HGETALL key` - Returns all fields and values of the hash stored at key. In the returned value, every field name is followed by its value, so the length of the reply is twice the size of the hash.
- `HKEYS key` - Returns all field names in the hash stored at key.
- `HVALS key` - Returns all values in the hash stored at key.
- `HSTRLEN key field` - Returns the string length of the value associated with field in the hash stored at key. If the key or the field do not exist, 0 is returned.
- `HLEN key` - Returns the number of fields contained in the hash stored at key.

### Inspect commands
- `HEXISTS key field` - Returns if field is an existing field in the hash stored at key.
- `HSCAN key cursor [MATCH pattern] [COUNT count]` - Incrementally iterate hash fields and associated values.


## Redis Expire Time Commands

### Set expiration commands 

- `EXPIRE key seconds` - Set a timeout on key. After the timeout has expired, the key will automatically be deleted. A key with an associated timeout is said to be volatile in Redis terminology.
- `PEXPIRE key milliseconds` - Like EXPIRE but takes milliseconds instead of seconds.
- `EXPIREAT key timestamp` - EXPIREAT has the same effect and semantic as EXPIRE, but instead of specifying the number of seconds representing the TTL (time to live), it takes an absolute Unix timestamp (seconds since January 1, 1970). A timestamp in the past will delete the key immediately.
- `PEXPIREAT key milliseconds-timestamp` - Like EXPIREAT but takes milliseconds precision instead of seconds.

### Inspect expiration time commands

- `TTL key` - Returns the remaining time to live of a key that has a timeout. This introspection capability allows a Redis client to check how many seconds a given key will continue to be part of the dataset.
- `PTTL key` - Like TTL this command returns the remaining time to live of a key that has an expire set, with the sole difference that TTL returns the amount of remaining time in seconds while PTTL returns it in milliseconds.


### Remove expiration time commands

- `PERSIST key` - Remove the existing timeout on key, turning the key from volatile (a key with an expire set) to persistent (a key that will never expire as no timeout is associated).


## Redis Transactions Commands

- `MULTI` - Marks the start of a transaction block. Subsequent commands will be queued for atomic execution using EXEC.
- `EXEC` - Executes all previously queued commands in a transaction and restores the connection state to normal.
- `DISCARD` - Flushes all previously queued commands in a transaction and restores the connection state to normal.
- `WATCH key [key ...]` - Marks the given keys to be watched for conditional execution of a transaction.
- `UNWATCH` - Flushes all the previously watched keys for a transaction.
- `WATCH key [key ...]` - Marks the given keys to be watched for conditional execution of a transaction.

### Example of transaction
````text
MULTI
SET event:Judo 100
INCR event:Judo
GET event:Judo
EXEC
````


## Bit Data Type Commands

### Set commands
- `SETBIT key offset value` - Sets or clears the bit at offset in the string value stored at key. The bit is either set or cleared depending on value, which can be either 0 or 1. When key does not exist, a new string value is created. The string is grown to make sure it can hold a bit at offset. The offset argument is required to be greater than or equal to 0, and smaller than 2^32 (this limits bitmaps to 512MB). When the string at key is grown, added bits are set to 0.
- `SETRANGE key offset value` - Overwrites part of the string stored at key, starting at the specified offset, for the entire length of value. If the offset is larger than the current length of the string at key, the string is padded with zero-bytes to make offset fit. Non-existing keys are considered as empty strings, so this command will make sure it holds a string large enough to be able to set value at offset.

### Get commands

- `GETBIT key offset` - Returns the bit value at offset in the string value stored at key. When offset is beyond the string length, the string is assumed to be a contiguous space with 0 bits. When key does not exist it is assumed to be an empty string, so offset is always out of range and the value is also assumed to be a contiguous space with 0 bits.
- `GETRANGE key start end` - Returns the substring of the string value stored at key, determined by the offsets start and end (both are inclusive). Negative offsets can be used in order to provide an offset starting from the end of the string. So -1 means the last character, -2 the penultimate and so forth. The function handles out of range requests by limiting the resulting range to the actual length of the string.
- `BITCOUNT key [start end]` - Count the number of set bits (population counting) in a string. By default all the bytes contained in the string are examined. It is possible to specify the counting operation only in an interval passing the additional arguments start and end.
- `BITPOS key bit [start] [end]` - Return the position of the first bit set to 1 or 0 in a string. The position is returned, thinking of the string as an array of bits from left to right, where the first byte’s most significant bit is at position 0, the second byte’s most significant bit is at position 8, and so forth. The same bit position convention is followed by GETBIT and SETBIT. When both start and end are set, the search is performed only in the specified range. When no set bit is found in the specified range, or if start > end, the special return value -1 is returned.
- `BITFIELD key [GET type offset] [SET type offset value] [INCRBY type offset increment] [OVERFLOW WRAP|SAT|FAIL]` - Perform arbitrary bitfield integer operations on strings. Integer representations are encoded as actual binary integers, so GET foo u4 0 returns 4 bits starting from the first bit and interprets them as an unsigned integer, while GET foo i4 0 returns 4 bits starting from the first bit and interprets them as a signed integer. Signed integers are represented using two’s complement. The first bit is the sign bit. The remaining bits are magnitude bits. The value of a positive number is the magnitude. The value of a negative number is the magnitude bit-wise inverted, plus one. For example, -1 is 0b11111111, -2 is 0b11111110, and so forth. The bitfield command supports different subcommands. The subcommand GET returns the specified bitfield(s) from the string value stored at key. GET can output signed and unsigned integers, in different bitfields of arbitrary size and at any offset within the string. The subcommand SET stores integer values right-aligned (directly with low bits) in the string value stored at key. The bitfield SET subcommand can also create a new key, provided that the bit offset specified is exactly the same as the current length of the string. The subcommand INCRBY increments or decrements (if negative) integers within given bitfields of a string value stored at key. The subcommand INCRBY can also create a new key, provided that the bit offset specified is exactly the same as the current length of the string. The subcommand OVERFLOW specifies the overflow behavior that should be used when the output of a bitfield operation exceeds the boundaries of integers of the specified bit size. The overflow behavior can be one of WRAP, SAT, or FAIL. The default is WRAP, which means that the value wraps around from the largest possible integer value back to the smallest possible integer value, and vice versa. The overflow behavior can be specified globally for all subcommands, or per-subcommand. The default is WRAP for all subcommands. The subcommand INCRBY supports the SAT overflow behavior, which means that the value saturates to the maximum or minimum integer value instead of wrapping around. The subcommand SET supports the FAIL overflow behavior, which means that the operation fails and the string value


### Inspect commands
- `BITOP operation destkey key [key ...]` - Perform a bitwise operation between multiple keys (containing string values) and store the result in the destination key. The BITOP command supports four bitwise operations: AND, OR, XOR and NOT, thus the valid forms to call the command are: BITOP AND destkey srckey1 srckey2 srckey3 ... BITOP OR destkey srckey1 srckey2 srckey3 ... BITOP XOR destkey srckey1 srckey2 srckey3 ... BITOP NOT destkey srckey The result of the operation is always stored at destkey.


## Geospatial commands

### Set commands
- `GEOADD key longitude latitude member [longitude latitude member ...]` - Add one or more geospatial items in the geospatial index represented using a sorted set.
- `GEOHASH key member [member ...]` - Returns members of a geospatial index as standard geohash strings.
- `GEOPOS key member [member ...]` - Returns longitude and latitude of members of a geospatial index.
- `GEODIST key member1 member2 [unit]` - Returns the distance between two members of a geospatial index.
- `GEORADIUS key longitude latitude radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]` - Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a point.
- `GEORADIUSBYMEMBER key member radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]` - Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a member.

### Get commands
- `GEOHASH key member [member ...]` - Returns members of a geospatial index as standard geohash strings.
- `GEOPOS key member [member ...]` - Returns longitude and latitude of members of a geospatial index.
- `GEODIST key member1 member2 [unit]` - Returns the distance between two members of a geospatial index.
- `GEORADIUS key longitude latitude radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]` - Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a point.

### Inspect commands
- `GEOSEARCH key [FROMMEMBER member] [FROMLONLAT longitude latitude] [BYRADIUS radius m|km|ft|mi] [BYBOX width height m|km|ft|mi] [ASC|DESC] [COUNT count] [WITHCOORD] [WITHDIST] [WITHHASH] [WITHCOORDS] [WITHDISTANCES] [WITHHASHES] [WITHGEODIST] [STORE key] [STOREDIST key] [STOREHASH key] [STOREUNIT m|km|ft|mi]` - Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a point.
- `GEOSEARCHSTORE key [FROMMEMBER member] [FROMLONLAT longitude latitude] [BYRADIUS radius m|km|ft|mi] [BYBOX width height m|km|ft|mi] [ASC|DESC] [COUNT count] [WITHCOORD] [WITHDIST] [WITHHASH] [WITHCOORDS] [WITHDISTANCES] [WITHHASHES] [WITHGEODIST] [STORE key] [STOREDIST key] [STOREHASH key] [STOREUNIT m|km|ft|mi]` - Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a point.
- `GEORADIUSBYMEMBER key member radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]` - Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a member.


## Luan in Redis

### Run script in CLI
````shell
HSET hash-key field1 "Hello" field2 "World"
EVAL "return redis.call('HGET', KEYS[1], ARGV[1])" 1 hash-key field1
> "Hello"
EVAL "return redis.call('HGET', KEYS[1], ARGV[1])" 1 hash-key field2
> "World"
````

- `EVAL script numkeys key [key...] arg [arg...]` - Execute a Lua script server side. The script runs inside the Redis server and it is isolated from the outer world (no disk access, no system calls, can’t interact with Redis clients). All the Redis commands must be called inside the script. It returns a single value: the return value of the script, as a Redis string (see next section for more information). The script does not need to return a string, but could also return a status reply, an integer, or simply nothing.

### Managing EVAL scripts

load script in redis server

- `SCRIPT LOAD script` # load LUA script into server and provide hash
- `EVALSHA sha1 numkeys key [key...] arg [arg...]` # run loaded script via sha1 hash
- `SCRIPT EXISTS sha1 [sha1...]` # check for existing script
- `SCRIPT FLUSH` # remove all scripts
- `SCRIPT KILL` # terminate LUA script 
- `SCRIPT DEBUG YES|SYNC|NO` # newer using in prod 

````shell
redis-cli> script load "local val=redis.call('GET', KEYS[1]) return val"
redis-cli> '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed' # generated hash for script
redis-cli> evalsha '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed' 1 key-name
redis-cli> "42" # returns result value
````

### Use Cases
- Limited Counters
- - Count by period 
- - \Adjust counter
- - Allow request if threshold not exceeded 

# TODO: Write script
# Step1: create script to save data and load in server
# Step2: create script to get data from server and load into server
# Step3: check logic for float numbers!