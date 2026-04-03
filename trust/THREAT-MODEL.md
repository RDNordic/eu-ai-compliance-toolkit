# Threat Model

This is a lightweight threat model for using this repository with AI assistants.

## Main Threats

### 1. Accidental Disclosure

Users paste confidential or personal data into an AI tool without understanding provider-side handling.

### 2. Over-Broad Workspace Exposure

The assistant has access to unrelated files in the workspace that contain sensitive information.

### 3. False Confidence

Generated outputs are treated as definitive legal approval rather than assisted analysis.

### 4. Stale Or Incomplete Legal Reasoning

The repo or the assistant output is used without verifying timing, jurisdiction, or evolving authority guidance.

### 5. Unsafe Reuse

A team copies an output into governance documentation without checking whether assumptions still hold.

## Main Mitigations

- use redacted or synthetic facts first
- review tool permissions and provider terms
- require assumptions and confidence levels in outputs
- require source-backed reasoning
- use escalation notes when uncertainty remains
- review high-impact use cases with counsel or formal governance functions

## Residual Risk

Residual risk remains whenever users share sensitive data with external AI tools or rely on outputs without internal review. This repo reduces chaos and improves discipline. It does not eliminate operational or legal risk.
