exit
sentence_transformers import SentenceTransformer
# Load embedding model (MiniLM for speed)
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text: str):
    return model.encode([text])[0]
EOF