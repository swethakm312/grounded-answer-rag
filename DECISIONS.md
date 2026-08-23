# Decisions
## Day 0 — Manual analysis findings

Read the full policy manual (data/policy-manual.md) end to end before writing 
any retrieval code, to identify the corpus's planted issues ahead of building.

**Gap found:** Full-time student needs calculation / absence rules. The topic 
is referenced as "addressed separately" or excluded/mentioned four times 
(§1.4.6, §2.4.2(d), §3.2.3, §5.2.3), but the one direct citation given 
(§7.1.3 → §5.4) points to an unrelated provision (care allowances). No 
working answer exists anywhere in the manual for how a household's needs 
figure is calculated when it includes a full-time student.

**Contradiction A:** §4.2.2 treats residential care as "temporary" for 
56 days (award unchanged per §5.1.2). §5.2.1 removes a household member 
after 28 days of absence unless one of three specific reasons in §3.2.2 
applies — "entering residential care" is not one of them. Same fact 
pattern, two different outcomes.

**Contradiction B:** §9.1.4 states the reporting deadline as "30 calendar 
days... required under §4.3," but §4.3.2 (the section actually cited) 
states 10 calendar days. §10.5.1(a) independently confirms 10 days 
elsewhere in the manual, so §9.1.4's "30 days" appears to be the outlier.

Decided to treat both contradictions as real and surface either when 
relevant, rather than picking one as "the" planted contradiction, since 
the problem statement says "at least one" — not "exactly one."

Ruled out as a false positive: §6.3.1 vs §6.3.2 (lump sum vs arrears) — 
initially looked contradictory but is a valid general-rule-plus-exception, 
not an overlap.

These findings will seed the ten-question test set required for the floor.


## Day 1 — Stack choice
Chose Gemini API for generation and FAISS for vector search.
Chunking by § section numbers since citations need to map to real clause numbers.

## Day 2 — Amendment received, date-aware design

Amendment No. 2026-01 confirmed Contradiction B (§9.1.4 vs §4.3.2) was real 
— the amendment's own note says the two never matched. 

Built ingest.py to chunk both the manual and the amendment by paragraph 
number (§x.x.x), tagging each chunk with valid_from/valid_to dates. Five 
provisions are hardcoded as superseded on 2026-03-01: §6.4.1 (disregard), 
§4.3.2 and §9.1.4 (reporting deadline), §6.6.1 (thresholds), §10.5.2 
(sanction rate). The amendment's own paragraphs are chunked separately and 
tagged valid_from 2026-03-01. Date resolution (which date field governs 
which provision) is deferred to generator.py via prompt, not hardcoded 
per-clause, since Amendment §5's transitional rules are plain-language.

Parsed 146 chunks total from both documents.

## Day 2 — Fixed retrieval gap for amended clauses

Found that similarity search alone didn't reliably retrieve both the old 
and amended version of a clause together (e.g. asking about the earnings 
disregard sometimes returned only the pre-amendment $120 chunk, missing 
the $175 replacement). Fixed by adding explicit related_id links between 
each superseded manual clause and its amendment paragraph in ingest.py, 
then expanding retrieval results to always include the linked chunk. 
Verified: querying "earnings disregard" now correctly returns both 
§6.4.1 (old, valid_to=2026-03-01) and Amendment §1.1 (new, 
valid_from=2026-03-01).


## Day 2 — Cleaned up accidental venv commit

Accidentally committed venv/ (hundreds of package files) in an earlier 
commit. Added .gitignore (excludes venv/, __pycache__/, *.pyc, and the 
embeddings cache) and removed venv from git tracking with git rm -r 
--cached. Repository history isn't rewritten (the bad commit still exists 
in history), but current state is clean going forward.

## Day 2 — generator.py working, date-aware answers confirmed

Built generator.py: retrieves chunks, adds the amendment's transitional 
rules (§5.1-5.3) to context whenever a date-sensitive chunk is retrieved, 
and prompts Gemini to select the correct value based on the reference 
date and cite it.

Verified with the earnings disregard test case:
- 2026-02-15 (pre-amendment) -> correctly answered $120, cited §6.4.1(a)
- 2026-04-01 (post-amendment) -> correctly answered $175, cited §6.4.1(a) 
  as amended by Amendment §1.1

Date-aware reasoning is handled entirely via prompt (not hardcoded 
per-clause logic), relying on Gemini reading the transitional rules 
directly. This worked correctly on first real test.


