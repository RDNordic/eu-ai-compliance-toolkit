# Sample Output: Recruitment Decision Record

## Objective

Record the current governance position for a proposed AI recruitment screening tool before procurement or deployment approval.

## System Or Project Name

Recruitment scoring and shortlist support tool.

## Date

Example only. Insert actual review date.

## Prepared By

Example repo workflow output.

## Facts Confirmed

- The tool ranks candidates for recruiter review.
- The deployment context is recruitment and hiring.
- An external vendor provides the tool.
- Human review exists in principle before interview decisions.

## Assumptions

- The organisation is acting as deployer and controller.
- Human review is intended but not yet evidenced as meaningful in operational design.
- Candidate data may include incidental special-category information.

## Applicable Workflow(s)

- [`../../flows/classify-ai-system.md`](../../flows/classify-ai-system.md)
- [`../../flows/check-gdpr-basis.md`](../../flows/check-gdpr-basis.md)
- [`../../flows/dpia-screen.md`](../../flows/dpia-screen.md)

## Key Conclusions

- The use case requires heightened governance review.
- Employment context increases the chance of significant-effect and fairness concerns.
- Current information is not sufficient for production approval.

## Sources Used

- [`../../eu-ai-act/risk-classification.md`](../../eu-ai-act/risk-classification.md)
- [`../../gdpr/lawful-basis-decision-tree.md`](../../gdpr/lawful-basis-decision-tree.md)
- [`../../gdpr/recruitment-automated-decision-guidance.md`](../../gdpr/recruitment-automated-decision-guidance.md)
- [`../../dpia/ai-dpia-template.md`](../../dpia/ai-dpia-template.md)

## Confidence Level

Medium.

## Open Legal Or Factual Questions

- Whether Article 22 is engaged in the real workflow
- Whether special-category data is screened or used
- Whether vendor retention and training settings are acceptable
- Whether candidate transparency is adequate

## Decision

Conditional go for further assessment only. Not approved for production deployment.

## Required Actions Before Next Stage

- run formal vendor due diligence
- document lawful basis by stage
- complete DPIA screening
- confirm meaningful human review safeguards
- record escalation points for unresolved legal issues

## Owner And Review Date

Assign product owner, HR owner, privacy/legal reviewer, and next review date before moving forward.
