# Detailed Test Execution Logs

### Test #1 [Gap]
**Question:** What are the specific needs and absence rules applied to full-time students under the household support program?
**Reference Date:** 2026-02-15
**Retrieved Chunks:** §5.2.3, §7.1.3, §3.2.3

**Generated Answer:**
Based on the information provided:

For absence rules, temporary absence does not include absence for the purpose of full-time education, which is addressed separately. (Citations: §5.2.3, §3.2.3)

For needs rules, the needs figure is calculated differently for full-time students, as the general calculation by reference to household size and composition does not apply to them. Specific rules are addressed in §5.4. (Citation: §7.1.3)

However, the specific rules for full-time students regarding absence and needs (i.e., what those separate rules are or what §5.4 details) are not provided in the given information. Therefore, I don't know the specific rules themselves.

--------------------------------------------------

### Test #2 [Contradiction A]
**Question:** What happens to a household member's status and benefit award after 40 days in residential care?
**Reference Date:** 2026-02-15
**Retrieved Chunks:** §5.1.1, §4.2.1, §4.2.2

**Generated Answer:**
After 40 days in residential care, the residence is still treated as temporary according to §4.2.2. Therefore:

*   **Status:** The household member's status has not changed, as residence is treated as temporary for the first 56 days, and a person is only considered no longer a member of the household from the date the residence becomes permanent (§4.2.1, §4.2.2).
*   **Benefit award:** The benefit award is not recalculated yet. Recalculation occurs from the date the residence is treated as permanent (§5.1.1), which has not happened after 40 days.

Citations: §4.2.1, §4.2.2, §5.1.1

--------------------------------------------------

### Test #3 [Contradiction B]
**Question:** What is the deadline for reporting a change in household circumstances for a change that occurred on January 15, 2026?
**Reference Date:** 2026-01-15
**Retrieved Chunks:** §4.3.2, Amendment §5.2, §9.1.4, Amendment §2.1, Amendment §2.2, Amendment §5.1, Amendment §5.3

**Generated Answer:**
The deadline for reporting a change in household circumstances is **10 calendar days** from the change occurring, or within 10 calendar days of the recipient becoming aware of the change, whichever is later.

This is determined by §4.3.2. Amendment §2.1, which would change the period to 14 days, is not applicable as the change of circumstances occurred before 1 March 2026. As per Amendment §5.2, "Where the change of circumstances occurred before 1 March 2026, the reporting period is the period that applied at the date of the change, irrespective of the date of the determination."

Citations: §4.3.2, Amendment §5.2.

--------------------------------------------------

### Test #4 [Date Logic (Pre)]
**Question:** What is the standard earnings disregard amount for a claim determined on February 10, 2026?
**Reference Date:** 2026-02-10
**Retrieved Chunks:** §6.4.1, §6.3.3, §6.4.2, Amendment §1.1, Amendment §5.1, Amendment §5.2, Amendment §5.3

**Generated Answer:**
The standard earnings disregard amount for a claim determined on February 10, 2026, is $120 per month.

Citation: §6.4.1

--------------------------------------------------

### Test #5 [Date Logic (Post)]
**Question:** What is the standard earnings disregard amount for a claim determined on April 5, 2026?
**Reference Date:** 2026-04-05
**Retrieved Chunks:** §6.4.1, §6.4.2, §6.3.3, Amendment §1.1, Amendment §5.1, Amendment §5.2, Amendment §5.3

**Generated Answer:**
The standard earnings disregard amount for a claim determined on April 5, 2026, is **$175 per month**.

Cited clauses: Amendment §1.1, Amendment §5.1, §6.4.1(a)

--------------------------------------------------

### Test #6 [Date Logic (Post)]
**Question:** If a change of circumstances occurred on March 10, 2026, how many days does the claimant have to report it?
**Reference Date:** 2026-03-10
**Retrieved Chunks:** §4.3.2, Amendment §5.2, §9.1.4, Amendment §2.1, Amendment §2.2, Amendment §5.1, Amendment §5.3

**Generated Answer:**
The claimant has 14 calendar days to report the change.

Citations: Amendment §2.1, Amendment §5.2.

--------------------------------------------------

### Test #7 [Amendment Rule]
**Question:** What sanction rate applies to an unreported income increase for a determination made in April 2026, and is there an exemption if the unreported change would have increased the award?
**Reference Date:** 2026-04-10
**Retrieved Chunks:** §10.5.2, Amendment §4.2, §10.5.1, Amendment §4.1, Amendment §5.1, Amendment §5.2, Amendment §5.3

**Generated Answer:**
For a determination made in April 2026:

The applicable sanction rate is **15 per cent** (Amendment §4.1), as the determination is made on or after 1 March 2026 (Amendment §5.1).

Yes, a sanction must not be imposed in respect of a failure to report where the change of circumstances in question would have increased the award (Amendment §4.2, inserting §10.5.3A). However, this exemption applies **only if the change of circumstances occurred on or after 1 March 2026** (Amendment §5.2).

--------------------------------------------------

### Test #8 [Spanning Cutoff]
**Question:** How is a benefit claim calculated if the entitlement period spans from February 15, 2026 to March 15, 2026?
**Reference Date:** 2026-03-01
**Retrieved Chunks:** Amendment §5.3, §7.4.3, §7.4.1, Amendment §5.1, Amendment §5.2

**Generated Answer:**
The benefit claim is calculated by applying the figures in force on each day of the entitlement period (February 15, 2026, to March 15, 2026). The award is then apportioned accordingly by reference to the number of days within each part of the period, reflecting the figures in force before March 1, 2026, and those in force on or after March 1, 2026.

**Clause Citation:** Amendment §5.3, §7.4.3

--------------------------------------------------

### Test #9 [Baseline]
**Question:** Who is considered an eligible dependent for the housing supplement calculation?
**Reference Date:** 2026-02-15
**Retrieved Chunks:** §7.3.2, §2.3.1, §7.2.1

**Generated Answer:**
I don't know

--------------------------------------------------

### Test #10 [Negative Control]
**Question:** What is the county policy on municipal parking permit discounts for low-income households?
**Reference Date:** 2026-02-15
**Retrieved Chunks:** §3.3.1, §7.2.1, §3.1.3

**Generated Answer:**
I don't know

--------------------------------------------------

