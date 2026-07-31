# Contributing

> **Last updated:** 2026-07-31

Thank you for your interest in contributing to the EU AI Compliance Toolkit.

## How to Contribute

1. **Report outdated legal content** — the most valuable contribution you can make. Regulatory drift is this repository's main failure mode. Use the [outdated legal content template](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues/new?template=outdated-legal-content.yml).
2. **Report a usability problem or gap** — something confusing, missing, or broken when you tried to use it. Use the [usability template](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues/new?template=usability-or-gap.yml).
3. **Submit a pull request** — fork the repo, make your changes, and open a PR. The pull request template lists what reviewers check.

Security concerns, especially anything involving leaked secrets or personal data, go through [`SECURITY.md`](SECURITY.md) rather than a public issue.

## Guidelines

- Use **British English** throughout (e.g. "organisation", "licence", "colour").
- Keep content **practical and actionable** — this is a toolkit, not an academic paper.
- Reference **official sources** (legislation, supervisory authority guidance) wherever possible.
- Do not include client-specific, proprietary, or confidential material.
- Include a `Last updated` date within the first 8 lines of each document, in this exact form:

  ```markdown
  > **Last updated:** YYYY-MM-DD
  ```

- Test all Markdown formatting before submitting.

## Sourcing Discipline For Legal Content

Anything under `eu-ai-act/`, `gdpr/`, or `dpia/` is held to a higher standard, because readers make compliance decisions on it.

- **Cite primary sources.** The Official Journal text, EUR-Lex, or supervisory authority guidance. Article and paragraph numbers, including the amending instrument where one applies.
- **Verify secondary commentary against the enacted text before publishing.** Law firm summaries are excellent for spotting that something changed and unreliable for exactly what changed. This repository has already had to correct two claims that were repeated consistently across six professional sources but did not match the regulation as enacted.
- **Update the claim-to-source register** in `eu-ai-act/risk-classification.md` when you add or change a claim.
- **State uncertainty explicitly.** A flagged open question is worth more than a confident wrong answer. If you cannot verify something, say so in the file and add a row to the regulatory watchlist.

### Retrieving EU legal texts

EUR-Lex web pages return HTTP 202 with an empty body to automated clients, which makes them awkward to check programmatically. The Publications Office CELLAR endpoint works:

```bash
curl -H "Accept: application/xhtml+xml" http://publications.europa.eu/resource/celex/32026R1744
```

Substitute the CELEX number of the instrument you need.

## Automated Checks

Two checks run on every pull request:

- **Relative links resolve.** External links are not checked, to avoid flaky failures.
- **Every document carries a valid `Last updated` header.**

Run them locally before opening a PR:

```bash
python3 .github/scripts/check_links.py && python3 .github/scripts/check_headers.py
```

A third check runs monthly and opens a tracking issue when content ages past its review threshold: 120 days for legal content, 270 days for everything else.

## Style

- Use plain, professional language accessible to compliance officers and developers alike.
- Prefer tables and structured formats over long prose paragraphs.
- Use decision trees and checklists where they aid comprehension.
- Link to official sources rather than paraphrasing legal text at length.

## Feedback

If you prefer not to open a pull request, you can also email feedback or suggestions to **contact@rdnordic.com**.

## Licence

By contributing, you agree that:

- Your contributions will be licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Your submissions are your own original work, or you have the right to submit them under this licence.
- You have not knowingly included any material that infringes on another party's intellectual property rights.
