# Flow: DPIA Screen

Use this flow to decide whether a DPIA is likely required and to prepare the structure for a fuller DPIA if needed.

## Use When

- a new AI use case is entering design, procurement, pilot, or deployment
- personal data processing may create elevated risk to individuals
- the team needs an early escalation signal before release

## Inputs To Collect

Start with:

- [`questionnaires/core-product-intake.md`](../questionnaires/core-product-intake.md)

Then collect:

- system description
- main data flows
- affected individuals
- potential harms and error modes
- safeguards already in place
- whether the system supports profiling, monitoring, or significant decisions

## Source Base

Ground the analysis in:

- [`../dpia/ai-dpia-template.md`](../dpia/ai-dpia-template.md)
- [`../gdpr/lawful-basis-decision-tree.md`](../gdpr/lawful-basis-decision-tree.md)

## Required Output

Default to:

- [`../outputs/source-backed-analysis.md`](../outputs/source-backed-analysis.md)

If the organisation needs a record for governance, also produce:

- [`../outputs/compliance-decision-record.md`](../outputs/compliance-decision-record.md)

## Output Must Include

- likely DPIA trigger assessment
- key risk drivers
- mitigations already present
- gaps requiring work before deployment
- whether prior consultation may need review
- confidence level
- next action

## Escalate If

- risk remains high after proposed mitigations
- significant effects on individuals are plausible
- sensitive data or vulnerable groups are involved
- public-sector or employment contexts are involved
