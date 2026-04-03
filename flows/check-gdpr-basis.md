# Flow: Check GDPR Basis

Use this flow to identify candidate lawful bases, Article 9 issues, and Article 22 concerns for an AI-related processing activity.

## Use When

- personal data is used to train, fine-tune, evaluate, monitor, or operate an AI system
- there is uncertainty about lawful basis by processing stage
- the system may contribute to decisions affecting individuals

## Inputs To Collect

Start with:

- [`questionnaires/core-product-intake.md`](../questionnaires/core-product-intake.md)

Collect additional detail on:

- processing stages
- data categories
- whether special-category or criminal-offence data is involved
- whether outputs produce legal or similarly significant effects
- human review points
- retention and international transfer assumptions

For recruitment use cases, also use:

- [`../questionnaires/recruitment-ai.md`](../questionnaires/recruitment-ai.md)

## Source Base

Ground the analysis in:

- [`../gdpr/lawful-basis-decision-tree.md`](../gdpr/lawful-basis-decision-tree.md)
- [`../gdpr/recruitment-automated-decision-guidance.md`](../gdpr/recruitment-automated-decision-guidance.md)

## Required Output

Default to:

- [`../outputs/source-backed-analysis.md`](../outputs/source-backed-analysis.md)

If important ambiguities remain, also produce:

- [`../outputs/legal-escalation-note.md`](../outputs/legal-escalation-note.md)

## Output Must Include

- candidate lawful basis by stage
- Article 9 condition screen
- Article 22 screen
- assumptions and fact gaps
- operational safeguards needed
- confidence level
- escalation points

## Escalate If

- special-category data is central to the use case
- automated decisions may significantly affect individuals
- recruitment or employment context is involved
- the proposed basis relies on weak consent assumptions
