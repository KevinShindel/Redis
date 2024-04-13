# Course outline

> Let's take a look at what we'll be covering in this course...

## Environment Setup

> We'll begin by getting your environment set up and ready for the course. You'll see how to get your own instance of Redis Stack either in the cloud or using Docker, and how to interact with it using redis-cli and the RedisInsight graphical management tool.

To take this course successfully, you will need:

- Redis Stack installed on your local machine or a cloud instance.
  - [Redis Enterprise Cloud](https://redislabs.com/try-free/) (free tier available).
  - [Docker](https://www.docker.com/products/docker-desktop) installed on your local machine.
- [Python 3.7](https://www.python.org/downloads/) or higher
- A [Redis](https://app.redislabs.com/) Cloud database or a local installation (to get a free Redis Cloud instance, jump to the instructions).
- The course sample data loaded into your Redis Stack instance.

> Throughout the course, we've provided example code written in Python, JavaScript (Node.js), Java and C#. You don't need to run the code to be successful on this course, and the exam does not contain programming language specific questions. If you'd like to try running some or all of the code samples then you'll also need to install:

Run Docker Image

```shell
docker run -p 6379:6379 --name stack-redis -d redis/redis-stack-server:latest
```

- [Node.js](https://nodejs.org/) (version 14.8 or higher).
- [Java JDK](https://sdkman.io/) (Java 11 or higher).
- [.NET SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) (version 6 or higher).

> You'll [need to follow the setup](https://github.com/redislabs-training/ru402/blob/main/README.md) instructions before proceeding.

## Section 1: Introduction to Semantic Search
> In this section you will be introduced to semantic search, what it is, what problems it resolves, and what are the popular use cases backed by it.
> In addition, you will understand the popular methods to model unstructured data so that it is possible to represent entities such as texts, images, audio files, or other data as vectors.
> The problem of modeling unstructured data is also discussed: the popular approaches are introduced, and you will learn how to work with your data using machine learning models. You will learn to convert text into embedding vectors using free embedding models.

## Section 2: Vector search
> Section 2 delves into translating the semantic similarity of entities from the real world to the similarity between vectors. The concept of distance between vectors is introduced, and you will learn to implement a simple system to find similar texts using the Python programming language. No Python advanced skills are required to understand the example, as the purpose of this section is understanding the mechanism behind vector similarity.

## Section 3: Redis as a vector database

> Implementing a system based on vector similarity is easy with Redis Stack and all the flavors based on it, Redis Enterprise and Redis Enterprise Cloud. This is the core section of the course where you will learn to configure vector search with different indexing methods, distance types and more. You will understand how to model data using the Hash and JSON data types, and understand the trade-offs to choose the suitable type for your use case. You will also learn the syntax of the Redis commands to create an index with the VECTOR field type and perform vector search.

## Section 4: Using the client libraries for vector search
> In this section, we'll examine how to write code that uses the vector search feature of Redis Stack. We'll first touch on coding with the following popular Redis clients:

- [redis-py](https://github.com/redis/redis-py) for Python.
- [node-redis](https://github.com/redis/node-redis) for Node.js.
- [jedis](https://github.com/redis/jedis) for Java.
- [NRedisStack](https://github.com/redis/NRedisStack) for .NET.

> Note that to be successful in this course, you don't need to be proficient at coding in Python, Node.js, Java or C# but you should check out the code samples for language(s) that you write applications in. There won't be any programming language specific questions on the final exam, we promise!

## Section 5: Developing use cases with semantic search

> Section 5 explains what are the most popular use cases that can be implemented with Redis Stack and its semantic search capability. From recommendation engines to anti-plagiarism systems, you will study and run examples to understand how to store, index and search your unstructured data and configure the suitable search parameters.
> Finally, you will understand the building blocks to developing a smart chatbot. In this section, you will go through the concepts of Generative AI, Retrieval Augmented Generation and understand how to integrate Redis Stack with OpenAI ChatGPT to "chat with your data". An example will follow, so you will be able to execute and fine tune the different components.


