# Official Links

> **Last updated:** 2026-08-18

Curated primary and official sources relevant to this repository.

## EU AI Act

- Regulation (EU) 2024/1689 (AI Act) on EUR-Lex:
  - https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **Regulation (EU) 2026/1744 (Digital Omnibus on AI)** on EUR-Lex, amending the AI Act:
  - https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- European Commission AI Act overview:
  - https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- European AI Office:
  - https://digital-strategy.ec.europa.eu/en/policies/ai-office
- AI Act Service Desk (European Commission), article-by-article:
  - https://ai-act-service-desk.ec.europa.eu/

## GDPR And Data Protection

- Regulation (EU) 2016/679 (GDPR) on EUR-Lex:
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj
- European Data Protection Board:
  - https://www.edpb.europa.eu/
- European Data Protection Supervisor:
  - https://www.edps.europa.eu/

## EU Institutions And Law

- EUR-Lex main portal:
  - https://eur-lex.europa.eu/
- European Commission digital strategy portal:
  - https://digital-strategy.ec.europa.eu/

## Retrieving Legal Texts Programmatically

EUR-Lex web pages return HTTP 202 with an empty body to automated clients, so scripted checks fail against them. Use the EU Publications Office CELLAR content-negotiation endpoint instead:

```bash
curl -H "Accept: application/xhtml+xml" http://publications.europa.eu/resource/celex/32026R1744
```

The CELEX number is `3` + year + document-type letter + number: Regulation (EU) 2024/1689 is `32024R1689`, Regulation (EU) 2026/1744 is `32026R1744`.

Note that third-party AI Act mirrors, and at times official Commission reference pages, can lag behind amendments. Check for an amendment notice before treating a page as current.

## How To Use This File

- Prefer these links when validating or refreshing repo content.
- Prefer primary law and supervisory authority material over blog posts or marketing summaries.
- Record verification dates when converting important claims into maintainable source registers.
