# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2026-07-31

Regulatory currency release. Brings the legal core in line with Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026.

### Changed
- **`eu-ai-act/application-dates.md` rewritten.** Annex III high-risk obligations 2026-08-02 to **2027-12-02**; Annex I / Art. 6(1) 2027-08-02 to **2028-08-02**; AI regulatory sandboxes 2026-08-02 to **2027-08-02**. Art. 50 transparency confirmed **unchanged** at 2026-08-02.
- **`eu-ai-act/risk-classification.md` updated** for the amended dates, the two new Art. 5 prohibitions (CSAM and non-consensual intimate imagery, transitional deadline 2026-12-02), the narrowed "safety component" test for embedded AI, the Art. 10(5) bias-detection extension to deployers, retained Art. 49 registration, and widened AI Office supervision.
- Regulatory watchlist and claim-to-source register in `risk-classification.md` populated with real entries, replacing empty templates.
- Worked examples given explicit timing notes distinguishing the delayed high-risk deadlines from the live Art. 50 duty.
- `source-update/README.md` and `source-update/CLAUDE.md` corrected. Setup instructions referenced `intake/questions/v0.yml`, `intake/templates/`, and `evidence-packs/example-municipality/triage-summary.md`, none of which existed; the quickstart could not be followed as written.

### Added
- **`eu-ai-act/omnibus-2026-changes.md`** transition guide: what moved, what did not, and the Article 50 trap.
- **`eu-ai-act/obligations-by-role.md`** mapping provider, deployer, importer, distributor, authorised representative, and GPAI provider duties, including the Art. 25 role-shift rules. This file was referenced by `README.md` but had never existed.

### Removed
- `gitignore.md`, an internal trial-planning note naming a third party, committed to the public repo under a misleading filename.

### Verification
- **All regulatory claims in `eu-ai-act/` are primary-source verified** against the Official Journal texts of Regulation (EU) 2026/1744 (CELEX 32026R1744) and Regulation (EU) 2024/1689, checked 2026-07-31. The claim-to-source register now cites the specific amending provision for each claim.
- Two corrections were made where widely repeated secondary reporting diverged from the enacted text:
  - The bias-detection change is a **deletion of Art. 10(5) and insertion of a new free-standing Art. 4a**, not an extension of Art. 10(5). Art. 4a(2) reaches deployers and non-high-risk systems, on six cumulative conditions, and creates no obligation.
  - **Art. 49 was not amended.** The registration burden was reduced by deleting Annex VIII Section B points 7 and 9.
- Additional detail recovered from the enacted text and now documented: the deferral covers **Chapter III Sections 1, 2 and 3 only, expressly excepting Art. 6(5)**; Arts. 102-110 applied from **27 July 2026**; Art. 111(2) grandfathering was re-keyed to the date of application of Chapter III; Art. 111(1) and the 2030-12-31 Annex X deadline were **not** amended; Annex I Section A point 1 was deleted and machinery moved to Annex I Section B; Art. 75(1) gives the AI Office **exclusive** competence over same-undertaking GPAI-based systems and VLOP/VLOSE-integrated systems.

### Known open items
- Whether **Chapter III Section 5** (Arts. 40-49: standards, conformity assessment, certificates, registration) falls outside the deferral and therefore applies from 2026-08-02. This is an interpretation question, not a sourcing gap, and is flagged in `application-dates.md` and the regulatory watchlist.
- Retention periods and thresholds in `obligations-by-role.md` are simplified and not individually verified.

### Maintainer note
- EUR-Lex web pages return HTTP 202 with an empty body to automated clients. The Publications Office CELLAR endpoint is the reliable programmatic route: `curl -H "Accept: application/xhtml+xml" http://publications.europa.eu/resource/celex/32026R1744`

## [0.2.0] - 2026-02-17

### Added
- `HOW-TO-USE.md` with 3 usage modes (library, copilot, project-embed)
- `agents/` pack:
  - `agents/CLAUDE.md`
  - `agents/AGENTS.md`
  - `agents/SYSTEM-PROMPT.md`
  - `agents/OUTPUT-FORMAT.md`
  - `agents/TASK-TEMPLATES.md`
- `starter-pack/` controls:
  - `starter-pack/compliance-gate.md`
  - `starter-pack/dpia-minimum.md`
  - `starter-pack/ai-act-classification-check.md`
  - `starter-pack/claim-source-register.csv`
- `intake/use-case-template.md` for structured project intake

### Changed
- Updated `README.md` to surface AI integration and embed options

## [0.1.0] - 2026-02-17

### Added
- Initial release
- EU AI Act risk classification quick reference
- GDPR lawful basis decision tree for AI/ML processing
- DPIA template for AI systems
- README, CONTRIBUTING, and LICENCE files
