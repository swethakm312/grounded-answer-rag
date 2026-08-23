import re
import json

AMENDMENT_EFFECTIVE = "2026-03-01"

# Clauses whose OLD value is superseded by the amendment on the effective date
SUPERSEDED_BY_AMENDMENT = {
    "6.4.1": AMENDMENT_EFFECTIVE,   # earnings disregard
    "4.3.2": AMENDMENT_EFFECTIVE,   # reporting deadline (date-of-change governs, handled at generation time)
    "9.1.4": AMENDMENT_EFFECTIVE,   # reporting deadline reference
    "6.6.1": AMENDMENT_EFFECTIVE,   # income thresholds table
    "10.5.2": AMENDMENT_EFFECTIVE,  # sanction percentage
}

def parse_manual(text, source_label):
    """Split manual text into chunks by paragraph marker, e.g. **6.4.1**"""
    pattern = re.compile(
        r'\*\*(\d+(?:\.\d+){1,3}[A-Z]?)\*\*\s*(.*?)(?=\n\*\*\d+(?:\.\d+){1,3}[A-Z]?\*\*|\Z)',
        re.DOTALL
    )
    chunks = []
    for match in pattern.finditer(text):
        para_id = match.group(1)
        body = re.sub(r'\s+', ' ', match.group(2).strip())
        chunks.append({
            "id": f"§{para_id}",
            "text": body,
            "source": source_label,
            "valid_from": None,
            "valid_to": SUPERSEDED_BY_AMENDMENT.get(para_id),
        })
    return chunks

def parse_amendment(text):
    """Split amendment text into chunks by paragraph marker, e.g. **2.1**"""
    pattern = re.compile(
        r'\*\*(\d+\.\d+[A-Z]?)\*\*\s*(.*?)(?=\n\*\*\d+\.\d+[A-Z]?\*\*|\Z)',
        re.DOTALL
    )
    chunks = []
    for match in pattern.finditer(text):
        para_id = match.group(1)
        body = re.sub(r'\s+', ' ', match.group(2).strip())
        chunks.append({
            "id": f"Amendment §{para_id}",
            "text": body,
            "source": "amendment",
            "valid_from": AMENDMENT_EFFECTIVE,
            "valid_to": None,
        })
    return chunks

def load_and_chunk():
    with open("data/policy-manual.md", encoding="utf-8") as f:
        manual_text = f.read()
    with open("data/amendment-2026-01.md", encoding="utf-8") as f:
        amendment_text = f.read()

    manual_chunks = parse_manual(manual_text, "manual")
    amendment_chunks = parse_amendment(amendment_text)
    return manual_chunks + amendment_chunks

if __name__ == "__main__":
    chunks = load_and_chunk()
    print(f"Parsed {len(chunks)} chunks total.")
    for c in chunks[:5]:
        print(c)
    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)
    print("Saved to data/chunks.json")