# EU AI Compliance Toolkit — Claude Code Quickstart

This folder contains everything you need to run the EU AI Compliance Toolkit as an agentic intake session using Claude Code CLI in VS Code.

Maintained by R&D Nordic Consultancy | https://github.com/RDNordic/eu-ai-compliance-toolkit

---

## What is this?

Instead of reading documents and filling in templates manually, you connect Claude directly to the toolkit's knowledge base and run a guided compliance intake session in your terminal. Claude asks the questions, interprets the answers against the EU AI Act and GDPR, flags risks in real time, and writes a structured evidence pack to your repo.

This is what "hook up your own AI, stay compliant" means in practice.

---

## Files in this folder

| File | Where it goes in your repo | What it does |
|------|---------------------------|--------------|
| `CLAUDE.md` | Repo root | Tells Claude Code how to behave, which modes to run, and what to produce |
| `intake/questions/v0.yml` | `intake/questions/v0.yml` | The question set Claude works through during a session |
| `evidence-packs/example-municipality/triage-summary.md` | `evidence-packs/example-municipality/triage-summary.md` | A worked example showing the expected triage output format |

---

## Setup (one-time)

**1. Install Claude Code CLI**

If you have not already done so:

```bash
npm install -g @anthropic-ai/claude-code
```

Requires Node 18 or later. Authenticate with your Anthropic account when prompted.

**2. Copy files into your repo**

Place each file at the path shown in the table above. The folder structure should look like this:

```
your-repo/
├── CLAUDE.md                          ← drop here
├── intake/
│   └── questions/
│       └── v0.yml                     ← drop here
└── evidence-packs/
    └── example-municipality/
        └── triage-summary.md          ← drop here
```

**3. Open your repo in VS Code and start Claude Code**

```bash
cd your-repo
claude
```

Claude Code reads `CLAUDE.md` automatically on startup. No additional configuration is needed.

---

## Running a session

Once Claude Code is running, start with a plain-language instruction. Examples:

- "I want to run a compliance triage for a new AI system."
- "Run a full compliance pack for our procurement tool."
- "Show me the example triage output before we start."

Claude will ask whether you want triage mode (15 minutes, key risk flags) or full pack mode (30-60 minutes, audit-ready evidence set), then work through the relevant questions one at a time.

---

## What Claude produces

### Triage mode

A single file written to:

```
evidence-packs/<your-project-slug>/triage-summary.md
```

Contains: system profile snapshot, provisional EU AI Act risk tier, DPIA trigger decision, top control gaps, and recommended next steps.

### Full pack mode

Seven files written to `evidence-packs/<your-project-slug>/`:

| File | Contents |
|------|----------|
| `system.yml` | System profile: purpose, users, deployment, vendors, data types |
| `ai-act-classification.md` | Risk tier decision record with article references |
| `roles-and-obligations.md` | Provider / deployer role mapping and required artefacts |
| `high-risk-flags.md` | Annex III domain flags and human oversight assessment |
| `dpia-triage.md` | DPIA required / not required / uncertain, with reasoning |
| `legal-basis-notes.md` | Lawful basis candidates and gaps for DPO review |
| `gap-register.md` | Prioritised list of gaps with owner and suggested deadline fields |

All files include a header with toolkit version, date, confidence level, and escalation flags.

---

## Customising the question set

Open `intake/questions/v0.yml` to adjust questions for your context. Key fields:

- `triage: true` — include this question in the 15-minute triage mode
- `risk_flag: true` — Claude surfaces this to the user immediately if it triggers
- `escalate: true` — Claude adds an explicit note that DPO or legal input is required
- `notes:` — internal guidance for Claude on how to interpret the answer

You do not need to touch `CLAUDE.md` to adjust question content.

---

## Worked example

Before running your first live session, review the municipality example:

```
evidence-packs/example-municipality/triage-summary.md
```

This shows a realistic triage output for a Norwegian municipality deploying an AI-assisted welfare case triage tool. It demonstrates the expected format, tone, confidence levels, and escalation flags.

---

## Important

Outputs from this toolkit are decision-support records, not legal opinions. Each output file includes a confidence level and explicit escalation gates. Any finding marked `escalation_required: true` must be reviewed by a qualified DPO or legal counsel before being relied upon.

This toolkit reflects the regulatory position as of the date shown in each document. Always verify against official sources before making compliance decisions.

**Regulation references:**
- EU AI Act: Regulation (EU) 2024/1689
- GDPR: Regulation (EU) 2016/679

---

## Feedback and issues

Open an issue at: https://github.com/RDNordic/eu-ai-compliance-toolkit/issues
Or email: contact@rdnordic.com
