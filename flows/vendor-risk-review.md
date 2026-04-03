# Flow: Vendor Risk Review

Use this flow to review an external AI vendor, AI-enabled SaaS product, or model provider before adoption.

## Use When

- a team wants to buy or trial an external AI tool
- procurement or security needs structured questions
- a deployer wants to understand upstream compliance dependencies

## Inputs To Collect

Start with:

- [`../questionnaires/vendor-ai-tooling.md`](../questionnaires/vendor-ai-tooling.md)

Add any known facts on:

- processing location
- model provider chain
- retention defaults
- training on customer prompts or content
- subcontractors and support access
- available customer controls

## Source Base

Ground the analysis in:

- [`../starter-pack/ai-act-classification-check.md`](../starter-pack/ai-act-classification-check.md)
- [`../starter-pack/dpia-minimum.md`](../starter-pack/dpia-minimum.md)
- [`../starter-pack/compliance-gate.md`](../starter-pack/compliance-gate.md)

## Required Output

Default to:

- [`../outputs/source-backed-analysis.md`](../outputs/source-backed-analysis.md)

## Output Must Include

- vendor risk summary
- missing due-diligence answers
- GDPR and AI Act dependency points
- recommended go / no-go / conditional-go view
- contract or procurement follow-ups
- confidence level

## Escalate If

- vendor cannot explain retention, training, or subprocessors
- special-category or large-scale personal data is expected
- the tool will materially influence important decisions
