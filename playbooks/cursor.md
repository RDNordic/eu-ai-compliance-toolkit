# Playbook: Cursor

Use this repo in Cursor or similar editor-native assistants by keeping the full repository in workspace context and working from [`../START-HERE.md`](../START-HERE.md).

## Recommended Pattern

1. Ask the assistant to follow `START-HERE.md`
2. Tell it which workflow you want
3. Let it ask questions from `questionnaires/`
4. Require output in one of the `outputs/` formats

## Watchouts

- Editor-native tools may have broad file access depending on configuration.
- Review what other project files are in workspace context before discussing confidential matters.
- If your project contains sensitive code or personal data, review `trust/SAFE-USAGE.md` first.
