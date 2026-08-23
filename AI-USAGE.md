# AI Usage

This file documents AI tool usage during development, as required by the 
Participant Handbook AI policy.

## Tools used
- Claude (Anthropic) — used throughout for planning, scaffolding, and debugging support.

## Log

### Day 0 (prep, before hackathon start)
- Used Claude to help plan project structure and module breakdown 
  (ingest.py / retriever.py / generator.py / cli.py separation).
- Used Claude to draft initial README.md and DECISIONS.md skeletons.
- All architectural decisions (stack choice, chunking strategy) were made by me; 
- Claude helped me reason through trade-offs, not choose for me.
  Used Claude as a reading partner to work through the full policy manual 
  section by section, flagging suspicious clauses (repeated numbers, forward 
  references, oddly specific definitions) as I read. Claude did not find the 
  planted contradiction/gap independently — I identified both; Claude helped 
  me cross-check candidates and rule out false positives (e.g. §6.3.1/6.3.2, 
  which I initially flagged but we confirmed was a valid rule-and-exception, 
  not a contradiction)
### Day 2
- Used Claude to design and write ingest.py's chunking logic (regex-based 
  paragraph split, date metadata scheme for amended clauses).
- Chunking strategy, which clauses to mark as superseded, and the overall 
  date-handling approach were decided by me based on the amendment text 
  and time constraints.
