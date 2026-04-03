# Playbook: Codex

Use this repo in a Codex workspace by asking the assistant to treat the repository as an operating kit rather than just a document library.

## Recommended Pattern

1. Start from [`../START-HERE.md`](../START-HERE.md)
2. Route into the relevant file under `flows/`
3. Collect facts from `questionnaires/`
4. Produce an artifact from `outputs/`
5. Review `trust/` before processing sensitive material

## Good Prompt

“Use this repo as a compliance runtime. Start with `START-HERE.md`, ask me the right intake questions, then run the GDPR and AI Act workflows and produce a source-backed analysis.”

## Watchouts

- The repo does not override workspace permissions or provider behavior.
- The main privacy risk is what users supply to the tool, not the markdown itself.
- Ask for explicit assumptions instead of filling gaps with confident guesses.
