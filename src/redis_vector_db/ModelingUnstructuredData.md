

> Semantic search helps to measure the semantic similarity of unstructured data such as texts, images, or media files. This is achieved by generating a vector that represents the features of the data under analysis because the vector is a convenient data structure to compress information and is easily manageable by a computer. We will introduce the techniques to transform unstructured data into a vector through practical examples and guide you to developing a simple application.

> Vectors have a massive role in modern Data Science and Machine Learning. With them, we can represent thousands of features for unstructured data, such as long texts, images, audio files, and more, using lists of floating point numbers. You can describe an entity as a vector in different terms; an intuitive way to visualize this representation might be RGB color codes.


When working with texts, there are several methods to represent them as arrays of numbers. An example may be expressing texts with the frequency of the words they contain. Consider these two sentences:

- "Understanding vector similarity is easy, but understanding all the mathematics behind a vector is not!"
- "Understanding vector similarity is difficult."

For a vectorized representation of these texts, we can list and count the repetition of words.

| Word          | Text1 | Text2 |
|---------------|-------|-------|
| Understanding | 2     | 1     |
| Vector        | 2     | 1     | 
| Similarity	   | 1     | 	1    |
| Is            | 	1    | 	1    |
| Easy	         | 1     | 	0    |
| Difficult     | 	0    | 	1    |
| but           | 	1    | 	0    |
| all           | 	1    | 	0    |
| mathematics   | 	1    | 	0    |
| behind	       | 1     | 	0    |
| not	          | 1     | 	0    |


## Activity. Using embedding models

1. Create env ```python3 -m venv env``` ```bash source env/bin/activate```
2. Install dependencies ```pip install -r requirements.txt```
3. Working with text ```python generate_text_embeddings.py```
4. Working with images ```python generate_image_embeddings.py```


## Vector search in practice

Vector search is a key function that can be performed between pairs of vectors.

- It is the process of finding data points that are similar to a given query vector in a set of vectors.
- Popular vector search uses include recommendation systems, image and video search, natural language processing, and anomaly detection.
- For example, if you build a recommendation system, you can use vector search to find (and suggest) products that are similar to a product in which a user previously showed interest.

Calculating the distance between vectors is a trivial operation using some math. Let's consider a simple example using sentences.

1. The following example in the cartesian plane defines three sentences
2. First, we calculate the vector embedding corresponding to each of the three sentences and store them
3. We define the test sentence "That is a happy person" and calculate the corresponding vector embedding
4. Finally, we compute the distance between the embedding of the test sentence and the three stored vector embeddings

Here's a graphical representation of the embeddings in a bi-dimensional vector space.

[<img style='background-color:white' alt="Vector space" src="https://university.redis.com/assets/courseware/v1/ee0b48c4ec07d86137daa0b8c7b6e041/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_2_2_0_three_sentences_vector_space.png"/>


## Distance Metrics

<img style='background-color:white' alt="Distance metrics" src="https://university.redis.com/assets/courseware/v1/03ab3e383eee49bde2b8689e04225af9/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_2_3_0_distance_metrics.png"/>

In this unit, we'll introduce three of the most popular distances:

- Euclidian distance
- Internal product
- Cosine similarity

### Euclidian distance
![Euclidian](https://university.redis.com/assets/courseware/v1/f6456581c5fc03d665625fd274a95420/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_2_3_0_euclidean_distance.png)
> The Euclidean distance is one of the most used distance metrics, and it calculates the distance between two data points on a plane.


### Internal product
> To determine similarity, the internal product looks at both the angle and magnitude of vectors. It's found by projecting one vector on the other and multiplying the result with the magnitude of the second vector. Let's look at this in two-dimensional space:
> 
<img style='background-color:white' alt="Internal product" src="https://university.redis.com/assets/courseware/v1/be2c2b7032840f8f831e453b05ab533e/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_2_3_0_internal_product.png"/>

>  The result of a dot product of two vectors is a scalar.
> 
> a = (3, 6, 1, 8)
> 
> b = (3, 2, 2, 1)
> 
> a⋅b = 3x3 + 6x2 + 1x2 +8x1 = 9 + 12 + 2 + 8 = 31


### Cosine similarity
> Cosine similarity is the first metric you would reach since it gives consistently good results, especially for high dimensional vector spaces. It is a good choice for use cases like document similarity, image comparison, pose comparison (in computer vision), and much more. Unlike the internal product, cosine similarity looks only at the angle between two vectors to determine similarity. Specifically, it looks at the cosine of the angle.

<img alt="Cosine similarity" height="400" src="https://university.redis.com/assets/courseware/v1/1ddfc42f838bd738e8c0ba37d32e65a1/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_2_3_0_cosine_similarity.png"/>

## Activity. Compute vector similarity.

> In this activity you will run a simple example to model the sentences considered before:
> - "That is a very happy person"
> - "That is a happy dog"
> - "Today is a sunny day"


### Result of the activity

Run the script `python vector_similarity.py` and you will see the following output:

```text
Query: That is a happy person
That is a very happy person  -> similarity score =  0.9429151
That is a happy dog  -> similarity score =  0.6945774
Today is a sunny day  -> similarity score =  0.25687617
```

### Redis as a real time vector database

> In this section, we will see how the concepts learned so far can be introduced in a system by adopting Redis as the primary database. In fact, Redis Stack (and all the flavors: Redis Enterprise and Redis Cloud Enterprise) can store vectors and calculate the distance between pairs of vectors, so you will dive into all the capabilities that turn Redis into a Vector Database.

### Accelerating semantic search

> The availability of machine learning models has boosted the rise of modern use cases and, consequently, the development and adoption of vector databases. Vector databases can store vectors and index and search the vector space efficiently.
> 
> <img style='background-color:white;padding:20px' alt="Vector database" src="https://university.redis.com/assets/courseware/v1/5b79b11ca26041e9c2015c4d5afcaa9e/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_3_1_0_vector_database.png"/>


### Modeling vectors in Redis

> All the Redis database flavors can store, index, and search vectors. This means that you can work with vectors using the Redis Stack distribution in your development environment and also for functional testing. Redis Enterprise and Redis Enterprise Cloud are built upon the Redis Stack capabilities, but they also offer a robust set of features to work efficiently with vectors at scale.
> 
> <img style='background-color:white;padding:20px' alt="Vector Embedding" src="https://university.redis.com/assets/courseware/v1/555d6d7e9d9ff697544c2d6c4c67e60b/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_3_2_0_redis_as_vector_database.png"/>

> First, it is important to highlight that before the native support for vectors was introduced in **Redis Stack Server 6.2.2-v1** in **2022**, vectors would be stored in Redis as a **string**, so serializing the vector and storing it in the desired data structure. 
> An example using the String:

 ```redis
  SET vec "0.00555776,0.06124274,-0.05503812,-0.08395513,-0.09052192,-0.01091553,-0.06539601,0.01099653,-0.07732834,0.0536432" 
```

```text
Since Redis Stack Server 6.2.2-v1, vectors can be stored as Hash or JSON documents, providing flexibility in how data 
is structured and accessed. Multiple indexing methods are supported, including FLAT and HNSW, enabling users to 
choose the most suitable approach for their specific use cases. Users can privilege precision over speed with the 
FLAT method or ensure high throughput with a little compromise on accuracy using HNSW. Additionally, 
Redis offers support for various distance metrics such as L2, IP, and COSINE, further enhancing the precision and
 efficiency of vector searches for specific types of embeddings. With these features, Redis becomes a flexible solution 
 for businesses seeking to harness the power of vector data in diverse applications, from recommendation engines to 
 similarity search tasks.
```

### Storing vectors: the hash and JSON data types

> Both the Hash and the JSON data types are suitable vector containers. In the following examples, we will show how to work with such data types. Let's calculate the vector embedding first, using the free all-MiniLM-L6-v2 embedding model from the HuggingFace library. This model maps texts of up to 256 words to a 384-dimensional dense vector space.
> 
```python
text = "Understanding vector search is easy, but understanding all the mathematics behind a vector is not!"
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embedding = model.encode(text)
# Note that Redis does not generate vectors; this is the responsibility of the client application to choose the desired library (HuggingFace, OpenAI, Cohere, and more)
```

> Next, we will store the vector embedding using the desired data structure and learn the syntax to create the index on
> the vector field stored in the document of choice. If you have already worked with Redis secondary indexing capabilities, 
> you know how to use the commands **FT.CREATE and FT.SEARCH**. Vectors can be indexed using the VECTOR data type,
> which adds to the existing **TEXT, TAG, NUMERIC, GEO and GEOSHAPE** types.


### Working with hashes

> The vector embedding we have just generated can be stored in a Hash as a binary blob within the document itself,
> together with the rest of the fields. This means that if our document is structured as follows:

```json
{
    "content": "Understanding vector search is easy, but understanding all the mathematics behind a vector is not!",
    "genre": "technical"
}
```
then we will include the vector embedding in the document itself:

```json
{
    "content": "Understanding vector search is easy, but understanding all the mathematics behind a vector is not!",
    "genre": "technical",
    "embedding": "..."
}
```
> In the following Python code sample, the utility astype from the numPy library for scientific computing is used: it casts the vector to the desired binary blob format, required by Redis for indexing purposes.

```python
blob = embedding.astype(np.float32).tobytes()
redis.hset('doc:1', mapping = {'embedding': blob,
                           'genre': 'technical',
                           'content': 'text'})
```

> Hash documents can be indexed with **FT.CREATE** using the **VECTOR** index type. 
> We can also index other fields in the same index definition, like the TEXT and TAG fields in the following instructions. 
> Indexing several fields in the same index enables hybrid searches, which we'll show later.

```redis
FT.CREATE doc_idx ON HASH PREFIX 1 doc: SCHEMA content AS content TEXT genre AS genre TAG embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 384 DISTANCE_METRIC COSINE
```

> Note how we have specified:
> - the dimension of the vectors, set by the specific embedding model **all-MiniLM-L6-v2**
> - the indexing method, **HNSW**
> - the vector type, **FLOAT32** in the example
> - the distance, **COSINE** in the example

Get full documentation about [Vector](https://redis.io/docs/latest/develop/interact/search-and-query/advanced-concepts/vectors/) in Redis.

### Working with JSON documents

> When using the JSON type to store the vectors, differently from the hash, vectors must be stored as arrays of floats instead of binary blobs. In this Python code sample, the numPy library converts the vector embedding to a list and stores it with the original text and the desired data.

```python
vector = embedding.tolist()
doc = {
    'embedding': vector,
    'genre': 'technical',
    'content': text
}
redis.json().set("doc:1", '$', doc)
```

> Indexing the JSON document can be achieved similarly to the hash:

````redis
FT.CREATE doc_idx ON JSON PREFIX 1 doc: SCHEMA $.content as content TEXT $.genre AS genre TAG $.embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 384 DISTANCE_METRIC COSINE
````

## Activity. Searching vectors


> Once your virtual environment is configured, you can move on to the rest of the tasks.
> 1. Download the code provided in the file vector_search.py.
> 2. Study the code example. In particular, focus on the conversion of the embedding to binary blob and how it is stored in the hash data structure.
> 3. Configure your Redis Cloud (or local instance) database host, port, username and password in the file.
> 4. Connect to the database using RedisInsight or redis-cli and flush the database with FLUSHALL.
> 5. Execute the example. The first time the sample is executed, the requested embedding model all-MiniLM-L6-v2 is downloaded and stored. Wait patiently, this can take a few seconds.

```text
Result{2 total, docs: [Document {'id': 'doc:1', 'payload': None, 'score': '0.0570845603943', 'content': 'That is a very happy person'}, Document {'id': 'doc:2', 'payload': None, 'score': '0.305422723293', 'content': 'That is a happy dog'}]}
```

> Expectedly, the best match is "**_That is a very happy person_**", having a shorter distance from the test sentence "**_That is a happy person_**".


### Choosing the right data type

> - Searching
>   - When using Hashes, storing and searching vectors requires using the binary blob format.
>   - For JSON documents, formats used for storing and searching are asymmetric: vectors must be stored as lists rather than binary blobs (model.encode(text).astype(np.float32).tolist()), but to perform VSS, JSON requires the binary blob format model.encode(text).astype(np.float32).tobytes()
> - Indexing. The Hash can index a single vector, defined by the FT.CREATE command. The JSON format, instead, can store and have multiple vectors indexed, identified by a JSONPath expression
> - Footprint. JSON has a larger memory footprint compared to the Hash


### Choosing the right distance

> - **L2**. The Euclidean distance is the default distance metric used by many algorithms, and it generally gives good results. Conceptually, it should be used when we compare observations whose features are continuous: numeric variables like height, weight, or salaries, for example, although it should be noted that it works best with low-dimensional data and where the magnitude of the vectors is important to be measured.
> - **COSINE**. Cosine similarity considers the cosine of the angle formed by two vectors (when the angle is close to 0, the cosine tends to 1, representing the maximum similarity). The cosine similarity does not account for the magnitude of the vectors being compared. The cosine distance is complementary to cosine similarity (obtained by subtracting the cosine similarity value from 1). This distance is appropriate when the magnitude of the vectors is not important in the description of the unstructured data
> - **IP**. The inner product looks at both the angle between the vectors and their magnitude. Note that this distance is equivalent to cosine similarity if vectors are normalized.


### Choosing the indexing method

**Flat index (FLAT)**
You can use the FLAT indexing method for smaller datasets. This method compares the test vector to all the vectors in the index, one by one. This is a more accurate but much slower and compute-intensive approach

**Hierarchical Navigable Small World graphs (HNSW)**
For more extensive datasets, it becomes difficult to compare the test vector to every single vector in the index, so a probabilistic approach is adopted through the HNSW algorithm. This method provides speedy search results. This approach trades some accuracy for significant performance improvements.


### Activity. Vector search with range queries

> Redis supports Range Queries for vector search, a way of filtering query results by the distance between the stored vectors and a query vector in terms of the relevant vector field distance metric. You can think of it as a geo query by radius, where we return all the points within a certain distance of a given point, except that the radius is the distance between the vectors. As an example, we can modify the query written in the previous example with:

```python
q = Query("@embedding:[VECTOR_RANGE $radius $vec]=>{$YIELD_DISTANCE_AS: score}").return_field("score").return_field("content").dialect(2)
res = redis.ft("doc_idx").search(q, query_params={"vec": model.encode(sentence).astype(np.float32).tobytes(), "radius":0.1})
```

This time, rather than specifying that we want the two best matches, we specify that we would rather have all the sentences with a distance score under 0.1. Executing the example with the modification produces:

```text
Result{1 total, docs: [Document {'id': 'doc:1', 'payload': None, 'score': '0.0570845603943', 'content': 'That is a very happy person'}]}
```
