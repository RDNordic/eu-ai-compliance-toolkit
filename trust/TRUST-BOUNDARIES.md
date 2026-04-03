# Trust Boundaries

This repo is useful only if users understand what it does and what it does not control.

## Boundary 1: The Repo

This repository controls:

- workflow structure
- questionnaires
- output templates
- compliance framing
- linked legal reference material

This repository does not control:

- provider-side data retention
- model training policies
- account-level security settings
- tenant configuration
- network transmission performed by your AI tool

## Boundary 2: The AI Tool

Your chosen AI assistant or coding tool may control:

- what context it reads
- what data it sends to the provider
- how long prompts or outputs are retained
- which tools or plugins are enabled
- whether content is used for model improvement

## Boundary 3: The User And Organisation

The user and organisation control:

- what data is shared
- what permissions are granted
- what workflows are followed
- whether outputs are reviewed
- whether legal or privacy escalation happens

## Practical Rule

Do not blame the markdown for decisions made at the tool, tenant, or organisational level. Review each boundary separately.
