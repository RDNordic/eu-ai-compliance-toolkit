# Pull Request

## What this changes

<!-- One or two sentences. What is different after this PR? -->

## Why

<!-- What problem does it solve? Link an issue if there is one. -->

---

## Checklist

Tick what applies. Delete what does not.

### All changes

- [ ] `Last updated` header bumped on every file I changed
- [ ] British English (organisation, licence, behaviour)
- [ ] No client-specific, confidential, or personal data
- [ ] No secrets, credentials, tokens, or internal URLs
- [ ] Relative links resolve (CI checks this, but a local look helps)

### Changes to legal or regulatory content

Required for anything under `eu-ai-act/`, `gdpr/`, or `dpia/`.

- [ ] Every new or changed claim cites a **primary source**: the Official Journal text, EUR-Lex, or supervisory authority guidance
- [ ] Article and paragraph numbers are specific, including the amending instrument where relevant
- [ ] The claim-to-source register is updated with the new or changed rows
- [ ] Where I relied on secondary commentary, I checked it against the enacted text before publishing
- [ ] Uncertainty is stated explicitly rather than smoothed over
- [ ] Anything I could not verify is flagged in the file and in the regulatory watchlist

> **On sourcing:** EUR-Lex web pages return HTTP 202 with an empty body to automated clients. The Publications Office CELLAR endpoint works:
>
> ```bash
> curl -H "Accept: application/xhtml+xml" http://publications.europa.eu/resource/celex/32026R1744
> ```

### New files

- [ ] Linked from `README.md` or a relevant index so it is discoverable
- [ ] Carries a `Last updated` header
- [ ] Ends with the informational-not-legal-advice line, if it makes legal claims

---

## Anything reviewers should look at closely?

<!-- Interpretation calls, places you were unsure, things you want a second opinion on. -->
