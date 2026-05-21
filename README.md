# Redis University - Complete Learning Repository

A comprehensive collection of Redis University courses and examples covering fundamental concepts to advanced techniques for building scalable, real-time applications with Redis.

## 📚 Course Modules

This repository contains 10 Redis University courses with practical examples and implementations:

1. **Async Connection** - Asynchronous Redis client patterns
2. **Cluster Connection** - Redis Cluster setup and operations
3. **Pub/Sub** - Publish/Subscribe messaging patterns
4. **DAO Schema** - Data Access Object patterns with Redis
5. **Redis Stream (RU202)** - Event streaming and time-series data
6. **Redis Security (RU330)** - Authentication, encryption, and access control
7. **Redis Data Structures (RU101)** - Core data types and operations
8. **Redis Scaling (RU301)** - Replication, clustering, and failover
9. **Redis JSON (RU204)** - JSON document storage and querying
10. **Redis Search (RU203)** - Full-text search and indexing

---

## 📁 Repository Structure

### `/src` - Source Code and Examples

#### **`/src/async`**
- **Description**: Asynchronous connection patterns and non-blocking I/O operations
- **Technologies**: Python (asyncio), aioredis
- **Benefits**: 
  - High-performance concurrent request handling
  - Improved throughput with non-blocking operations
  - Ideal for I/O-bound applications

#### **`/src/cluster`**
- **Description**: Redis Cluster deployment, configuration, and client integration
- **Technologies**: Python, Redis Cluster protocol, redis-py
- **Benefits**:
  - Horizontal scalability across multiple nodes
  - Automatic data partitioning
  - High availability and fault tolerance

#### **`/src/config`**
- **Description**: Configuration management and Redis server setup
- **Technologies**: Configuration files, shell scripts
- **Benefits**:
  - Centralized configuration management
  - Easy deployment and environment setup
  - Best practices for production deployments

#### **`/src/dao`**
- **Description**: Data Access Object pattern implementation with Redis
- **Technologies**: Python, OOP patterns, redis-py
- **Benefits**:
  - Abstraction layer for data operations
  - Decoupling business logic from data access
  - Easier testing and maintenance

#### **`/src/orm`**
- **Description**: Object-Relational Mapping (ORM) for Redis integration
- **Technologies**: Python ORM frameworks, Redis OM
- **Benefits**:
  - Object-oriented interface to Redis data
  - Automatic serialization/deserialization
  - Schema validation and type safety

#### **`/src/redi_search`** (RU203: Querying, Indexing, and Full-Text Search)
- **Description**: Advanced search capabilities, full-text indexing, and query optimization
- **Technologies**: Python, RediSearch module, redis-py, Docker, Node.js, Java, C#
- **Benefits**:
  - Complex search queries on Redis data
  - Full-text search with relevance ranking
  - Faceted search and aggregations
  - Sub-millisecond query performance
- **Key Files**: `commands.redis`, sample data loading scripts
- **Setup Options**: Docker (recommended), Local installation, Redis Cloud

#### **`/src/redis_data_structures`** (RU101: Redis Data Structure Module)
- **Description**: Deep dive into Redis core data structures (Strings, Lists, Sets, Sorted Sets, Hashes)
- **Technologies**: Python, redis-py, Redis CLI
- **Benefits**:
  - Understanding fundamental Redis primitives
  - Optimized operations for each data type
  - Foundation for advanced patterns
  - Memory efficiency

#### **`/src/redis_insight`**
- **Description**: RedisInsight GUI client setup and usage examples
- **Technologies**: RedisInsight desktop application, CLI tools
- **Benefits**:
  - Visual data exploration and debugging
  - Real-time monitoring and profiling
  - Advanced CLI with syntax highlighting
  - Support for Redis Stack modules

#### **`/src/redis_json`** (RU204: Storing, Querying and Indexing JSON at Speed)
- **Description**: JSON document storage, retrieval, and indexing with RedisJSON module
- **Technologies**: Python, Node.js, Java, C#, RedisJSON, Docker, RediSearch
- **Benefits**:
  - Native JSON document support without relational database
  - Sub-millisecond query performance
  - Atomic JSON document updates
  - Integration with full-text search
- **Sample Data**: Science fiction book collection (~1500 documents)
- **Examples**: 
  - Python data loader (`data_loader.py`)
  - Node.js Redis OM examples
  - Java and .NET implementations
  - Multi-language code samples

#### **`/src/redis_scaling`** (RU301: Redis Scaling Module)
- **Description**: Replication, Sentinel, and Cluster deployment for high availability and scaling
- **Technologies**: Redis Sentinel, Redis Cluster, Python, shell scripts
- **Benefits**:
  - Master-replica replication with automatic failover
  - Sentinel-managed high availability
  - Load distribution across nodes
  - Production-grade reliability
- **Key Tasks**:
  - Replication setup
  - Sentinel configuration and monitoring
  - Cluster deployment and management

#### **`/src/redis_security`** (RU330: Redis Security Module)
- **Description**: Authentication, encryption, access control lists (ACL), and security best practices
- **Technologies**: TLS/SSL, Redis ACL, shell scripts, authentication mechanisms
- **Benefits**:
  - Secure communication with TLS encryption
  - User authentication and authorization
  - Granular access control policies
  - Production security compliance
- **Key Features**: User management, password policies, ACL configuration

#### **`/src/redis_stream`** (RU202: Redis Stream Module)
- **Description**: Event streaming, time-series data, and consumer groups
- **Technologies**: Redis Streams, Python, redis-py
- **Benefits**:
  - Persistent message queues with automatic ID generation
  - Consumer group management for distributed processing
  - Time-based range queries
  - Event persistence and replay capability
- **Operations**: XADD, XRANGE, XLEN, XDEL, XTRIM, and consumer group commands

#### **`/src/redis_vector_db`**
- **Description**: Vector embeddings and semantic search capabilities using Redis as a vector database
- **Technologies**: Python, Machine Learning models, Vector embeddings, RediSearch with VECTOR field type
- **Benefits**:
  - Semantic search on unstructured data (text, images, audio)
  - AI/ML integration for similarity matching
  - Low-latency vector similarity search
  - Support for multiple distance metrics and indexing strategies

### `/tests` - Test Suites

#### **`/tests/test_redis_stream`**
- **Description**: Unit and integration tests for Redis Stream functionality
- **Technologies**: Python testing frameworks (pytest, unittest)
- **Benefits**:
  - Comprehensive test coverage
  - Validation of stream operations
  - Consumer group testing

---

## 🛠 Technologies Used

### Core Technologies
- **Python (49.6%)**: Primary language for examples, data loaders, and utilities
- **Jupyter Notebook (29.4%)**: Interactive learning and documentation
- **Java (6.4%)**: Object-oriented programming examples
- **C# (4.3%)**: .NET framework examples
- **JavaScript/Node.js (4.0%)**: Web-based examples
- **Dockerfile (5.2%)**: Containerization for Redis Stack
- **Shell (1.1%)**: Deployment and configuration scripts

### Redis-Specific
- **Redis Stack**: Core platform with multiple modules
- **RediSearch**: Full-text search and indexing
- **RedisJSON**: JSON document support
- **Redis Streams**: Event streaming
- **Redis Cluster**: Horizontal scaling
- **Redis Sentinel**: High availability
- **Redis ACL**: Access control

### Libraries and Frameworks
- **redis-py**: Python Redis client
- **Redis OM**: Object mapping for multiple languages
- **Node.js redis**: JavaScript client
- **Java Jedis**: Java Redis client
- **StackExchange.Redis**: .NET Redis client
- **Docker & Docker Compose**: Containerization

---

## 🎯 Key Benefits

### Performance
- ⚡ Sub-millisecond response times
- 🚀 High-throughput data operations
- 💾 In-memory data structures optimized for speed

### Scalability
- 📊 Horizontal scaling with Cluster mode
- 🔄 Master-replica replication
- 🎯 Data partitioning across nodes

### Reliability
- 🛡️ Automatic failover with Sentinel
- 💾 Data persistence with RDB and AOF
- 🔐 Security with TLS and ACL

### Developer Experience
- 📚 Multiple language support (Python, Java, C#, Node.js)
- 🎓 Comprehensive learning materials and examples
- 🐳 Docker support for easy setup
- 🖥️ RedisInsight GUI for visualization

### Real-World Applications
- 📱 Real-time messaging and notifications
- 🔍 Full-text search capabilities
- 📈 Time-series data and analytics
- 🤖 ML-powered semantic search
- 💬 Chat and collaboration features
- 📊 Leaderboards and counters
- 🛒 Shopping carts and sessions

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ (for data loaders and examples)
- Docker (recommended for beginners)
- Git

### Option 1: Using Docker (Recommended)
```bash
cd src/redis_json  # or any course directory
docker-compose up -d
```

### Option 2: Redis Cloud (Free Tier)
- Visit [Redis Cloud](https://redis.com/try-free/)
- Create a free account and database
- Use connection details in examples

### Running Examples
```bash
# For Redis JSON examples
cd src/redis_json
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python data_loader.py --dir data/books

# For Redis Stream examples
cd src/redis_stream
python stream_examples.py
```

---

## 📖 Learning Path

1. **Start**: Redis Data Structures (RU101) - Understand core concepts
2. **Build**: Redis JSON (RU204) + Redis Search (RU203) - Real-world data modeling
3. **Scale**: Redis Scaling (RU301) - Handle growth and reliability
4. **Secure**: Redis Security (RU330) - Production deployment
5. **Stream**: Redis Stream (RU202) - Event-driven architectures
6. **Advanced**: Vector DB + ORM patterns - Modern applications

---

## 🔗 Resources

- [Redis Official Documentation](https://redis.io/documentation)
- [Redis University](https://university.redis.com/)
- [RedisInsight Download](https://redis.com/redis-enterprise/redis-insight/)
- [Redis Community Discord](https://discord.gg/redis)
- [Redis Stack Docker Hub](https://hub.docker.com/r/redis/redis-stack)

---

## 📝 License

This repository contains educational materials from Redis University. Please refer to individual course folders for specific license information.

## 🤝 Contributing

This is an educational repository from Redis University. For contributions and issues, please refer to the official Redis repositories.

---

**Last Updated**: 2026
**Repository**: Redis University Course Materials and Examples
