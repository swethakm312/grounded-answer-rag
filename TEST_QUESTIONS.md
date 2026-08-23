# Test Questions & Evaluation Results

**Test Date:** 23 August 2026  
**Target Repo:** github.com/swethakm312/grounded-answer-rag  

---

| # | Category | Question & Date Context | Expected Outcome | Actual Outcome | Status |
|---|---|---|---|---|---|
| 1 | Gap | Full-time student needs/absence rules (2026-02-15) | Explicitly state missing policy / "I don't know" | Identified citations pointing to §5.4, recognized missing details, and returned "I don't know" | **PASS** |
| 2 | Contradiction A | Status/award after 40 days in residential care (2026-02-15) | Identify conflict or state §4.2.2 56-day rule | Correctly cited §4.2.1, §4.2.2, §5.1.1 and applied 56-day temporary rule | **PASS** |
| 3 | Contradiction B | Reporting deadline for change on Jan 15, 2026 | 10 days per pre-amendment §4.3.2 | Returned 10 days, citing §4.3.2 and Amendment §5.2 transitional rule | **PASS** |
| 4 | Date Logic | Earnings disregard for claim determined Feb 10, 2026 | $120 per original §6.4.1 | Returned $120, citing §6.4.1 | **PASS** |
| 5 | Date Logic | Earnings disregard for claim determined Apr 5, 2026 | $175 per Amendment No. 2026-01 | Returned $175, citing Amendment §1.1 and Amendment §5.1 | **PASS** |
| 6 | Date Logic | Reporting deadline for change occurring Mar 10, 2026 | 14 days per Amendment No. 2026-01 | Returned 14 days, citing Amendment §2.1 and Amendment §5.2 | **PASS** |
| 7 | Amendment Rule | Sanction rate & exemption for Apr 2026 determination | 15% rate + exemption for positive changes | Returned 15% rate (Amendment §4.1) and exemption rule (Amendment §4.2 / §5.2) | **PASS** |
| 8 | Spanning | Benefit calculation spanning Feb 15 - Mar 15, 2026 | Day-by-day apportionment per §7.4.3 | Returned day-by-day apportionment, citing Amendment §5.3 and §7.4.3 | **PASS** |
| 9 | Baseline | Eligible dependent definition for housing supplement (2026-02-15) | Accurate citation of dependent eligibility | Returned "I don't know" (Retrieval missed specific housing supplement eligibility clause) | **FAIL** |
| 10 | Negative Control | Municipal parking permit discount policy (2026-02-15) | "I don't know" / out of scope | Returned "I don't know" without hallucinating | **PASS** |

---
> **Note:** Test #2 above passed with specific phrasing ("status and benefit
> award"). An earlier ad-hoc test using vaguer phrasing ("status" only) failed
> at retrieval — see DECISIONS.md for details on this phrasing-sensitivity limitation.

## Detailed Test Run Logs

*(Refer to `TEST_RUN_LOGS.md` for full prompt trace, citations, and output text)*