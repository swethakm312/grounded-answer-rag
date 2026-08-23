import re
import json

AMENDMENT_EFFECTIVE = "2026-03-01"

SUPERSEDED_BY_AMENDMENT = {
    "6.4.1": AMENDMENT_EFFECTIVE,
    "4.3.2": AMENDMENT_EFFECTIVE,
    "9.1.4": AMENDMENT_EFFECTIVE,
    "6.6.1": AMENDMENT_EFFECTIVE,
    "10.5.2": AMENDMENT_EFFECTIVE,
}

MANUAL_TO_AMENDMENT_PARA = {
    "6.4.1": "1.1",
    "4.3.2": "2.1",
    "9.1.4": "2.2",
    "6.6.1": "3.1",
    "10.5.2": "4.1",
}

def parse_manual(text, source_label):
    pattern = re.compile(
        r'\*\*(\d+(?:\.\d+){1,3}[A-Z]?)\*\*\s*(.*?)(?=\n\*\*\d+(?:\.\d+){1,3}[A-Z]?\*\*|\Z)',
        re.DOTALL
    )
    chunks = []
    for match in pattern.finditer(text):
        para_id = match.group(1)
        body = re.sub(r'\s+', ' ', match.group(2).strip())
        related_para = MANUAL_TO_AMENDMENT_PARA.get(para_id)
        chunks.append({
            "id": f"§{para_id}",
            "text": body,
            "source": source_label,
            "valid_from": None,
            "valid_to": SUPERSEDED_BY_AMENDMENT.get(para_id),
            "related_id": f"Amendment §{related_para}" if related_para else None,
        })
    return chunks

def parse_amendment(text):
    pattern = re.compile(
        r'\*\*(\d+\.\d+[A-Z]?)\*\*\s*(.*?)(?=\n\*\*\d+\.\d+[A-Z]?\*\*|\Z)',
        re.DOTALL
    )
    chunks = []
    for match in pattern.finditer(text):
        para_id = match.group(1)
        body = re.sub(r'\s+', ' ', match.group(2).strip())
        amended_clause = next((k for k, v in MANUAL_TO_AMENDMENT_PARA.items() if v == para_id), None)
        chunks.append({
            "id": f"Amendment §{para_id}",
            "text": body,
            "source": "amendment",
            "valid_from": AMENDMENT_EFFECTIVE,
            "valid_to": None,
            "related_id": f"§{amended_clause}" if amended_clause else None,
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
    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)
    print("Saved to data/chunks.json")