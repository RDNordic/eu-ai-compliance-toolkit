# EU AI Act Application Dates

> **Last updated:** 2026-08-18
>
> **Status: revised for Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026.**
>
> This page is a practical timeline summary of Article 113 of Regulation (EU) 2024/1689 **as amended**. Always verify against the official legal text and current guidance.

---

## Read This First

The Digital Omnibus on AI **delayed the high-risk obligations but did not delay the transparency obligations**.

If you take one thing from this page: the widely reported "AI Act delayed to 2027" headline is only half true. **Article 50 transparency duties have applied since 2 August 2026.** Teams that stood down entirely on the strength of the delay have missed an obligation that is already in force.

See [`omnibus-2026-changes.md`](omnibus-2026-changes.md) for the full change analysis, and [`article-50-transparency.md`](article-50-transparency.md) for the transparency duties in detail.

---

## Core Timeline

| Date | Applies From | Status | Notes |
|------|--------------|--------|-------|
| 2024-08-01 | Entry into force | Unchanged | AI Act entered into force 20 days after publication in the Official Journal. |
| 2025-02-02 | Chapter I and Chapter II | Unchanged | Includes AI literacy (Art. 4) and prohibited practices (Art. 5). |
| 2025-08-02 | Chapter III Section 4, Chapter V, Chapter VII, Chapter XII, and Art. 78 | Unchanged | Includes GPAI obligations and notified body framework elements. |
| **2026-08-02** | **General application date; Art. 50 transparency obligations** | **Unchanged - still binding** | The general application date stands. Transparency duties under Art. 50, including telling people they are interacting with an AI system, apply from this date. |
| **2026-12-02** | **Art. 50(2) machine-readable marking of synthetic content - grace period** | **New** | Grace period for systems **already placed on the market before 2 August 2026**. New systems comply from 2026-08-02. |
| **2026-12-02** | **New Art. 5 prohibitions - transitional deadline** | **New** | Safeguards deadline for the newly added prohibitions on CSAM-generating systems and non-consensual intimate imagery. |
| **2027-08-02** | **AI regulatory sandboxes** | **Moved** (was 2026-08-02) | Deadline for Member States to establish national AI regulatory sandboxes. |
| **2026-07-27** | **AI Act Arts. 102 to 110** | **New** | Art. 113(3)(d), added by the Omnibus. These are the AI Act's amendments to other Union legislation; they applied immediately on the Omnibus entering into force. |
| **2027-12-02** | **Annex III standalone high-risk systems** | **Moved** (was 2026-08-02) | Chapter III Sections 1, 2 and 3 for systems classified high-risk under Art. 6(2) and Annex III: employment, education, essential services, biometrics, law enforcement, migration, justice, democratic processes. |
| **2028-08-02** | **Annex I embedded high-risk systems (Art. 6(1))** | **Moved** (was 2027-08-02) | Chapter III Sections 1, 2 and 3 for systems classified high-risk under Art. 6(1) and Annex I. |
| 2030-08-02 | Legacy high-risk systems used by public authorities | Amended | Art. 111(2). Providers and deployers of high-risk systems intended for use by public authorities must comply by this date. The Omnibus re-keyed the grandfathering cut-off from a fixed 2026-08-02 to "the date of application of Chapter III", so it now tracks the delay. |
| 2030-12-31 | Legacy large-scale IT systems | **Unchanged, verified** | Art. 111(1) was **not** amended by the Omnibus. Annex X large-scale EU IT systems placed on the market before 2027-08-02 must comply by this date. The 2027-08-02 reference date stands. |

---

## Exactly What Was Delayed

The delay is narrower than "high-risk obligations moved". Article 113(3)(c) as replaced by the Omnibus reads, in substance:

> Chapter III, Sections 1, 2, and 3, **with the exception of Article 6(5)**, shall apply from (i) 2 December 2027 for Annex III high-risk systems, and (ii) 2 August 2028 for Annex I high-risk systems.

That covers:

- **Section 1** (Arts. 6-7): classification rules
- **Section 2** (Arts. 8-15): requirements for high-risk systems
- **Section 3** (Arts. 16-27): obligations of providers, deployers, importers, distributors

Two things are **not** in that list, and this is easy to miss:

- **Article 6(5)**, the Commission's duty to provide classification guidelines, is expressly excepted from the delay.
- **Chapter III Section 5** (Arts. 40-49): harmonised standards, conformity assessment, certificates, and **registration in the EU database**. Section 4 (notified bodies) has applied since 2 August 2025.

> **Open interpretation point.** On the face of Art. 113 as amended, Chapter III Section 5 is not covered by the deferral and would fall under the general 2 August 2026 application date, even though the substantive provider obligations it supports are deferred to 2027 and 2028. That reading has practical consequences for conformity assessment and Art. 49 registration timing. **This is a question for counsel, not a settled position.** Treat it as flagged, not answered, and watch for Commission guidance.

---

## What This Means In Practice

**If you are building an Annex III high-risk system**, you have gained roughly 16 months, but the requirements themselves did not soften. Risk management, data governance, technical documentation, logging, human oversight, and conformity assessment all still apply, just later. Treat the delay as schedule relief, not scope relief.

**If you ship a chatbot, an assistant, a content generator, or anything users interact with**, your obligation has been live since 2 August 2026 regardless of the delay. Check Art. 50 first: [`article-50-transparency.md`](article-50-transparency.md).

**If you generate or manipulate synthetic content**, note the split: systems already on the market get until 2 December 2026 for machine-readable marking; systems placed on the market on or after 2 August 2026 do not.

**If you are relying on the Art. 6(1) safety-component route**, re-run your classification. The Omnibus narrowed the definition. See [`omnibus-2026-changes.md`](omnibus-2026-changes.md).

---

## How to Use This Timeline

1. Confirm whether your use case is an AI system, GPAI model, or both.
2. Determine your role: provider, deployer, importer, distributor, authorised representative. See [`obligations-by-role.md`](obligations-by-role.md).
3. Check whether Art. 6(1), Annex III, or Annex X transitional rules apply.
4. Check Art. 50 separately. It applies across risk tiers and is not covered by the high-risk delay.
5. Record the date logic in your claim-to-source register.

---

## Primary Sources

- Regulation (EU) 2024/1689 (AI Act), consolidated
  - https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **Regulation (EU) 2026/1744 (Digital Omnibus on AI), 8 July 2026**, amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230. Published OJ 24 July 2026; in force 27 July 2026.
  - https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Article 113 (application and transitional dates)
  - https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113
- EU AI Act implementation timeline (European Commission service desk)
  - https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline

---

## Verification Note

> **Primary-source verified, 2026-07-31.**
>
> Every date in the table above was checked line-by-line against the Official Journal text of **Regulation (EU) 2026/1744** (CELEX 32026R1744), retrieved from the EU Publications Office CELLAR endpoint. The "was" column was verified against the Official Journal text of Regulation (EU) 2024/1689 as originally adopted.
>
> Specific provisions relied on: Art. 113(3)(a), (c) and (d) as amended by Art. 1(40) of the Omnibus; Art. 111(2) and new Art. 111(4) as amended by Art. 1(39); Art. 57(1) as amended by Art. 1(22); Art. 5(1) points (ba), (bb) and Art. 5(1a), (1b) as inserted by Art. 1(7); Art. 6(1a), (1b), (1c) as inserted by Art. 1(8); new Art. 4a as inserted by Art. 1(6).
>
> Regulation (EU) 2026/1744 was done at Strasbourg on **8 July 2026**, published in the Official Journal on **24 July 2026**, and under its Article 4 entered into force on the **third day** following publication, that is **27 July 2026**.
>
> **Remaining open item:** the Chapter III Section 5 question flagged above is an interpretation point, not a retrieval gap. It is tracked in the regulatory watchlist in [`risk-classification.md`](risk-classification.md).

---

This document is informational and not legal advice.
