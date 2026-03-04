# src/generate.py
from retrieve import Retriever

THRESHOLD = 0.35

PROMPT_TMPL = """You are a grounded assistant.
Answer ONLY using the provided context.
If context is insufficient, say: "I don't know based on provided sources."

Question:
{question}

Context:
{context}

Return:
1) Answer
2) Sources (file + chunk id)
"""

def build_context(hits):
    lines = []
    for h in hits:
        lines.append(f"[{h['source_file']}#{h['chunk_id']}] {h['text']}")
    return "\n\n".join(lines)

def ask(question):
    r = Retriever()
    hits = r.search(question, k=5)
    if not hits or hits[0]["score"] < THRESHOLD:
        return {
            "answer": "I don't know based on provided sources.",
            "sources": []
        }

    context = build_context(hits)
    prompt = PROMPT_TMPL.format(question=question, context=context)

    # Replace this with your LLM call:
    answer = "Mock answer for now. Connect your chat model API here."

    sources = [f"{h['source_file']}#{h['chunk_id']}" for h in hits[:3]]
    return {"answer": answer, "sources": sources, "prompt_preview": prompt[:1200]}

if __name__ == "__main__":
    q = "How are production incidents escalated?"
    out = ask(q)
    print(out["answer"])
    print("sources:", out["sources"])
