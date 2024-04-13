"""
Module: vector_search.py
Author: Kevin Shindel
Date: 2024-12-04

This module is responsible for creating a semantic search engine using Redis and the sentence-transformers library.

The main logic of the module is as follows:

1. Establish a Redis connection using the parameters defined in the environment variables.
2. Flush all data from the Redis database.
3. Define the SentenceTransformer model to use.
4. Create an index in Redis with a schema that includes a TextField for content, a TagField for genre, and a VectorField for embeddings.
5. Import sample data into Redis, converting text into vector embeddings using the SentenceTransformer model.
6. Define a test sentence and convert it into a vector embedding.
7. Perform a search in Redis using the KNN algorithm to find the two most similar vectors to the test sentence vector.
8. Print the search results.

This module is part of a larger project that uses Redis Stack for semantic search and vector similarity.
It is used in the context of understanding and implementing vector similarity for semantic search with text.
"""

import redis
from redis.commands.search.field import TextField, TagField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition
from redis.commands.search.query import Query
import numpy as np
from sentence_transformers import SentenceTransformer
from common import *

if __name__ == '__main__':
    # Get a Redis connection
    session = redis.Redis(host=REDIS_HOST,
                          port=REDIS_PORT,
                          db=REDIS_DB,
                          username=REDIS_USER,
                          password=REDIS_PASSWORD,
                          encoding='utf-8',
                          decode_responses=True)
    # run command FLUSH ALL
    session.execute_command('FLUSHALL')

    # Define the model we want to use
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Create the index
    index_def = IndexDefinition(prefix=["doc:"])
    schema = (TextField("content", as_name="content"),
              TagField("genre", as_name="genre"),
              VectorField("embedding", "HNSW",
                          {"TYPE": "FLOAT32", "DIM": 384, "DISTANCE_METRIC": "COSINE"}))
    session.ft('doc_idx').create_index(schema, definition=index_def)

    # Import sample data
    session.hset('doc:1',
                 mapping={'embedding': model.encode("That is a very happy person").astype(np.float32).tobytes(),
                          'genre': 'persons', 'content': "That is a very happy person"})
    session.hset('doc:2', mapping={'embedding': model.encode("That is a happy dog").astype(np.float32).tobytes(),
                                   'genre': 'pets',
                                   'content': "That is a happy dog"})
    session.hset('doc:3',
                 mapping={'embedding': model.encode("Today is a sunny day").astype(np.float32).tobytes(),
                          'genre': 'weather',
                          'content': "Today is a sunny day"})

    # This is the test sentence
    sentence = "That is a happy person"

    q = Query("*=>[KNN 2 @embedding $vec AS score]").return_field("score").return_field("content").dialect(2)
    res = session.ft("doc_idx").search(q, query_params={"vec": model.encode(sentence).astype(np.float32).tobytes()})
    print(res)
