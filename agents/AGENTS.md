# AGENTS.md (Template)

Define role-specialized sub-agents for compliance workflows.

## Agent Roles

### classification-agent
- Determines AI Act classification and obligations.
- Produces: tier decision, rationale, source links, open questions.

### gdpr-agent
- Evaluates lawful basis, Art. 9 conditions, Art. 22 triggers.
- Produces: basis options, risks, recommended path, source links.

### dpia-agent
- Drafts or reviews DPIA sections.
- Produces: risk table, mitigations, residual risk, escalation items.

### evidence-agent
- Maintains claim-source mapping.
- Produces: updated claim register entries with verification dates.

### governance-agent
- Runs release gate checks.
- Produces: go/no-go with blocking issues and remediation actions.

## Handoff Contract
Every handoff must include:
- Objective
- What is confirmed
- What is assumed
- Sources used
- Next action
