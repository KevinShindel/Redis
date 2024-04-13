from redisvl.index import SearchIndex
from redisvl.query import VectorQuery
from redisvl.utils.vectorize.text.huggingface import HFTextVectorizer
from common import *

if __name__ == '__main__':

    # initialize the index and connect to Redis
    index = SearchIndex.from_yaml("schema.yaml")
    index.connect(REDIS_HOST, db=REDIS_DB, password=REDIS_PASSWORD, port=REDIS_PORT, decode_responses=True)

    # initialize the embedder
    hf = HFTextVectorizer(model="sentence-transformers/all-MiniLM-L6-v2")

    # create the index in Redis
    index.create(overwrite=True)

    # load data into the index in Redis (list of dicts)
    data = [
        {'content': 'That is a very happy person', 'genre': 'persons',
         'embedding': hf.embed('That is a very happy person', as_buffer=True)},
        {'content': 'That is a happy dog', 'genre': 'pets',
         'embedding': hf.embed('That is a happy dog', as_buffer=True)},
        {'content': 'Today is a sunny day', 'genre': 'weather',
         'embedding': hf.embed('Today is a sunny day', as_buffer=True)}
    ]

    index.load(data)

    # perform the VSS query
    query = VectorQuery(
        vector=hf.embed('That is a happy person'),
        vector_field_name="embedding",
        return_fields=["content"],
        num_results=3,
    )

    results = index.query(query)
    print(results)
