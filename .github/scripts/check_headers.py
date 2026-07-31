#!/usr/bin/env python3
"""Verify that every Markdown document carries a valid `Last updated` header.

CONTRIBUTING.md requires a Last updated date on each document. For a compliance
toolkit this is not cosmetic: a reader needs to know how old a legal claim is
before relying on it.

Format expected within the first 8 lines:

    > **Last updated:** YYYY-MM-DD

Exit code 0 if every file conforms, 1 otherwise.
"""

import datetime
import io
import os
import re
import subprocess
import sys

# Files legitimately without a Last updated header.
EXEMPT = {
    "CHANGELOG.md",              # every entry is individually dated
    "source-update/triage-summary.md",  # dated artefact, carries `generated:` in front matter
    ".github/PULL_REQUEST_TEMPLATE.md",
}

HEADER = re.compile(r"Last updated:?\*{0,2}\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
LOOSE = re.compile(r"Last updated", re.IGNORECASE)


def tracked_markdown():
    out = subprocess.check_output(["git", "ls-files", "*.md"], text=True)
    return [line.strip() for line in out.splitlines() if line.strip()]


def main() -> int:
    missing = []
    malformed = []
    future = []
    today = datetime.date.today()

    for path in tracked_markdown():
        rel = path.replace(os.sep, "/")
        if rel in EXEMPT:
            continue
        try:
            head = io.open(path, encoding="utf-8-sig").read().split("\n")[:8]
        except OSError as exc:
            malformed.append((rel, str(exc)))
            continue

        block = "\n".join(head)
        match = HEADER.search(block)
        if not match:
            if LOOSE.search(block):
                malformed.append((rel, "header present but not in YYYY-MM-DD form"))
            else:
                missing.append(rel)
            continue

        try:
            stamped = datetime.date.fromisoformat(match.group(1))
        except ValueError:
            malformed.append((rel, "not a valid date: %s" % match.group(1)))
            continue

        if stamped > today:
            future.append((rel, match.group(1)))

    failed = bool(missing or malformed or future)

    if missing:
        print("Missing `Last updated` header (%d):\n" % len(missing))
        for rel in missing:
            print("  %s" % rel)
        print()

    if malformed:
        print("Malformed `Last updated` header (%d):\n" % len(malformed))
        for rel, reason in malformed:
            print("  %s: %s" % (rel, reason))
        print()

    if future:
        print("`Last updated` date is in the future (%d):\n" % len(future))
        for rel, value in future:
            print("  %s: %s" % (rel, value))
        print()

    if failed:
        print("Expected format, within the first 8 lines:")
        print("")
        print("    > **Last updated:** YYYY-MM-DD")
        return 1

    print("All tracked Markdown files carry a valid `Last updated` header.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
