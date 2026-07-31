# Claim-to-Source Register Template

> **Last updated:** 2026-07-31

Use this template to map legal and compliance claims to primary sources and verification dates.

## How to Use

- Add one row per substantive claim.
- Prefer primary sources: regulation text, official guidance, authority statements.
- Cite the **specific provision**, including the amending instrument where one applies. "AI Act Art. 113" is weaker than "Reg. (EU) 2026/1744 Art. 1(40), replacing Reg. (EU) 2024/1689 Art. 113(3)(c)(i)".
- Update `Last Verified` whenever you re-check the source, even if nothing changed.
- Mark a claim explicitly when it rests on secondary commentary you have not yet checked against the enacted text.

| Claim ID | Document | Section | Claim Summary | Source Type | Article / Reference | Link | Last Verified | Verified By | Notes |
|----------|----------|---------|---------------|-------------|---------------------|------|---------------|-------------|-------|
| C-001 | | | | `Regulation` / `Guideline` / `Authority statement` / `Case law` | | | YYYY-MM-DD | | |
| C-002 | | | | | | | YYYY-MM-DD | | |

### Worked example

What a completed row should look like:

| Claim ID | Document | Section | Claim Summary | Source Type | Article / Reference | Link | Last Verified | Verified By | Notes |
|----------|----------|---------|---------------|-------------|---------------------|------|---------------|-------------|-------|
| C-001 | `eu-ai-act/application-dates.md` | Core Timeline | Annex III high-risk obligations apply from 2027-12-02 | `Regulation` | Reg. (EU) 2026/1744 Art. 1(40), replacing Reg. (EU) 2024/1689 Art. 113(3)(c)(i) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | A. Reviewer | Verified against OJ text. Was 2026-08-02 |

## Source Quality Rule

Prefer sources in this order:

1. Official legislation text (EUR-Lex, Official Journal)
2. Official EU institution guidance
3. National supervisory authority guidance
4. Secondary commentary (supplemental context only)

## Consensus Is Not Verification

Professional commentary is excellent at telling you **that** something changed and unreliable at telling you **exactly what** changed. Summaries get copied between firms, so several sources agreeing is weak evidence, not strong evidence: they may share an ancestor rather than independently reading the text.

This is not hypothetical. In July 2026, six independent professional sources described the Digital Omnibus as extending AI Act Article 10(5) to deployers. The enacted text **deleted** Article 10(5) and inserted a new free-standing Article 4a with a different structure and scope. A register row citing "Art. 10(5) as amended" would have pointed at a provision that no longer existed.

**Use secondary sources to find the change. Cite the enacted text.**

## Retrieving EU Legal Texts

EUR-Lex web pages return HTTP 202 with an empty body to automated clients, which makes them awkward to verify programmatically. The Publications Office CELLAR endpoint works:

```bash
curl -H "Accept: application/xhtml+xml" http://publications.europa.eu/resource/celex/32026R1744
```

Replace the CELEX number with the instrument you need. The format is `3` + year + document type letter + number, so Regulation (EU) 2024/1689 is `32024R1689`.

Be aware that third-party AI Act mirrors, and at times official Commission reference pages, can lag behind amendments. Check whether the page you are reading carries an amendment notice before treating it as current.
