from retriever import build_index, retrieve
from generator import generate_answer

def main():
    print("Loading policy manual and amendment...")
    index, chunks = build_index()
    print("Ready. Ask a question about the Household Support Program.")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("Ask a question: ").strip()
        if question.lower() in ("quit", "exit"):
            print("Goodbye.")
            break
        if not question:
            continue

        reference_date = input("What date does this relate to? (YYYY-MM-DD): ").strip()

        results = retrieve(index, chunks, question, k=3)
        answer, used_chunks = generate_answer(question, reference_date, chunks, results)

        print(f"\nAnswer: {answer}")
        print(f"(Based on: {', '.join(c['id'] for c in used_chunks)})\n")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    main()