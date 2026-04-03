# Runbook

This repository is designed to be operated as a repeatable compliance workflow inside an AI-assisted workspace.

## Intended Usage

The normal operating model is:

1. Open [`START-HERE.md`](START-HERE.md)
2. Select the relevant workflow in `flows/`
3. Run the matching questionnaire in `questionnaires/`
4. Ground the analysis in `eu-ai-act/`, `gdpr/`, `dpia/`, and `resources/`
5. Produce a standard output from `outputs/`
6. Review trust and data-handling boundaries in `trust/` before using sensitive material

## Behavioral Expectations For Assistants

Assistants using this repo should:

- ask structured follow-up questions rather than guessing
- clearly mark assumptions
- avoid claiming legal certainty where ambiguity exists
- cite the repo source material and, where available, primary sources
- avoid overconfident “you are compliant” conclusions
- recommend escalation where high-impact rights, special-category data, or deployment risk is present

## Typical End-to-End Pattern

For a normal product team query:

1. Gather facts using `questionnaires/core-product-intake.md`
2. Run one or more flows
3. Produce a `source-backed-analysis`
4. If the output is being used for governance or delivery control, convert it into a `compliance-decision-record`
5. If unresolved issues remain, issue a `legal-escalation-note`

## Scope Boundary

This repo supports:

- structured analysis
- evidence-backed reasoning
- governance documentation
- intake and handoff discipline

This repo does not replace:

- legal advice
- organisational approval authority
- provider-side technical security review
- tenant-level privacy and retention controls in third-party AI tools
