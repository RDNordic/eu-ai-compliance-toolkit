# Worked Example: Recruitment AI Screening Tool

This example shows how a team might use the repo to assess a hiring-support tool that ranks candidates before human review.

## Scenario

A company wants to use an AI-assisted recruitment tool that:

- ingests CVs and application forms
- scores candidates against role criteria
- suggests a ranked shortlist to recruiters
- allows recruiters to review the shortlist before inviting candidates to interview

The company is based in Europe and plans to use the tool for multiple roles across business units.

## Why This Example Matters

Recruitment is a good stress test because it can trigger:

- AI Act classification questions
- GDPR lawful basis concerns
- Article 22 issues
- weak consent assumptions in employment contexts
- DPIA screening questions

## Suggested Starting Prompt

“Use `START-HERE.md` in this repo. I need to assess an AI recruitment tool that scores and ranks candidates before recruiter review. Ask me the minimum questions needed to classify it under the EU AI Act, assess GDPR lawful basis and Article 22 concerns, and screen whether a DPIA is likely required. Output a source-backed analysis and a short decision record.”

## Likely Questionnaire Path

Start with:

- [`../questionnaires/core-product-intake.md`](../questionnaires/core-product-intake.md)
- [`../questionnaires/recruitment-ai.md`](../questionnaires/recruitment-ai.md)

Typical questions the assistant should ask:

- Does the system rank or screen out candidates
- What practical effect does the score have
- Can recruiters meaningfully override the result
- What data is used
- Is any special-category data present or inferred
- Is the tool developed internally or supplied by a vendor
- What lawful basis is currently assumed

## Likely Workflow Path

- [`../flows/classify-ai-system.md`](../flows/classify-ai-system.md)
- [`../flows/check-gdpr-basis.md`](../flows/check-gdpr-basis.md)
- [`../flows/dpia-screen.md`](../flows/dpia-screen.md)

## Example Fact Pattern

- Role: likely deployer, with possible controller responsibilities for candidate data
- Purpose: prioritise and shortlist candidates for recruiter review
- Users: internal recruitment staff
- Affected persons: job applicants
- Data: CV content, work history, education, screening responses, possible interview notes
- Significant effect risk: yes, because outputs may affect progression in a hiring process
- Human review: yes, but practical override quality is uncertain
- Vendor: external SaaS provider
- Special-category data: not intentionally collected, but may appear in CVs

## Example Analysis Shape

Likely output themes:

- AI Act: recruitment-related use case may trigger high-risk analysis depending on the function and deployment context
- GDPR: consent is likely a weak basis in an employment context; the assistant should test more defensible basis reasoning by processing stage
- Article 22: the assistant should assess whether practical reliance on the tool leads to decisions with similarly significant effects
- DPIA: likely strong case for a DPIA screen and probably a fuller DPIA if the tool materially influences candidate progression

## Example Output Excerpt

Not a final legal conclusion, but a realistic output summary:

- Objective: assess recruitment screening tool before procurement approval
- Facts provided: tool ranks candidates and informs shortlist creation
- Assumptions: recruiters can review outputs, but override is not yet evidenced in process design
- Analysis: heightened AI Act and GDPR risk due to employment context and significant effect potential
- Source basis: risk classification guide, lawful basis decision tree, recruitment guidance, DPIA template
- Confidence level: medium
- Open questions: actual override design, scoring logic transparency, vendor retention and training terms
- Recommended next action: do not approve deployment until vendor due diligence and DPIA screening are completed

## Example Decision Record Outcome

Plausible result:

- Decision: conditional go for further assessment, not production approval
- Required actions:
  - confirm actual human review safeguards
  - assess whether Article 22 is engaged in practice
  - complete vendor review
  - complete DPIA screening
  - document lawful basis by processing stage

## Why This Is Useful In Public

This example shows that the repo is not just “a prompt pack.” It demonstrates an actual governance flow that a product or HR-adjacent team can understand immediately.
