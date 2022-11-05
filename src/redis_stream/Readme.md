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