# Applying semantic search to popular use cases

> Finally, we will introduce how Vector Databases complement Large Language Models (LLM) to enable generative AI in chatbots. You will learn what Retrieval Augmented Generation (RAG) and basic concepts of prompt tuning to interact with LLMs.

## Implementing a text-based recommender system

<details>
  <summary>Click to show</summary>
  
> The idea behind a recommender system using vector search is to transform the relevant information (title, description, date of creation, authors, and more) into the corresponding vector embedding and store it in the same document as the original data. Then, when visualizing an entry (an article from a digital newspaper or any other media from the web), it is possible to leverage the stored vector embedding for that entry and feed into a vector search operation to semantically similar content.

## Writing a recommender system

1. We will use the dataset of books available under /data/books ```python df = pd.read_csv('data/books.jsonl', lines=True)```
2. The source code of the example is available as the Jupyter notebook books.ipynb

> You can refer to the source code for the details to load the books and generate the embeddings.
> Books will be stored in the following JSON format and using the Redis Stack JSON data type.

```json
  {
      "author": "Martha Wells",
      "id": "43",
      "description": "My risk-assessment module predicts a 53 percent chance of a human-on-human massacre before the end of the contract. A short story published in Wired.com magazine on December 17, 2018.",
      "editions": [
        "english"
      ],
      "genres": [
        "adult",
        "artificial intelligence"
      ],
      "inventory": [
        {
          "status": "available",
          "stock_id": "43_1"
        }
      ],
      "metrics": {
        "rating_votes": 274,
        "score": 4.05
      },
      "pages": 369,
      "title": "Compulsory",
      "url": "https://www.goodreads.com/book/show/56033969-compulsory",
      "year_published": 2018
    }
```

> The relevant section in the example is the implementation of semantic search, delivered by this snippet of code:

```python
import numpy as np
import Query

def get_recommendation(key):
    embedding = r.json().get(key)
    embedding_as_blob = np.array(embedding['embedding'], dtype=np.float32).tobytes()
    q = Query("*=>[KNN 5 @embedding $vec AS score]").return_field("$.title").sort_by("score", asc=True).dialect(2).paging(1, 5)
    res = redis.ft("books_idx").search(q, query_params={"vec": embedding_as_blob})
    return res
```

> The previous snippet does the following:
> 1. Given a document, it extracts the vector embedding for that document from the JSON entry
> 2. It converts the vector embedding, stored as an array of floats, to a binary array
> 3. It executes Vector Similarity Search to find similarities and get the most similar books
> 4. It pages the results, excluding the first result. Hence, paging starts from 1 rather than 0. In the first position, we would find the entry itself, having a distance from the test vector equal to zero

> Launching the execution of the example for the two known movies: "It" and "Transformers: The Ultimate Guide" :
```python
print(get_recommendation('book:26415'))
print(get_recommendation('book:9'))
```

We obtain the related recommendations:

```text
Result{5 total, docs: [Document {'id': 'book:3008', 'payload': None, '$.title': 'Wayward'}, Document {'id': 'book:2706', 'payload': None, '$.title': 'Before the Devil Breaks You'}, Document {'id': 'book:23187', 'payload': None, '$.title': 'Neverwhere'}, Document {'id': 'book:942', 'payload': None, '$.title': 'The Dead'}]}
Result{5 total, docs: [Document {'id': 'book:15', 'payload': None, '$.title': 'Transformers Volume 1: For All Mankind'}, Document {'id': 'book:3', 'payload': None, '$.title': 'Transformers: All Fall Down'}, Document {'id': 'book:110', 'payload': None, '$.title': 'Transformers: Exodus: The Official History of the War for Cybertron (Transformers'}, Document {'id': 'book:2', 'payload': None, '$.title': 'Transformers Generation One, Vol. 1'}]}
```

## Performing range search

> In this example, we executed a KNN search and retrieved the documents with the closest distance from the document being considered. Alternatively, we can perform a vector search range search to retrieve results having the desired distance from the sample vector embedding. The related code is:

```python
def get_recommendation_by_range(key):
    embedding = r.json().get(key)
    embedding_as_blob = np.array(embedding['embedding'], dtype=np.float32).tobytes()
    q = Query("@embedding:[VECTOR_RANGE $radius $vec]=>{$YIELD_DISTANCE_AS: score}") \
      .return_fields("title") \
      .sort_by("score", asc=True) \
      .paging(1, 5) \
      .dialect(2)
    
    # Find all vectors within a radius from the query vector
    query_params = {
      "radius": 3,
      "vec": embedding_as_blob
    }
    
    res = r.ft("books_idx").search(q, query_params)
    return res
```

> Computing this vector search range search returns similar results.

```text
Result{1486 total, docs: [Document {'id': 'book:3008', 'payload': None, 'title': 'Wayward'}, Document {'id': 'book:2706', 'payload': None, 'title': 'Before the Devil Breaks You'}, Document {'id': 'book:23187', 'payload': None, 'title': 'Neverwhere'}, Document {'id': 'book:942', 'payload': None, 'title': 'The Dead'}, Document {'id': 'book:519', 'payload': None, 'title': 'The Last Days of Magic'}]}
Result{1486 total, docs: [Document {'id': 'book:15', 'payload': None, 'title': 'Transformers Volume 1: For All Mankind'}, Document {'id': 'book:3', 'payload': None, 'title': 'Transformers: All Fall Down'}, Document {'id': 'book:110', 'payload': None, 'title': 'Transformers: Exodus: The Official History of the War for Cybertron (Transformers'}, Document {'id': 'book:2', 'payload': None, 'title': 'Transformers Generation One, Vol. 1'}, document {'id': 'book:37', 'payload': None, 'title': 'How to Build a Robot Army: Tips on Defending Planet Earth Against Alien Invaders, Ninjas, and Zombies'}]}
```

## Activity. Implementing a text-based recommender system

> We have provided you with a Jupyter notebook that includes the entire example.

> Ensure that you have database host, port, username and password for your Redis Cloud database at hand (alternatively, a Redis Stack instance is running). Complete the configuration of the environment by setting the environment variable that configures your Redis instance (default is localhost on port 6379).

1. Connect to the database using RedisInsight or redis-cli and flush the database with FLUSHALL.
2. Configure the environment variable to connect export REDIS_URL=redis://user:password@host:port

Now, you can start the notebook, execute all the cells, and check the results.
```bash
jupyter notebook books.ipynb
```
</details>

## Visual recommender systems
<details>
  <summary>Click to show</summary>

> Implementing a visual recommender system using vector search follows the same logic as the textual recommender systems. Once the image is modeled as a vector embedding, the implementation is very similar: the main difference resides in the embedding model used to generate the vector from the image file.

> We will split the dataset into training and testing sets.

1. Of the 10 photos available per individual, we select 5 to extract vector embeddings and store them in Redis, one per document. This means we will use 200 images to train our system to recognize identities from the ORL database
2. The rest of 5 faces are used to test the system. Every test image is vectorized and vector search performed.
3. If the identity of the individual matches the result of vector search, we account for a success
4. We will present a recognition rate. Testing with different embedding models can be evaluated by the success rate


### Working with Hashes

> We propose two different models for this system. We can model a user as a series of Hashes, each containing a vector embedding. An example of an entry would be:

```redis
HGETALL face:s33:4
1) "person_path"
2) "../../data/orl/s33/4.bmp"
3) "person_id"
4) "s33"
5) "embedding"
6) "...binary_blob...
```
> The code sample that implements the logic follows.

```python
for person in range(1, 41):
    person = "s" + str(person)
    for face in range(1, 6):
        facepath = '../../data/orl/' + person + "/" + str(face) + '.bmp'
        print ("Training face: " + facepath)
        vec = DeepFace.represent(facepath, model_name=models[0], enforce_detection=False)[0]['embedding']
        embedding = np.array(vec, dtype=np.float32).astype(np.float32).tobytes()
        face_data_values ={ 'person_id':person,
                            'person_path':facepath,
                            'embedding':embedding}
        r.hset('face:'+person+':'+str(face),mapping=face_data_values)
```
### Calculating the recognition rate

> Similarly to the training phase, we iterate through the rest of the faces, extract the vector embedding from each facial picture, and perform vector search. If the recognition is successful, and the face belongs to the known identity, we increment a counter to calculate a relative rate.

```python
import numpy as np
from redis import Query

def find_face(facepath):
    vec = DeepFace.represent(facepath, model_name=models[0], enforce_detection=False)[0]['embedding']
    embedding = np.array(vec, dtype=np.float32).astype(np.float32).tobytes()
    
    q = Query("*=>[KNN 1 @embedding $vec AS score]").return_field("score").dialect(2)
    res = r.ft("face_idx").search(q, query_params={"vec": embedding})
    
    for face in res.docs:
        print(face.id.split(":")[1])
        return face.id.split(":")[1]


def test():
    success = 0
    for person in range(1, 41):
        person = "s" + str(person)
        for face in range(6, 11):
            facepath = '../../data/orl/' + person + "/" + str(face) + '.bmp'
            print ("Testing face: " + facepath)
            found = find_face(facepath)
            if person == found:
                success = success +1
    
    print(success/200*100)
```
> The default vector search parameters used in the example and the chosen embedding model provide a recognition rate of 99.5%. You can experiment further with different models.

### Working with JSON documents

> Modeling the training set using JSON documents allows a more compact data representation. We can store all the vector embeddings for a person (five, in this example) in the same JSON document rather than one Hash document per vector embedding.

```redis
JSON.GET face:s11
{"person_id":"s11","embeddings":[[0.006758151110261679,0.018658878281712532,...],[0.006758151110261679,0.018658878281712532,...],[0.006758151110261679,0.018658878281712532,...],[0.006758151110261679,0.018658878281712532,...],[0.006758151110261679,0.018658878281712532,...]]
```

> The example proposed so far can be adapted with minor modifications. We can store the training set with the JSON command JSON.ARRAPPEND under the $.embedding field as follows:

```python
for person in range(1, 41):
    person = "s" + str(person)
    r.json().set(f"face:{person}", "$", {'person_id':person})
    r.json().set(f"face:{person}", "$.embeddings", [])
    for face in range(1, 6):
        facepath = '../../data/orl/' + person + "/" + str(face) + '.bmp'
        print ("Training face: " + facepath)
        vec = DeepFace.represent(facepath, model_name=EMBEDDING_MODEL, enforce_detection=False)[0]['embedding']
        embedding = np.array(vec, dtype=np.float32).astype(np.float32).tolist()
        r.json().arrappend(f"face:{person}",'$.embeddings', embedding)
```

> The index definition changes slightly, as well. Here, we define what portion of the JSON document we would like to index using a JSONPath expression.

```python
index_def = IndexDefinition(prefix=["face:"], index_type=IndexType.JSON)
schema = (VectorField("$.embeddings[*]", "HNSW", {"TYPE": "FLOAT32", "DIM": 2622, "DISTANCE_METRIC": "COSINE"}, as_name="embeddings"))
r.ft('face_idx').create_index(schema, definition=index_def)
# Note how the expression $.embeddings[*] selects all the vectors under the field $.embeddings.
```

## Activity. Implementing a face recognition system

> Now, you can start the notebooks, execute all the cells, and check the recognition rate presented once all the tests are performed. Execute the following notebook for the example using the Hash data structure:

```bash
 jupyter notebook faces.ipynb
 ```

And the following one to use the JSON data structure:

```bash
 jupyter notebook faces_json.ipynb
 ```

</details>

## LLM (Large Language Models)

<details>
  <summary>Click to show</summary>

> Redis, the Vector Database for conversational AI use cases
 
> Redis, as a high-performance, in-memory data platform, can play a pivotal role in addressing the challenges of LLM-based use cases. Here's how:
> - **Context Retrieval** for RAG. Pairing Redis Enterprise with LLMs enables these models to access external contextual knowledge. This contextual knowledge is crucial for providing accurate and context-aware responses, preventing the model from generating incorrect or 'hallucinated' answers. By storing and indexing vectors that model unstructured data, Redis Enterprise ensures that the LLM can retrieve relevant information quickly and effectively, enhancing its response quality.
> - **LLM Conversation Memory**. Redis Enterprise allows the persistence of all conversation history (memories) as embeddings in a vector database to improve model quality and personalization. When a conversational agent interacts with the LLM, it can check for relevant memories to aid or personalize the LLM's behavior. This feature enables seamless topic transitions during conversations and reduces misunderstandings.
> - **Semantic Caching**. LLM completions can be computationally expensive. Redis Enterprise helps reduce the overall costs of ML-powered applications by caching input prompts and evaluating cache hits based on semantic similarity using vector search. This caching mechanism ensures that frequently requested information is readily available, optimizing response times and resource utilization.

> Fine-tuning and Retrieval Augmented Generation (RAG)
> - **Fine-tuning**. Fine-tuning is a process that involves training a pre-trained LLM on a specific dataset to adapt it to a particular task or domain. Fine-tuning is crucial for improving the performance of LLMs in specialized tasks, such as question-answering, summarization, or conversational agents. By leveraging Redis Enterprise as a vector database, you can store and index the embeddings of the fine-tuned LLMs, enabling efficient retrieval and utilization of these models in real-time applications.
> - **Retrieval Augmented Generation (RAG)**. RAG is a framework that combines the strengths of LLMs and vector search to enhance the generation of responses in conversational AI systems. By using Redis Enterprise to store and index the embeddings of the LLMs and the retrieved documents, you can implement RAG efficiently. This approach allows the LLM to access external knowledge sources through vector search, improving the quality and relevance of the generated responses.

```text
RAG, presented by Meta in 2020, allows LLMs to incorporate external knowledge sources through retrieval mechanisms,
    extending the model capabilities with the latest information.
This method enables language models to perform similarly to humans, 
    with little information collected from the environment and in real-time.
RAG has been demonstrated to be very effective. However, it requires careful prompt engineering,
    management of fresh knowledge, and the orchestration of different components.
The following picture summarizes the flow when a user interacts with a chatbot assistant by asking a question.
```
<img style="background-color: white; padding: 20px" alt="RAG" src="https://university.redis.com/assets/courseware/v1/7acd2d2bd42400afcf61ea080f55e901/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_5_3_1_conversational_ai_rag.png" />

> We can simplify the architecture by considering the following three phases:
> 1. **Preparation**. The knowledge we want to make available to increase the expertise of our LLM assistant is collected, transformed, ingested, and indexed. This requires a specific data preprocessing pipeline, with connectors to the data source and downstream connectors to the target database. In the implementation we will explore in this article, Redis is the chosen Vector Database. The data can be represented by articles, documents, books, and any textual source to specialize our chat. Of the many indexing strategies available, vector databases have been demonstrated to be effective at indexing and searching unstructured data stored in vectorial format.
> 2. **Retrieval**. In this phase, the information (or context) relevant to the user's question is retrieved. Database semantic search assists in this task: the question is converted to a vector embedding, and vector search is performed to retrieve the relevant results from the database. vector search can be configured and performed with hybrid or range search strategies to determine what results best describe the question and can likely contain an answer. The assumption is that the question and the answer will be semantically similar.
> 3. **Generation**. Time of prompt engineering: with the relevant context and the question in our hands, we proceed to create a prompt and instruct the LLM to elaborate and return a response. Composing the right prompt to leverage the provided context (and eventually the previous historical interactions in the chat) is crucial to getting a relevant answer to the question and guardrail the output.

###  LLM conversation memory

<img style="background-color: white; padding: 20px" alt="LLM" src="https://university.redis.com/assets/courseware/v1/4e4b3a4b38630fad8de1a57479c3c683/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_5_3_1_conversational_ai_relevant_context.png" />

> The idea behind the LLM Conversation Memory is to improve the model quality and personalization through an adaptive memory.
> - Persist all conversation history (memories) as embeddings in a vector database.
> - A conversational agent checks for relevant memories to aid or personalize the LLM behavior.
> - Allows users to change topics without misunderstandings seamlessly.

### Semantic caching

> Semantic caching is used with large user bases or commonly asked questions. As usual with caching, this use case is about improving the application's responsiveness and reducing costs when using LLM-as-a-service. Because LLM completions are expensive, it helps to reduce the overall costs of the ML-powered application.

<img style="background-color: white; padding: 20px" alt="Semantic" src="https://university.redis.com/assets/courseware/v1/49b3faeb1b97b432e322236067b37b8c/asset-v1:redislabs+RU402+2023_11+type@asset+block/ru402_5_3_1_conversational_ai_semantic_cache.png" />

> Otherwise, the LLM produces a new response, which is cached for future searches.
> - Use vector database to cache input prompts
> - Cache hits evaluated by semantic similarity
> 
> *Note that the RedisVL client library makes semantic caching available out-of-the-box.

</details>

## Setting up a RAG Chatbot

<details>
  <summary>Click to show</summary>

> Prototyping an ML-powered chatbot is not an impossible mission. The many frameworks and libraries available, together with the simplicity of getting an API token from the chosen LLM service provider, can assist you in setting up a proof-of-concept in a few hours and lines of code. Sticking to the three phases mentioned earlier (preparation, generation, and retrieval), let's proceed to create a chatbot assistant, a movie expert you can consult to get recommendations from and ask for specific movies.


### Preparation

> Imagine a movie expert who may answer questions or recommend movies based on criteria (genre, your favorite cast, or rating). A smart, automated chatbot will be trained on a corpus of popular films, which, for this example, we have downloaded from Kaggle: the IMDB movies dataset, with more than 10,000 movies and plenty of relevant information.
> An entry in the dataset stores the following information:

```json
{
  "names": "The Super Mario Bros. Movie",
  "date_x": "04/05/2023",
  "score": 76.0,
  "genre": "Animation, Adventure, Family, Fantasy, Comedy",
  "overview": "While working underground to fix a water main, Brooklyn plumbers—and brothers—Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi.",
  "crew": [
    "Chris Pratt, Mario (voice)",
    "Anya Taylor-Joy, Princess Peach (voice)",
    "Charlie Day, Luigi (voice)",
    "Jack Black, Bowser (voice)",
    "Keegan-Michael Key, Toad (voice)",
    "Seth Rogen, Donkey Kong (voice)",
    "Fred Armisen, Cranky Kong (voice)",
    "Kevin Michael Richardson, Kamek (voice)",
    "Sebastian Maniscalco, Spike (voice)"
  ],
  "status": "Released",
  "orig_lang": "English",
  "budget_x": 100000000.0,
  "revenue": 724459031.0,
  "country": "AU"
}
```

> A possible index definition could be:

```redis
FT.CREATE movie_idx ON JSON PREFIX 1 moviebot:movie: SCHEMA $.crew AS crew
        TEXT $.overview AS overview TEXT $.genre AS genre TAG SEPARATOR ,
        $.names AS names TAG SEPARATOR ,
        $.overview_embedding AS embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 384 DISTANCE_METRIC COSINE
```

> This definition enables searches on several fields. As an example, we can perform a full-text search:
```redis
FT.SEARCH movie_idx @overview:'While working underground' RETURN 1 names
1) (integer) 1
2) "moviebot:movie:2"
3) 1) "names"
   2) "The Super Mario Bros. Movie"
```
> Or retrieve a movie by exact title match:
```redis
FT.SEARCH movie_idx @names:{Interstellar} RETURN 1 overview
1) (integer) 1
2) "moviebot:movie:190"
3) 1) "overview"
   2) "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage."
```
> The final step to complete the preparation phase is deciding what will be indexed by the database; for that, we need to prepare the paragraph to be transformed by the embedding model. We can capture as much information as we want. In the following Python excerpt, we will extract one entry and format the string movie.

```python
result = conn.json().get(key, "$.names", "$.overview", "$.crew", "$.score", "$.genre")
movie = f"movie title is: {result['$.names'][0]}\n"
movie += f"movie genre is: {result['$.genre'][0]}\n"
movie += f"movie crew is: {result['$.crew'][0]}\n"
movie += f"movie score is: {result['$.score'][0]}\n"
movie += f"movie overview is: {result['$.overview'][0]}\n"
```
> Now, we can transform this string to a vector using the chosen model and store the vector in the same JSON entry, so the vector is packed together with the original entry in a compact object.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embedding = model.encode(movie).astype(np.float32).tolist()
conn.json().set(key, "$.overview_embedding", embedding)
```

Repeating the operation for all the movies in the dataset completes the preparation phase.

### Retrieval

In this phase, we deal with the question from the user. 

```python

context = ""
q = Query("@embedding:[VECTOR_RANGE $radius $vec]=>{$YIELD_DISTANCE_AS: score}") \
    .sort_by("score", asc=True) \
    .return_fields("overview", "names", "score", "$.crew", "$.genre", "$.score") \
    .paging(0, 3) \
    .dialect(2)

# Find all vectors within VSS_MINIMUM_SCORE of the query vector
query_params = {
    "radius": VSS_MINIMUM_SCORE,
    "vec": model.encode(query).astype(np.float32).tobytes()
}

res = conn.ft("movie_idx").search(q, query_params)

if (res is not None) and len(res.docs):
    it = iter(res.docs[0:])
    for x in it:
        movie = f"movie title is: {x['names']}\n"
        movie += f"movie genre is: {x['$.genre']}\n"
        movie += f"movie crew is: {x['$.crew']}\n"
        movie += f"movie score is: {x['$.score']}\n"
        movie += f"movie overview is: {x['overview']}\n"
        context += movie + "\n"
```
## Activity 

Ensure that you have database host, port, username and password for your Redis Cloud database at hand
(alternatively, a Redis Stack instance is running). Complete the configuration of the environment by setting the
environment variable that configures your Redis instance (default is localhost on port 6379) 
and your OpenAI token: the chatbot leverages the OpenAI ChatGPT ChatCompletion API.

1. Connect to the database using RedisInsight or redis-cli and flush the database with FLUSHALL.
2. Configure the environment variable to connect export REDIS_URL=redis://user:password@host:port
3. Configure the OpenAI token using the environment variable: export OPENAI_API_KEY="your-openai-token"

Now, you can start the notebook and execute all the cells.
```bash
jupyter notebook moviebot.ipynb
```

> The execution of the notebook will open an input field. Type your question (e.g., Recommend three science fiction movies) and check the result!

## More Use Cases

> - **Fraud detection**. Vector search can be used to classify user behaviors when these are properly modeled as vectors, so we can deduce if user interactions resemble previously known fraud attempts
> - **Personalization** of product description. Based on semantic matching, the user will read a product description that highlights aspects of the product matching user preferences
> - **User segmentation**. Semantic matching enables the creation of categories of users to boost the relevance of recommendations
> - **Contact center analytics**. Vector search helps retrieve historical tickets to assist with incoming tickets. When paired with speech-to-text, this is especially useful to store phone conversations as text and have them indexed by Redis.
> - **Customer support**. Semantic search can significantly reduce the flow of new tickets if the customer, based on the problem description, gets a relevant document that solves the problem

</details>
