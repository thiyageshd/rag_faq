# src/retrieve.py
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "data/index.faiss"
CHUNKS_PATH = "data/chunks.json"
MODEL_NAME = "all-MiniLM-L6-v2"

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = faiss.read_index(INDEX_PATH)
        with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
            self.rows = json.load(f)

    def search(self, query, k=5):
        q = self.model.encode([query], normalize_embeddings=True).astype("float32")
        scores, ids = self.index.search(q, k)
        out = []
        for score, i in zip(scores[0], ids[0]):
            if i < 0:
                continue
            row = self.rows[i]
            out.append({
                "score": float(score),
                "source_file": row["source_file"],
                "chunk_id": row["chunk_id"],
                "text": row["text"]
            })
        return out

if __name__ == "__main__":
    r = Retriever()
    q = "What is our refund policy?"
    for hit in r.search(q, k=5):
        print(hit["score"], hit["source_file"], hit["chunk_id"])
        print(hit["text"][:180], "\n")
