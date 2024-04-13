"""
Module: generate_text_embeddings.py
Author: Kevin Shindel
Date: 2024-13-04

This module is responsible for generating text embeddings using the SentenceTransformer model from the sentence-transformers library.

The main logic of the module is as follows:

1. Define the SentenceTransformer model to use.
2. Define a text string to be processed.
3. Convert the text into a vector embedding using the SentenceTransformer model.
4. Print the first ten elements of the generated embedding.

This module is part of a larger project that uses Redis Stack for semantic search and vector similarity.
It is used in the context of understanding and implementing vector similarity for semantic search with text.
"""


from sentence_transformers import SentenceTransformer

if __name__ == '__main__':
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    text = "This is a technical document, it describes the SID sound chip of the Commodore 64"
    embedding = model.encode(text)

    print(embedding[:10])
