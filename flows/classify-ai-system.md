# Flow: Classify AI System

Use this flow to determine the likely EU AI Act classification of a use case and identify the immediate obligations that follow.

## Use When

- a team is designing or procuring an AI system
- the role of provider or deployer needs to be clarified
- someone needs to understand whether the use case is prohibited, high-risk, limited-risk, or minimal-risk

## Inputs To Collect

Start with:

- [`questionnaires/core-product-intake.md`](../questionnaires/core-product-intake.md)

Add these clarifiers if missing:

- intended purpose
- sector and deployment context
- who uses the system
- who is affected by outputs
- whether the system influences employment, education, essential services, law enforcement, migration, justice, or democratic processes
- whether emotion recognition, biometric categorisation, or remote biometric identification is involved

## Source Base

Ground the analysis in:

- [`../eu-ai-act/risk-classification.md`](../eu-ai-act/risk-classification.md)
- [`../eu-ai-act/application-dates.md`](../eu-ai-act/application-dates.md)

## Required Output

Default to:

- [`../outputs/source-backed-analysis.md`](../outputs/source-backed-analysis.md)

If a decision is being recorded for project governance, also produce:

- [`../outputs/compliance-decision-record.md`](../outputs/compliance-decision-record.md)

## Output Must Include

- likely classification
- role assumption
- article or annex references where available in the repo source material
- obligations triggered
- timing or applicability caveats
- confidence level
- open legal interpretation points
- next action

## Escalate If

- the use case may fall into a prohibited practice
- high-risk classification is plausible but factually uncertain
- biometric or public-sector use is implicated
- the organisation’s role is unclear
