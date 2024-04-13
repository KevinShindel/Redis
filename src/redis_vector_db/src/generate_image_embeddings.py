"""
Module: generate_image_embeddings.py
Author: Kevin Shindel
Date: 2024-13-03

This module is responsible for generating image embeddings using the imgbeddings library.

The main logic of the module is as follows:

1. Define the URL of the image to be processed.
2. Open the image using the PIL library.
3. Initialize the imgbeddings model.
4. Convert the image into an embedding using the imgbeddings model.
5. Print the first five elements of the generated embedding.

This module is part of a larger project that uses Redis Stack for semantic search and vector similarity.
It is used in the context of understanding and implementing vector similarity for semantic search with images.
"""

import requests
from PIL import Image
from imgbeddings import imgbeddings

if __name__ == '__main__':
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    ibed = imgbeddings()
    embedding = ibed.to_embeddings(image)
    print(embedding[0][0:5])
