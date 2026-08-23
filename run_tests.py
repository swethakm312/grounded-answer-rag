import json
import os
import time
from retriever import build_index, retrieve
from generator import generate_answer

TEST_SUITE = [
    {
        "id": 1,
        "category": "Gap",
        "question": "What are the specific needs and absence rules applied to full-time students under the household support program?",
        "date": "2026-02-15"
    },
    {
        "id": 2,
        "category": "Contradiction A",
        "question": "What happens to a household member's status and benefit award after 40 days in residential care?",
        "date": "2026-02-15"
    },
    {
        "id": 3,
        "category": "Contradiction B",
        "question": "What is the deadline for reporting a change in household circumstances for a change that occurred on January 15, 2026?",
        "date": "2026-01-15"
    },
    {
        "id": 4,
        "category": "Date Logic (Pre)",
        "question": "What is the standard earnings disregard amount for a claim determined on February 10, 2026?",
        "date": "2026-02-10"
    },
    {
        "id": 5,
        "category": "Date Logic (Post)",
        "question": "What is the standard earnings disregard amount for a claim determined on April 5, 2026?",
        "date": "2026-04-05"
    },
    {
        "id": 6,
        "category": "Date Logic (Post)",
        "question": "If a change of circumstances occurred on March 10, 2026, how many days does the claimant have to report it?",
        "date": "2026-03-10"
    },
    {
        "id": 7,
        "category": "Amendment Rule",
        "question": "What sanction rate applies to an unreported income increase for a determination made in April 2026, and is there an exemption if the unreported change would have increased the award?",
        "date": "2026-04-10"
    },
    {
        "id": 8,
        "category": "Spanning Cutoff",
        "question": "How is a benefit claim calculated if the entitlement period spans from February 15, 2026 to March 15, 2026?",
        "date": "2026-03-01"
    },
    {
        "id": 9,
        "category": "Baseline",
        "question": "Who is considered an eligible dependent for the housing supplement calculation?",
        "date": "2026-02-15"
    },
    {
        "id": 10,
        "category": "Negative Control",
        "question": "What is the county policy on municipal parking permit discounts for low-income households?",
        "date": "2026-02-15"
    }
]

def run_tests():
    print("==================================================")
    print("  BUILDING INDEX & INITIALIZING FAISS...")
    print("==================================================")
    index, chunks = build_index()

    print("\n==================================================")
    print("  RUNNING 10 TEST CASES THROUGH RAG PIPELINE")
    print("  (Adding 12s sleep between calls to respect 5 RPM limit)")
    print("==================================================\n")
    
    log_output = ""
    
    for i, test in enumerate(TEST_SUITE):
        print(f"Running Test #{test['id']} [{test['category']}]...")
        
        try:
            results = retrieve(index, chunks, test['question'], k=3)
            answer, used_chunks = generate_answer(test['question'], test['date'], chunks, results)
            
            c_ids = ", ".join(c['id'] for c in used_chunks)
            entry = f"### Test #{test['id']} [{test['category']}]\n" \
                    f"**Question:** {test['question']}\n" \
                    f"**Reference Date:** {test['date']}\n" \
                    f"**Retrieved Chunks:** {c_ids}\n\n" \
                    f"**Generated Answer:**\n{answer}\n\n"
        except Exception as e:
            entry = f"### Test #{test['id']} [{test['category']}]\n" \
                    f"**Question:** {test['question']}\n" \
                    f"**ERROR:** {str(e)}\n\n"
        
        log_output += entry + ("-" * 50) + "\n\n"
        
        # Pause 12 seconds between requests to avoid rate limits
        if i < len(TEST_SUITE) - 1:
            time.sleep(12)

    with open("TEST_RUN_LOGS.md", "w", encoding="utf-8") as f:
        f.write("# Detailed Test Execution Logs\n\n" + log_output)
        
    print("\nComplete! All 10 results saved cleanly to TEST_RUN_LOGS.md")

if __name__ == "__main__":
    run_tests()