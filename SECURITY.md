# Security Policy

> **Last updated:** 2026-07-31

This is the repository's security **reporting** policy. For the substantive guidance on operating this toolkit safely, see [`trust/SECURITY.md`](trust/SECURITY.md) and the rest of [`trust/`](trust/).

## Scope

This repository is markdown content: guidance, questionnaires, templates, and operating instructions. It ships no installer, executable, background service, or telemetry component. The only executable code is the maintenance workflow in [`.github/`](.github/).

Because of that, the security issues that matter here differ from a typical software project:

| In scope | Out of scope |
|---|---|
| Content that could mislead a user into unsafely disclosing personal or confidential data | Vulnerabilities in third-party AI tools used to operate this repo |
| Prompt or instruction content that could cause an assistant to behave unsafely | Your organisation's own tenant, provider, or workspace configuration |
| Leaked secrets, credentials, or personal data in the repository or its history | General AI model behaviour |
| Broken or misleading trust, privacy, or safe-use guidance | Legal accuracy issues, which are content issues |
| Supply-chain issues in the GitHub Actions workflows | |

Legal or regulatory inaccuracy is a content issue, not a security issue. Report it using the outdated-legal-content issue template.

## Reporting

**For leaked secrets, credentials, or personal data:** do not open a public issue. Email **contact@rdnordic.com** with the detail.

**For everything else in scope:** [open an issue](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues) with enough detail to reproduce the concern.

There is no bug bounty for this repository.

## The Main Risk Is Not This Repository

The repo is low-risk to clone and inspect. The real operational risk depends on what users paste into an AI tool, which provider they use, and what permissions that tool holds in their environment.

Read these before sharing sensitive material with any AI tool:

- [`trust/SECURITY.md`](trust/SECURITY.md)
- [`trust/PRIVACY.md`](trust/PRIVACY.md)
- [`trust/SAFE-USAGE.md`](trust/SAFE-USAGE.md)
- [`trust/TRUST-BOUNDARIES.md`](trust/TRUST-BOUNDARIES.md)
- [`trust/THREAT-MODEL.md`](trust/THREAT-MODEL.md)
