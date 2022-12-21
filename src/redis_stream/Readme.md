# Redis Stream

### Add item to the stream

````text
> XADD numbers * n 1
````
#### Auto-generated ID stream message
````text
XADD -> Command 
numbers -> stream-key
* -> create auto-id
n -> key
1 -> value
````
#### pattern key stream message
````text
> XADD mystream 1526919030474-* message " World!"
> "1526919030474-56"
````
#### Static Key stream message
````text
> XADD mystream_static_id 172-1 message 'hi!'
> XADD mystream_static_id 172-2 message 'hi!'
````
#### Multi-value message stream 
````text
> XADD mystream * field1 value1 field2 value2 field3 value3
````

### Managing the Length of a Stream
#### XLEN
````text
> XLEN mystream
> 3
Integer reply: the number of entries of the stream at key.
````
#### XDEL
````text
Removes the specified entries from a stream, and returns the number of entries deleted. 
This number may be less than the number of IDs passed to the command in the case where some of the specified IDs do not exist in the stream.
````
````text
> XDEL mystream 1538561700640-0
````

#### XTRIM
````text
XTRIM trims the stream by evicting older entries (entries with lower IDs) if needed.
````
````text
- MAXLEN: Evicts entries as long as the stream's length exceeds the specified threshold, where threshold is a positive integer.
- MINID: Evicts entries with IDs lower than threshold, where threshold is a stream ID.
````
````text
> XTRIM mystream MAXLEN 1000
this will trim the stream to exactly the latest 1000 items
````

````text
> XTRIM mystream MINID 649085820
e, all entries that have an ID lower than 649085820-0 will be evicted
````

## Time-Based Range Queries

### XRANGE / XREVRANGE
````text
XRANGE -> Returns from OLDEST to NEWEST
XRANGE -> Returns from NEWEST to OLDEST
````

#### Search in all range
````text
XRANGE key start end [COUNT count]
> XRANGE somestream - +
1) 1) 1526985054069-0
   2) 1) "duration"
      2) "72"
      3) "event-id"
      4) "9"
      5) "user-id"
      6) "839248"
2) 1) 1526985069902-0
   2) 1) "duration"
      2) "415"
      3) "event-id"
      4) "2"
      5) "user-id"
      6) "772213"
````
### Search between timestamps
````text
> XRANGE somestream 1526985054069 1526985055069
````
### Returning a maximum number of entries
````text
> XRANGE somestream 1526985054069-0 + COUNT 1
1) 1) 1526985054069-0
   2) 1) "duration"
      2) "72"
      3) "event-id"
      4) "9"
      5) "user-id"
      6) "839248"
````

### Iterating a stream
````text
> XRANGE writers - + COUNT 2
1) 1) 1526985676425-0
   2) 1) "name"
      2) "Virginia"
      3) "surname"
      4) "Woolf"
2) 1) 1526985685298-0
   2) 1) "name"
      2) "Jane"
      3) "surname"
      4) "Austen"
````

### XREAD
````text
Read data from one or multiple streams, 
only returning entries with an ID greater than the last received ID reported by the caller.
````

````text
> XREAD COUNT 2 STREAMS mystream writers 0-0 0-0
1) 1) "mystream"
   2) 1) 1) 1526984818136-0
         2) 1) "duration"
            2) "1532"
            3) "event-id"
            4) "5"
            5) "user-id"
            6) "7782813"
      2) 1) 1526999352406-0
         2) 1) "duration"
            2) "812"
            3) "event-id"
            4) "9"
            5) "user-id"
            6) "388234"
2) 1) "writers"
   2) 1) 1) 1526985676425-0
         2) 1) "name"
            2) "Virginia"
            3) "surname"
            4) "Woolf"
      2) 1) 1526985685298-0
         2) 1) "name"
            2) "Jane"
            3) "surname"
            4) "Austen"
````
````text
STREAMS key_1 key_2 key_3 ... key_N ID_1 ID_2 ID_3 ... ID_N
````

### Blocking Read
````text
> XREAD COUNT [count] BLOCK [milliseconds] STREAMS stream1 [stream2] id1 [id2]
````

````text
> XREAD BLOCK 5000 STREAMS numbers $
Messages added to the stream after this XREAD command executes and begins to block
````


````text
> XREAD BLOCK 0 STREAMS numbers $
The XREAD command blocks indefinitely until a message is added to the stream and will never return if no new messages are added.
````

## Publish/Subscribe [https://redis.io/commands/?group=pubsub]

### Publish
````text
PUBLISH channel message
````
### Subscribe
````text
SUBSCRIBE channel [channel ...]
````


## Consumer Groups

### Create Consumer group
````text
> XGROUP CREATE queue_name group_name 0 MKSTREAM
> EXISTS queue_name
> XLEN queue_name
````
### Detail info about Consumers Groups
````text
> XINFO GROUPS queue_name
The output from XINFO GROUPS shows us which consumer groups are associated with the stream.
 We have one group named primes, containing our three consumers instances:
````

````text
> XINFO GROUPS numbers
1) 1) "name"             
   2) "primes"           
   3) "consumers"        
   4) (integer) 3        
   5) "pending"          
   6) (integer) 10       
   7) "last-delivered-id"
   8) "1667762643632-0" 
````


````text
The XINFO CONSUMERS command's output shows us information about the status of each consumer in the group primes:
````

````text
 XINFO CONSUMERS numbers primes
1) 1) "name"        
   2) "BOB-0"       
   3) "pending"     
   4) (integer) 3   
   5) "idle"        
   6) (integer) 1889
2) 1) "name"        
   2) "BOB-1"       
   3) "pending"     
   4) (integer) 1
   5) "idle"
   6) (integer) 773
3) 1) "name"
   2) "BOB-2"
   3) "pending"
   4) (integer) 4
   5) "idle"
   6) (integer) 393

````
### Memory usage
````text
> MEMORY USAGE numbers
(integer) 67294
````

## XINFO
```text
The XINFO STREAM command shows information about the current state of the stream, including:

The stream's overall length
Information about the underlying radix tree implementation
The number of consumer groups associated with the screen (we have 1, the primes group)
The last (highest) ID in the stream
The first and last entries in the stream
````

````text
> XINFO STREAM numbers
 1) "length"            
 2) (integer) 368       
 3) "radix-tree-keys"   
 4) (integer) 4         
 5) "radix-tree-nodes"  
 6) (integer) 10        
 7) "groups"            
 8) (integer) 1         
 9) "last-generated-id" 
10) "1667762560044-0"  
````

### Read queue as a part of consumer group
````text
> XREADGROUP GROUP group_name0 consumerA COUNT 1 BLOCK 1000 STREAMS stream_name >

Sign > - mean - Read the message immediately following the last message delivered to the consumer group 
````

### Processing in a Group
````text
The command returns the number of messages successfully acknowledged. Certain message IDs may no longer be part of the PEL (for example because they have already been acknowledged), and XACK will not count them as successfully acknowledged.
````
````text
> XACK stream_name consumer_group0 message_id-1
The XACK command removes one or multiple messages from the Pending Entries List (PEL) of a stream consumer group
````

### Disabling XACK
````text
Explanation
When using the NOACK option with XREADGROUP, Redis considers all messages read by XREADGROUP to be automatically acknowledged whether the client successfully processes them or not. This means that stream processing will then operate in an at-most-once delivery semantic. The pending entry list will not be maintained for the consumer,
 and the consumer will not be required to acknowledge successful processing of messages using the XACK command.
````
````text
The message delivery semantics will change from at-least-once to at-most-once.
Redis will consider all messages returned by XREADGROUP to be acknowledged.
````
````text
> XREADGROUP group_name0 consumer_name0 NOACK COUNT 1 SREAMS stream_name > 
````

## Basic Consumer Group Administration

### XPENDING
````text
The XPENDING command is the interface to inspect the list of pending messages,
 and is as thus a very important command in order to observe and understand what is happening with a streams consumer groups: what clients are active, 
what messages are pending to be consumed, or to see if there are idle messages.
````
````text
> XPENDING numbers primes
1) (integer) 7
2) "1667765887692-0"
3) "1667765888112-0"
4) 1) 1) "BOB-0"
      2) "1"
   2) 1) "BOB-2"
      2) "1"
   3) 1) "BOB-3"
      2) "1"
   4) 1) "BOB-5"
      2) "1"
   5) 1) "BOB-7"
      2) "1"
   6) 1) "BOB-8"
      2) "1"
   7) 1) "BOB-9"
      2) "1"

````


### XCLAIM
````text
In the context of a stream consumer group, this command changes the ownership of a pending message,
 so that the new owner is the consumer specified as the command argument. 
````
````text
> XCLAIM mystream mygroup Alice 3600000 1526569498055-0
1) 1) 1526569498055-0
   2) 1) "message"
      2) "orange"
````

###  XGROUP DELCONSUMER
- Deletes a consumer from a group
- Deletes the consumer's list of pending entries

### Managing Pending Messages
- <a href="https://redis.io/commands/xpending/">XPENDING</a>
- <a href="https://redis.io/commands/xclaim/">XCLAIM</a> 
- <a href="https://redis.io/commands/xinfo/">XINFO</a>

#### XCLAIM
````text
In the context of a stream consumer group, this command changes the ownership of a pending message, 
so that the new owner is the consumer specified as the command argument. 
````

### Consumer Recovery & Poison-Pill Messages
- Recovering from an Offline Consumer
````text
* Monitor pending messages using XPENDING
* Determine which messages should be reassigned: 
    By delivery count
    By Elapsed time since last delivery
    By Consumer idle time
````

### Poison-pill message
It is a message that:
 - A bad unprocessable message
 - Might cause consumer to die
 - Might be reprocessed indefinitely

### Poison-pill recovery

### Performance Considerations

- Streams act like an append-only log but are implemented as <a href="https://en.wikipedia.org/wiki/Radix_tree">radix-trees</a>
- O(1) guarantees performence for XREAD, XREADGROUP, XRANGE and XDEL
- Do not count stream (this transfrom an 0(1) into O(N))

 XADD command
 XRANGE command
 XREAD command
 XREADGROUP command
 XDEL command
 
### Stream Memory Usage
- With small data values, streams are much more memory-efficient
- As the data values increased in size, the data structure overhead of sorted sets will be less pronounced
- Best to generate sample data for your use case and test memory usage command


Useful commands 
- <a href="https://redis.io/commands/XADD/">XADD</a>
- <a href="https://redis.io/commands/XTRIM/">XTRIM</a>
- <a href="https://redis.io/commands/memory-usage/">MEMORY USAGE</a>

Suppose you're trying to decide whether to use a Redis stream, sorted set, or list. Memory efficiency is the most important criterion. How do you decide which data structure to use?
Generate realistic sample data, add the data to each data stucture, and then compare the data structures using the MEMORY USAGE command

The use of a Radix Tree provides a space-optimized data structure for the stream. Redis Streams keys are particularly suited to such a structure as they are relatively small and have repeating elements in them due to the use of millisecond timestamps in the keys.

Additionally, the storage overhead associated with message payload metadata is reduced by flagging a series of messages all with same field names, avoiding redundant storage of the field name strings.

### Stream Capping Strategies
Useful commands 
- <a href="https://redis.io/commands/XADD/">XADD</a>
- <a href="https://redis.io/commands/XTRIM/">XTRIM</a>
- <a href="https://redis.io/commands/expire/">EXPIRE</a>
- <a href="https://redis.io/commands/xlen/">XLEN</a>
- <a href="https://redis.io/commands/xrange/">XRANGE</a>

Strategies for control stream:
- Trimming with XADD (XADD numbers MAXLEN ~ 1000 * n 144450) # use for best performance
- Trimming with XTRIM (XTRIM numbers MAXLEN ~ 500) # for periodic usage (manual\automatic)
- Time bassed Trimming (EXPIRE mykey 10 ) # message will be deleted after 10 seconds

### Redis Streams Usage Patterns
- Large message payloads
- One stream vs multiple streams
- Single consumer vs consumer groups