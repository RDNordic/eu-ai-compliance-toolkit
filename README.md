# EU AI Compliance Toolkit

Turn Claude, Codex, and similar workspace assistants into structured EU AI Act and GDPR compliance operators for product teams.

This repository is designed to be cloned into a project workspace or used as a standalone compliance operating kit. It combines:

- guided intake and questionnaires
- repeatable compliance flows
- source-backed outputs
- trust and safe-usage boundaries
- practical legal reference material for the EU AI Act and GDPR

This is not an auto-certification tool and it is not legal advice. It is a serious working repo for teams that want governance to be usable, fast, and grounded.

## What This Repo Does

Use this repo to help an assistant:

- classify an AI use case under the EU AI Act
- assess GDPR lawful basis and Article 9 / Article 22 issues
- screen whether a DPIA is likely required
- review vendor risk and deployment readiness
- produce decision-ready outputs with assumptions, confidence, sources, and escalation points

The intended interaction model is progressive:

- start with a short fact pattern
- route to the right workflow
- collect only the missing facts that matter
- escalate to a fuller questionnaire when risk, uncertainty, or governance needs justify it

## Start Here

If you are using this repo with Claude, Codex, Cursor, or similar tools:

1. Open [`START-HERE.md`](START-HERE.md)
2. Tell your assistant what you want to do in a short fact pattern
3. Let it route you to the relevant workflow
4. Answer only the minimum follow-up questions needed
5. Use a full questionnaire only if the issue is material, ambiguous, or heading toward a decision record
6. Review the output and any legal escalation points

Suggested starting format:

- what the product or use case does
- who the users are
- what AI does in the workflow
- what data is involved
- what outcome or decision you need help with

Supporting files:

- [`RUNBOOK.md`](RUNBOOK.md)
- [`playbooks/claude-code.md`](playbooks/claude-code.md)
- [`playbooks/codex.md`](playbooks/codex.md)
- [`playbooks/cursor.md`](playbooks/cursor.md)

## Core Workflows

- [`flows/classify-ai-system.md`](flows/classify-ai-system.md)
- [`flows/check-gdpr-basis.md`](flows/check-gdpr-basis.md)
- [`flows/dpia-screen.md`](flows/dpia-screen.md)
- [`flows/vendor-risk-review.md`](flows/vendor-risk-review.md)
- [`flows/release-governance-check.md`](flows/release-governance-check.md)

## Questionnaires

- [`questionnaires/core-product-intake.md`](questionnaires/core-product-intake.md)
- [`questionnaires/recruitment-ai.md`](questionnaires/recruitment-ai.md)
- [`questionnaires/public-sector-chatbot.md`](questionnaires/public-sector-chatbot.md)
- [`questionnaires/vendor-ai-tooling.md`](questionnaires/vendor-ai-tooling.md)

## Standard Outputs

- [`outputs/compliance-decision-record.md`](outputs/compliance-decision-record.md)
- [`outputs/source-backed-analysis.md`](outputs/source-backed-analysis.md)
- [`outputs/legal-escalation-note.md`](outputs/legal-escalation-note.md)
- [`outputs/executive-summary.md`](outputs/executive-summary.md)

## Worked Examples

- [`examples/recruitment-ai-case.md`](examples/recruitment-ai-case.md)
- [`examples/public-sector-chatbot-case.md`](examples/public-sector-chatbot-case.md)
- sample outputs in [`examples/output-samples/`](examples/output-samples/)

## Launch Prompts

For copy-paste prompts that help new users start quickly, see:

- [`LAUNCH-PROMPTS.md`](LAUNCH-PROMPTS.md)

## Practical Assets

- checklists in [`checklists/`](checklists/)
- prompt packs in [`prompts/`](prompts/)
- official sources in [`resources/official-links.md`](resources/official-links.md)

## Trust And Safe Use

Read these before sharing sensitive material with any AI tool:

- [`trust/SECURITY.md`](trust/SECURITY.md)
- [`trust/PRIVACY.md`](trust/PRIVACY.md)
- [`trust/SAFE-USAGE.md`](trust/SAFE-USAGE.md)
- [`trust/TRUST-BOUNDARIES.md`](trust/TRUST-BOUNDARIES.md)
- [`trust/THREAT-MODEL.md`](trust/THREAT-MODEL.md)

These files are part of the product, not afterthoughts. The repo itself is low-risk markdown content. The real operational risk depends on what users paste into an AI tool, which provider they use, and what permissions that tool has in their environment.

## Knowledge Base

The flows above are grounded in the existing legal core:

| Folder | Contents |
|--------|----------|
| [`eu-ai-act/`](eu-ai-act/) | Risk classification reference, obligations by role, application dates |
| [`gdpr/`](gdpr/) | Lawful basis decision tree, recruitment guidance |
| [`dpia/`](dpia/) | AI-specific DPIA template and checklist material |
| [`resources/`](resources/) | Maintenance templates and official source support material |
| [`agents/`](agents/) | Reusable assistant instructions and task templates |
| [`starter-pack/`](starter-pack/) | Copy-ready controls for embedding compliance in product repos |

## Who This Is For

- Product teams deploying AI systems in or into the EU market
- Compliance and legal teams who want structured, reproducible analysis
- AI builders who need practical governance, not policy theater
- Procurement and vendor-management teams assessing external AI tools

## Geographic Scope

This repo is written primarily for:

- EU GDPR: Regulation (EU) 2016/679
- EU AI Act: Regulation (EU) 2024/1689

It is most directly relevant to EU and EEA contexts, and may also matter for non-EU organisations with extraterritorial exposure.
For EEA countries such as Norway, local applicability of the EU AI Act may depend on separate incorporation and timing, so users should confirm current national status where that matters.

## Business Use

This open repo is intended to be usable on its own, but it also supports tailored implementation work such as:

- organisation-specific questionnaires
- internal governance workflow design
- evidence register setup
- sector-specific compliance packs
- ongoing regulatory update and review support

## Important Limits

- This repo does not make an organisation compliant by itself.
- Assistant outputs still require human review.
- Legal uncertainty should be surfaced, not hidden.
- High-impact or jurisdiction-sensitive decisions should be escalated to qualified counsel.

## How To Contribute

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

## Feedback

If you notice an error, outdated source, or major gap, open an issue:

- https://github.com/RDNordic/eu-ai-compliance-toolkit/issues

## Licence

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

## Disclaimer

This toolkit is provided for informational purposes only and does not constitute legal, regulatory, or professional advice. Organisations should seek qualified legal counsel for decisions specific to their circumstances.
