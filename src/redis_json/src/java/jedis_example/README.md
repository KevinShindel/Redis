# RU204 Jedis (Java) Example

The following example demonstrates the execution of RedisJSON commands using the [Jedis](https://github.com/redis/jedis) client for the Java programming language.

## Prerequisites

* You'll need [Java 11](https://sdkman.io/sdks) or higher installed.
* You will need an instance of Redis Stack.  See the [setup instructions](/README.md) in the README at the root of this repo.
* If you are running your Redis Stack instance in the cloud or somewhere that isn't localhost:6379, you'll need to set the `REDIS_URL` environment variable to point at your instance before running the code.  If you need help with the format for this, check out the [Redis URI scheme specification](https://www.iana.org/assignments/uri-schemes/prov/redis).

## Run the Code

Ensure that your Redis Stack instance is running, and that you have set the `REDIS_URL` environment variable if necessary.  Example:

```bash
export REDIS_URL=redis://user:password@host:port
```

Now, run the code with the Maven wrapper provided:

```bash
./mvnw clean compile exec:java
```

## View the Code

The code is contained in [`App.java`](src/main/java/com/redis/university/ru204/App.java).