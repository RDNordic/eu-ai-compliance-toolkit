# Security

> **Last updated:** 2026-04-03

## What This Repo Is

This repository is primarily markdown guidance, questionnaires, templates, and operating instructions. It is intended to be low-risk to clone and inspect.

## What This Repo Is Not

This repo is not:

- an installer
- a background service
- a hosted platform
- a browser extension
- a telemetry agent

## Practical Security Boundary

The main security risk does not come from the markdown files themselves. It comes from how a user operates an external AI tool around this repo.

Examples:

- pasting confidential architecture into a third-party model
- granting a workspace assistant broad access to unrelated internal files
- relying on generated answers without internal review
- using outputs in production governance decisions without checking source and context

## Recommended Security Posture

- clone and inspect the repo before use
- review the `trust/` files before sharing sensitive material
- minimise the data you provide to any AI assistant
- use redacted or synthetic examples by default
- verify provider, tenant, and workspace permissions independently

## Reporting

See [`../SECURITY.md`](../SECURITY.md) for what is in scope and how to report it. Anything involving leaked secrets, credentials, or personal data should go to contact@rdnordic.com rather than a public issue.

Raise substantive issues in the repo content, trust framing, or operational guidance rather than assuming the repo silently “handles” it.
