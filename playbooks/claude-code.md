# Playbook: Claude Code

Use this repo in a Claude Code workspace by keeping the repository available to the assistant and starting from [`../START-HERE.md`](../START-HERE.md).

## Recommended Pattern

1. Tell Claude the outcome you want.
2. Ask it to follow `START-HERE.md`.
3. Let it run the relevant questionnaire before analysis.
4. Require one of the output templates in `outputs/`.
5. Review `trust/` before sharing sensitive content.

## Good Prompt

“Use `START-HERE.md` in this repo. Ask me the minimum questions needed to classify this use case and assess GDPR and DPIA implications. Output a source-backed analysis and a short decision record.”

## Watchouts

- Claude may still rely on provider-side handling rules outside this repo.
- Do not paste secrets or raw personal data without internal approval.
- If the answer affects legal rights, employment, public services, or sensitive data, require escalation points in the output.
