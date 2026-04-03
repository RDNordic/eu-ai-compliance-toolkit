# Sample Output: Recruitment Source-Backed Analysis

## Objective

Assess an AI recruitment tool that scores and ranks candidates before recruiter review.

## Facts Provided

- The tool ingests CVs and screening responses.
- It generates candidate scores and a ranked shortlist.
- Recruiters review the shortlist before interview invitations are sent.
- The tool is supplied by an external vendor.
- The organisation is established in Europe and plans multi-team use.

## Assumptions

- The organisation acts at least as deployer under the EU AI Act and controller for candidate data under GDPR.
- Recruiters retain formal authority over interview decisions.
- Practical override quality has not yet been demonstrated in process design.
- Special-category data is not intentionally collected, but such data may appear in CVs.

## Analysis

The use case creates heightened governance sensitivity because it sits in an employment context and may materially influence candidate progression. The assistant should treat any claim that “humans stay in the loop” with caution unless the process shows meaningful review rather than rubber-stamping.

On the AI Act side, the use case should be screened carefully against the recruitment and employment-related risk logic in the repo materials. On the GDPR side, the main issues are lawful basis by processing stage, potential Article 22 implications if the ranking is relied upon in practice, and the handling of special-category data that may appear incidentally in application materials.

A DPIA screen is strongly indicated. Vendor due diligence is also necessary before deployment approval because retention, training-on-customer-data, and transparency practices can materially change the compliance posture.

## Source Basis

- [`../../eu-ai-act/risk-classification.md`](../../eu-ai-act/risk-classification.md)
- [`../../gdpr/lawful-basis-decision-tree.md`](../../gdpr/lawful-basis-decision-tree.md)
- [`../../gdpr/recruitment-automated-decision-guidance.md`](../../gdpr/recruitment-automated-decision-guidance.md)
- [`../../dpia/ai-dpia-template.md`](../../dpia/ai-dpia-template.md)

## Confidence Level

Medium.

## Open Questions

- Does the tool screen out candidates automatically at any stage
- How meaningful is recruiter override in practice
- What vendor retention and training defaults apply
- What transparency is given to candidates
- Whether the organisation has documented lawful basis by stage

## Recommended Next Action

Do not approve production deployment yet. Complete a vendor review, document lawful basis by processing stage, run a DPIA screen, and verify whether the human-review process is actually meaningful.
