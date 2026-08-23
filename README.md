# The Grounded Answer

A CLI assistant that answers policy questions from the Calder County Household 
Support Program manual, citing the exact clause it relies on, and refusing to 
answer when the manual doesn't cover the question.

## Setup

1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set your Gemini API key: `set GEMINI_API_KEY=your_key_here`

## Run
python cli.py

## How it works# Date-Aware Grounded Answer RAG

A temporal-aware Retrieval-Augmented Generation (RAG) system built with Google GenAI SDK (gemini-2.5-flash) and FAISS. Designed to answer benefit policy questions accurately by taking into account specific reference dates, transitional amendment rules, and strict anti-hallucination constraints.

---

## Key Features

* Temporal Context Awareness: Correctly applies policy pre-amendment vs. post-amendment depending on the claim or determination date.
* Transitional Rule Injection: Automatically includes transitional logic clauses (Amendment §5.1–§5.3) when temporal metadata is detected in retrieved chunks.
* Strict Anti-Hallucination: Refuses to guess when policy details are missing or out-of-scope, returning "I don't know".
* Exact Clause Citations: Formats output with strict citations referencing specific sections and amendments.

---

## Project Structure

grounded-answer-rag/
├── data/                  # Standard policy documents & amendments
├── ingest.py              # Loads chunks and builds FAISS index with metadata
├── retriever.py           # Similarity search + transitional context injection
├── generator.py           # GenAI prompt formatting & date logic generation
├── cli.py                 # Command-line interactive interface
├── run_tests.py           # Test execution script with API rate-limit delays
├── TEST_QUESTIONS.md      # Test suite evaluation matrix & pass/fail results
├── TEST_RUN_LOGS.md       # Detailed test execution logs and traces
├── DECISIONS.md           # Architecture design choices & triage log
├── AI_USAGE.md            # Work distribution & AI assistance tracking
└── requirements.txt       # Dependencies

---

## Setup & Installation

### 1. Clone the Repository
git clone https://github.com/swethakm312/grounded-answer-rag.git
cd grounded-answer-rag

### 2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Gemini API Key
set GEMINI_API_KEY=your_gemini_api_key_here

---

## Running the System

### Interactive CLI
Ask custom date-aware questions interactively:
python cli.py

### Run Test Evaluation Suite
Execute all 10 ground-truth test scenarios:
python run_tests.py

---

## Evaluation Summary

* Pass Rate: 9/10 (90%)
* Date Logic Accuracy: 100% across pre/post amendment windows and spanning periods.
* Hallucination Refusal: 100% safe refusal on missing or out-of-scope queries.

*(See TEST_QUESTIONS.md and DECISIONS.md for full breakdown and triage notes).*