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