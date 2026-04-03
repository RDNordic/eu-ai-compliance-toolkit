# How To Use This Repo

This repository is now structured as a portable compliance operating kit for AI-assisted work.

## Fastest Way To Use It

1. Open [`START-HERE.md`](START-HERE.md)
2. Tell your assistant what you need
3. Let it run the relevant questionnaire from `questionnaires/`
4. Let it follow the matching file in `flows/`
5. Require an output from `outputs/`
6. Review `trust/` before sharing sensitive material

## Usage Modes

## 1) Runtime Mode

Best for teams using Claude, Codex, Cursor, or similar tools directly in a workspace.

Key files:

- [`START-HERE.md`](START-HERE.md)
- [`RUNBOOK.md`](RUNBOOK.md)
- [`flows/`](flows/)
- [`questionnaires/`](questionnaires/)
- [`outputs/`](outputs/)
- [`playbooks/`](playbooks/)
- [`trust/`](trust/)

## 2) Library Mode

Best for legal, privacy, or governance teams that want to read and apply the source material directly.

Core reference files:

- [`eu-ai-act/risk-classification.md`](eu-ai-act/risk-classification.md)
- [`eu-ai-act/application-dates.md`](eu-ai-act/application-dates.md)
- [`gdpr/lawful-basis-decision-tree.md`](gdpr/lawful-basis-decision-tree.md)
- [`gdpr/recruitment-automated-decision-guidance.md`](gdpr/recruitment-automated-decision-guidance.md)
- [`dpia/ai-dpia-template.md`](dpia/ai-dpia-template.md)

## 3) Project-Embed Mode

Best for product teams that want to copy controls into their own repositories.

Start from:

- [`starter-pack/compliance-gate.md`](starter-pack/compliance-gate.md)
- [`starter-pack/dpia-minimum.md`](starter-pack/dpia-minimum.md)
- [`starter-pack/ai-act-classification-check.md`](starter-pack/ai-act-classification-check.md)
- [`starter-pack/claim-source-register.csv`](starter-pack/claim-source-register.csv)

## Minimum Quality Rule

Any serious compliance output should include:

- facts provided
- assumptions
- source basis
- confidence level
- open legal or factual questions
- next action

## Important

This repo is informational and operationally useful, but it is not legal advice and it does not automatically make an organisation compliant.
