# src/ingest.py
import os, json, uuid
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"
INDEX_PATH = "data/index.faiss"
CHUNKS_PATH = "data/chunks.json"
MODEL_NAME = "all-MiniLM-L6-v2"

def chunk_text(text, size=1200, overlap=200):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+size])
        i += size - overlap
    return [c.strip() for c in chunks if c.strip()]

def load_docs():
    docs = []
    for fn in os.listdir(DATA_DIR):
        if fn.endswith(".txt") or fn.endswith(".md"):
            p = os.path.join(DATA_DIR, fn)
            with open(p, "r", encoding="utf-8") as f:
                txt = "\n".join([line.rstrip() for line in f.readlines()]).strip()
                docs.append((fn, txt))
    return docs

def main():
    model = SentenceTransformer(MODEL_NAME)
    rows = []
    for fn, txt in load_docs():
        for idx, ch in enumerate(chunk_text(txt)):
            rows.append({
                "id": str(uuid.uuid4()),
                "source_file": fn,
                "chunk_id": idx,
                "text": ch
            })

    texts = [r["text"] for r in rows]
    embs = model.encode(texts, normalize_embeddings=True).astype("float32")
    dim = embs.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embs)

    faiss.write_index(index, INDEX_PATH)
    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    print(f"chunks={len(rows)} dim={dim}")

if __name__ == "__main__":
    main()
