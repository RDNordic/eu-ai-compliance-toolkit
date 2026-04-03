# Worked Example: Public-Sector Service Chatbot

This example shows how a team might use the repo to assess a public-sector chatbot that helps citizens navigate services and submit requests.

## Scenario

A public body wants to deploy a chatbot on its website that:

- answers questions about available services
- helps users understand eligibility requirements
- collects intake details before routing a request to staff
- may suggest the most relevant form or service path

The chatbot is intended to reduce call-center load and improve access to information.

## Why This Example Matters

Public-sector use cases are useful because they raise questions around:

- public authority context
- access to services and rights
- vulnerable users
- DPIA and accountability expectations
- vendor and trust-boundary concerns

## Suggested Starting Prompt

“Use `START-HERE.md` in this repo. I need to assess a public-sector chatbot that helps citizens find services and routes requests to staff. Ask me the right intake questions, classify the use case under the EU AI Act, screen the GDPR and DPIA implications, and give me a source-backed analysis plus a decision record.”

## Likely Questionnaire Path

Start with:

- [`../questionnaires/core-product-intake.md`](../questionnaires/core-product-intake.md)
- [`../questionnaires/public-sector-chatbot.md`](../questionnaires/public-sector-chatbot.md)

Typical questions the assistant should ask:

- Does the tool only provide information or also shape access to services
- Are children or vulnerable persons likely users
- Does it access case-specific or authenticated data
- Are staff relying on it for triage or prioritization
- What logs are kept
- Is the solution vendor-supplied

## Likely Workflow Path

- [`../flows/classify-ai-system.md`](../flows/classify-ai-system.md)
- [`../flows/dpia-screen.md`](../flows/dpia-screen.md)
- optionally [`../flows/vendor-risk-review.md`](../flows/vendor-risk-review.md)

## Example Fact Pattern

- Role: likely deployer and controller for citizen interaction data
- Purpose: service navigation and early intake support
- Users: citizens and residents
- Affected persons: members of the public, potentially including vulnerable groups
- Data: contact details, free-text service questions, possible case-related context
- Human review: staff review routed requests after intake
- Vendor: external chatbot platform
- Significant effect risk: depends on whether the chatbot only informs or meaningfully influences access to services

## Example Analysis Shape

Likely output themes:

- AI Act: classification depends on whether the chatbot is merely informational or materially affects access, prioritization, or public decision processes
- GDPR: intake and routing may involve personal data and require clear role, purpose, minimisation, and retention analysis
- DPIA: strong case for a formal screen given public-sector context, citizen-facing deployment, and possible vulnerable-user impact
- Vendor review: important if the platform processes prompts, stores logs, or uses data for training

## Example Output Excerpt

- Objective: assess public-sector chatbot before pilot launch
- Facts provided: chatbot helps users find services and routes requests to staff
- Assumptions: final service decisions remain with human staff
- Analysis: moderate-to-high governance sensitivity due to public-sector setting and potential effect on access to services
- Source basis: risk classification guide, DPIA template, starter-pack controls
- Confidence level: medium
- Open questions: vendor retention, access-control model, logging scope, effect on vulnerable users
- Recommended next action: run DPIA screening and vendor review before launch approval

## Example Decision Record Outcome

Plausible result:

- Decision: conditional go for pilot only
- Required actions:
  - limit data collection
  - define staff override and review process
  - confirm vendor privacy and retention controls
  - complete DPIA screening
  - document public-facing transparency messaging

## Why This Is Useful In Public

This example broadens the repo beyond HR or private-sector use and shows direct relevance for public bodies, suppliers, and govtech teams.
