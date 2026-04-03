# Start Here

Use this file as the operating entrypoint for the repository.

If you are an AI assistant working in this repo, do not start by dumping a generic explanation. Route the user into a concrete workflow.

## First Step

Ask the user what they want to do:

- classify an AI system under the EU AI Act
- check GDPR lawful basis and special-category issues
- screen whether a DPIA is likely required
- review an AI vendor or external tool
- prepare a release or deployment governance check
- understand privacy, security, or trust boundaries before using this repo

If the user is unsure, start with [`questionnaires/core-product-intake.md`](questionnaires/core-product-intake.md).

## Operating Rules

When running any workflow:

1. Collect missing facts through the relevant questionnaire.
2. State assumptions explicitly.
3. Separate confirmed facts from inference.
4. Use the domain documents in `eu-ai-act/`, `gdpr/`, and `dpia/` as the legal knowledge base.
5. Produce one of the standard outputs from `outputs/`.
6. Include source references, confidence level, and escalation points.
7. If the user asks about safety, privacy, or data exposure, route to `trust/` before proceeding.

## Routing Table

Use this mapping:

- AI Act classification: [`flows/classify-ai-system.md`](flows/classify-ai-system.md)
- GDPR lawful basis: [`flows/check-gdpr-basis.md`](flows/check-gdpr-basis.md)
- DPIA screen: [`flows/dpia-screen.md`](flows/dpia-screen.md)
- Vendor review: [`flows/vendor-risk-review.md`](flows/vendor-risk-review.md)
- Release gate: [`flows/release-governance-check.md`](flows/release-governance-check.md)
- Trust / privacy / security questions: [`trust/TRUST-BOUNDARIES.md`](trust/TRUST-BOUNDARIES.md)

## Default Output Choice

Unless the user asks for a different format, produce:

- [`outputs/source-backed-analysis.md`](outputs/source-backed-analysis.md) for analysis work
- [`outputs/compliance-decision-record.md`](outputs/compliance-decision-record.md) for a decision artifact
- [`outputs/legal-escalation-note.md`](outputs/legal-escalation-note.md) if there are material unresolved legal issues

## Minimum Quality Bar

Every serious answer should include:

- objective
- facts provided
- assumptions
- analysis
- source basis
- confidence level
- open questions
- next action

## Important Limit

This repo does not itself transmit data anywhere, but the AI tool being used may do so depending on provider and configuration. Before processing confidential or personal data, review:

- [`trust/PRIVACY.md`](trust/PRIVACY.md)
- [`trust/SAFE-USAGE.md`](trust/SAFE-USAGE.md)
