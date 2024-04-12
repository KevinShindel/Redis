from sentence_transformers import SentenceTransformer

if __name__ == '__main__':
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    text = "This is a technical document, it describes the SID sound chip of the Commodore 64"
    embedding = model.encode(text)

    print(embedding[:10])
