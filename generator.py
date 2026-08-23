import os
from google import genai
from retriever import build_index, retrieve

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

TRANSITIONAL_IDS = ["Amendment §5.1", "Amendment §5.2", "Amendment §5.3"]

def get_transitional_chunks(chunks):
    by_id = {c["id"]: c for c in chunks}
    return [by_id[i] for i in TRANSITIONAL_IDS if i in by_id]

def format_chunk(c):
    date_note = ""
    if c["valid_from"] or c["valid_to"]:
        date_note = f" [valid from {c['valid_from'] or 'always'} to {c['valid_to'] or 'ongoing'}]"
    return f"{c['id']}{date_note}: {c['text']}"

def needs_transitional_context(results):
    return any(r["valid_from"] or r["valid_to"] for r in results)

def generate_answer(question, reference_date, chunks, results):
    context_chunks = list(results)
    if needs_transitional_context(results):
        for t in get_transitional_chunks(chunks):
            if t["id"] not in [c["id"] for c in context_chunks]:
                context_chunks.append(t)

    context_text = "\n\n".join(format_chunk(c) for c in context_chunks)

    prompt = f"""You are a policy assistant answering questions about the Calder County Household Support Program, using ONLY the information below.

The question relates to a claim/determination dated: {reference_date}

Some provisions were amended by Amendment No. 2026-01, effective 1 March 2026. Where a provision shows a valid date range, use ONLY the version that applies on {reference_date}. If the reference date falls within a chunk's valid range, that chunk's figure is correct; otherwise it is superseded or not yet in force.

If transitional rules are provided below, follow them exactly to determine which date (determination date vs. date the change of circumstances occurred) governs the answer.

Cite the exact clause number(s) you relied on (e.g. §6.4.1 or Amendment §1.1).

If the information below does not answer the question, say "I don't know" and do not guess.

Information:
{context_text}

Question: {question}

Answer (include the clause citation):"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text, context_chunks

if __name__ == "__main__":
    index, chunks = build_index()
    question = input("Ask a question: ")
    reference_date = input("What date does this relate to? (YYYY-MM-DD): ")
    results = retrieve(index, chunks, question, k=3)
    answer, used_chunks = generate_answer(question, reference_date, chunks, results)
    print(f"\nAnswer: {answer}")
    print(f"\n(Based on: {', '.join(c['id'] for c in used_chunks)})")