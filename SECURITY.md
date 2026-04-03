# Security Policy

This repository is a markdown-first compliance operating kit. It does not include an installer, background service, or telemetry component.

## Main Security Note

The main security and privacy risk is usually not the repo itself. It is how users operate external AI tools around the repo, including:

- what information they paste into prompts
- what files the assistant can access
- what provider or tenant settings are enabled
- whether generated outputs are reviewed before operational use

## Before Use

Review:

- [`trust/SECURITY.md`](trust/SECURITY.md)
- [`trust/PRIVACY.md`](trust/PRIVACY.md)
- [`trust/SAFE-USAGE.md`](trust/SAFE-USAGE.md)
- [`trust/TRUST-BOUNDARIES.md`](trust/TRUST-BOUNDARIES.md)
- [`trust/THREAT-MODEL.md`](trust/THREAT-MODEL.md)

## Reporting Concerns

If you identify a material issue in the repository content or its safe-use guidance, open an issue with enough detail to reproduce the concern.
