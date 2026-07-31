# Regulatory Watchlist Template

> **Last updated:** 2026-07-31

Use this template to maintain a live list of regulatory changes that may require updates to a compliance document.

## How to Use

- Keep one row per tracked topic.
- Assign a single named owner for each row. An unowned row is not tracked, it is decoration.
- Set a concrete review date, not "ongoing".
- Use `Status` to record whether the source material actually changed since the last check.
- When something does change, update the affected document **and** its claim-to-source register in the same pass.

| Topic | What to Watch | Owner | Review Date | Status | Trigger | Notes |
|-------|---------------|-------|-------------|--------|---------|-------|
| AI Act delegated/implementing acts | New acts affecting obligations or definitions | | YYYY-MM-DD | `No change` / `Update needed` | Official publication | |
| AI Office guidance | New FAQs, guidance, or interpretations | | YYYY-MM-DD | `No change` / `Update needed` | Guidance update | |
| EDPB guidance | New or revised GDPR guidance relevant to AI | | YYYY-MM-DD | `No change` / `Update needed` | Guideline publication | |
| National authority guidance | Local regulator updates (e.g. Datatilsynet, CNIL, BfDI, ICO) | | YYYY-MM-DD | `No change` / `Update needed` | Publication update | |
| Case law and enforcement | Decisions affecting lawful basis, profiling, or AI deployment | | YYYY-MM-DD | `No change` / `Update needed` | Court/authority decision | |
| **Amending regulations** | Omnibus or simplification packages amending instruments you rely on | | YYYY-MM-DD | `No change` / `Update needed` | Official Journal publication | Amending acts move article numbers, not just dates |
| Harmonised standards | CEN-CENELEC deliverables underpinning high-risk conformity | | YYYY-MM-DD | `No change` / `Update needed` | Standard published or cited in OJ | Standards readiness drives whether deadlines hold |

## Suggested Starter Rows For 2026 To 2027

Adapt these to your own scope. Dates reflect the position after Regulation (EU) 2026/1744.

| Topic | What to Watch | Review By | Why It Matters |
|---|---|---|---|
| Art. 50 transparency | Commission guidance and codes of practice on marking and labelling | 2026-09-01 | Applies from 2026-08-02 and was **not** deferred |
| Art. 50(2) marking grace period | Systems on the market before 2026-08-02 must comply by 2026-12-02 | 2026-11-01 | Short runway, easy to miss |
| New Art. 5 prohibitions | Enforcement approach to the Art. 5(1a) safeguards test | 2026-11-01 | Transitional deadline 2026-12-02 |
| Art. 4a bias detection | Supervisory expectations on evidencing the six cumulative conditions | 2026-11-01 | New route; interacts with Art. 9(2)(g) GDPR |
| Chapter III Section 5 scope | Whether Arts. 40-49 fall outside the deferral and apply from 2026-08-02 | 2026-09-01 | Open interpretation point affecting conformity assessment and registration timing |
| Annex III deferral | Whether 2027-12-02 holds, given standards readiness was the stated reason for the delay | 2027-03-01 | A further deferral is possible if standards slip again |
| National competent authorities | Designations and national implementing law, including EEA timing for Norway, Iceland, Liechtenstein | 2026-12-01 | EEA incorporation can lag EU application dates |

## Review Discipline

A watchlist only works if reviews actually happen. Two habits make the difference:

- **Review on a schedule, not on rumour.** If you only check when someone forwards a newsletter, you will miss the quiet amendments.
- **Record a negative result.** Marking a row `No change` with today's date is a real output. It is what lets the next person trust the register instead of redoing the work.

Consider automating the reminder rather than relying on memory. This repository runs a monthly staleness check that files a tracking issue when a document ages past its review threshold; see `.github/workflows/staleness.yml` for a pattern you can copy.
