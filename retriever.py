import os
import json
import time
import numpy as np
import faiss
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

EMBEDDINGS_CACHE = "data/embeddings.npy"

def embed_text(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return np.array(result.embeddings[0].values, dtype="float32")

def embed_all_chunks(chunks):
    """Embed all chunks, respecting the free-tier rate limit (100/min)."""
    embeddings = []
    for i, c in enumerate(chunks):
        embeddings.append(embed_text(c["text"]))
        if (i + 1) % 90 == 0 and (i + 1) < len(chunks):
            print(f"  Embedded {i+1}/{len(chunks)}, pausing 60s for rate limit...")
            time.sleep(60)
    return np.array(embeddings)

def build_index():
    with open("data/chunks.json", encoding="utf-8") as f:
        chunks = json.load(f)

    if os.path.exists(EMBEDDINGS_CACHE):
        print("Loading cached embeddings...")
        embeddings = np.load(EMBEDDINGS_CACHE)
    else:
        print(f"Embedding {len(chunks)} chunks (first run, this takes a few minutes)...")
        embeddings = embed_all_chunks(chunks)
        np.save(EMBEDDINGS_CACHE, embeddings)
        print(f"Cached embeddings to {EMBEDDINGS_CACHE}")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, chunks

def retrieve(index, chunks, question, k=3):
    question_embedding = embed_text(question).reshape(1, -1)
    distances, indices = index.search(question_embedding, k)
    results = [chunks[i] for i in indices[0]]

    chunks_by_id = {c["id"]: c for c in chunks}
    seen_ids = {r["id"] for r in results}
    expanded = list(results)
    for r in results:
        related_id = r.get("related_id")
        if related_id and related_id not in seen_ids and related_id in chunks_by_id:
            expanded.append(chunks_by_id[related_id])
            seen_ids.add(related_id)
    return expanded

if __name__ == "__main__":
    index, chunks = build_index()
    test_question = "What is the earnings disregard?"
    results = retrieve(index, chunks, test_question, k=3)
    print(f"\nQuestion: {test_question}")
    for r in results:
        print(f"  {r['id']} (valid_from={r['valid_from']}, valid_to={r['valid_to']}): {r['text'][:80]}...")