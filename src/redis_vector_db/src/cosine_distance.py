import numpy as np
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer

if __name__ == '__main__':
    # Define the model we want to use (it'll download itself)
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    sentences = [
        "That is a very happy person",
        "That is a happy dog",
        "Today is a sunny day"
    ]

    sentence = "That is a happy person"

    # vector embeddings created from dataset
    embeddings = model.encode(sentences)

    # query vector embedding
    query_embedding = model.encode(sentence)


    def cosine_similarity(a, b):
        """  define our distance metric """
        return np.dot(a, b) / (norm(a) * norm(b))


    # run semantic similarity search
    print("Query: That is a happy person")
    for e, s in zip(embeddings, sentences):
        print(s, " -> similarity score = ", cosine_similarity(e, query_embedding))

    def find_maximum_similarity(_embeddings, _query_embedding):
        """ find the maximum similarity """
        _max_similarity = 0
        _max_index = 0
        for idx, embd in enumerate(_embeddings):
            similarity = cosine_similarity(embd, _query_embedding)
            if similarity > _max_similarity:
                _max_similarity = similarity
                _max_index = idx
        return _max_similarity, _max_index

    max_similarity, max_index = find_maximum_similarity(embeddings, query_embedding)
    print("Most similar sentence: ", sentences[max_index], " -> similarity score = ", max_similarity)