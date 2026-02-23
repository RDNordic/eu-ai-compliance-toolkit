# How To Use This Repo

This repository supports three practical usage modes.

## 1) Library Mode (read and apply)
Best for legal/compliance teams who want guidance and templates.

Steps:
1. Start in `README.md`.
2. Use `eu-ai-act/risk-classification.md` for classification.
3. Use `gdpr/lawful-basis-decision-tree.md` for lawful basis analysis.
4. Use `dpia/ai-dpia-template.md` for DPIA work.

## 2) Copilot Mode (connect your AI assistant)
Best for teams using Claude, Codex, or similar tools in a project workspace.

Use these files:
- `agents/CLAUDE.md`
- `agents/AGENTS.md`
- `agents/SYSTEM-PROMPT.md`
- `agents/TASK-TEMPLATES.md`

How to apply:
1. Copy these files into your project root (or merge into your existing assistant instructions).
2. Keep this repo available to your assistant as reference material.
3. Require output in the format defined in `agents/OUTPUT-FORMAT.md`.

## 3) Project-Embed Mode (copy starter controls)
Best for product teams that need compliance controls in delivery flow.

Copy from `starter-pack/` into your project:
- `compliance-gate.md`
- `dpia-minimum.md`
- `ai-act-classification-check.md`
- `claim-source-register.csv`

## Minimum Quality Rule (all modes)
Any compliance output should include:
- Claim summary
- Source link(s)
- Jurisdiction assumptions
- Confidence level
- Open legal questions

## Important
This toolkit is informational and not legal advice. Use qualified legal counsel for decisions with legal or regulatory impact.
