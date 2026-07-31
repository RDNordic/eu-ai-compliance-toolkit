#!/usr/bin/env python3
"""Report Markdown documents whose `Last updated` date has aged past a threshold.

Regulatory drift is this repository's main failure mode. This script does not
fail a build: it produces a Markdown report that the scheduled workflow files as
an issue, so review is prompted rather than silently skipped.

Legal-content directories get a shorter threshold than operational guidance,
because they go stale faster and matter more when they do.

Usage:  check_staleness.py [--report PATH]
Writes the report to PATH (default: staleness-report.md) and prints it.
Exit code is always 0 unless the repository cannot be read.
"""

import argparse
import datetime
import io
import os
import re
import subprocess
import sys

LEGAL_PREFIXES = ("eu-ai-act/", "gdpr/", "dpia/", "resources/")
LEGAL_DAYS = 120
GENERAL_DAYS = 270

EXEMPT = {
    "CHANGELOG.md",
    "source-update/triage-summary.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
}

HEADER = re.compile(r"Last updated:?\*{0,2}\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)


def tracked_markdown():
    out = subprocess.check_output(["git", "ls-files", "*.md"], text=True)
    return [line.strip() for line in out.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="staleness-report.md")
    args = parser.parse_args()

    today = datetime.date.today()
    legal_stale = []
    general_stale = []
    undated = []

    for path in tracked_markdown():
        rel = path.replace(os.sep, "/")
        if rel in EXEMPT:
            continue
        try:
            head = io.open(path, encoding="utf-8-sig").read().split("\n")[:8]
        except OSError:
            continue

        match = HEADER.search("\n".join(head))
        if not match:
            undated.append(rel)
            continue

        try:
            stamped = datetime.date.fromisoformat(match.group(1))
        except ValueError:
            undated.append(rel)
            continue

        age = (today - stamped).days
        is_legal = rel.startswith(LEGAL_PREFIXES)
        threshold = LEGAL_DAYS if is_legal else GENERAL_DAYS
        if age > threshold:
            (legal_stale if is_legal else general_stale).append((rel, match.group(1), age))

    legal_stale.sort(key=lambda row: -row[2])
    general_stale.sort(key=lambda row: -row[2])

    lines = []
    lines.append("Automated staleness check, %s." % today.isoformat())
    lines.append("")
    lines.append("Thresholds: legal content %d days, other content %d days."
                 % (LEGAL_DAYS, GENERAL_DAYS))
    lines.append("")

    if not (legal_stale or general_stale or undated):
        lines.append("Nothing is overdue for review.")
    else:
        if legal_stale:
            lines.append("## Legal content overdue for review")
            lines.append("")
            lines.append("Check these against the current enacted text before anyone relies on them.")
            lines.append("")
            lines.append("| File | Last updated | Age (days) |")
            lines.append("|---|---|---|")
            for rel, stamp, age in legal_stale:
                lines.append("| `%s` | %s | %d |" % (rel, stamp, age))
            lines.append("")

        if general_stale:
            lines.append("## Other content overdue for review")
            lines.append("")
            lines.append("| File | Last updated | Age (days) |")
            lines.append("|---|---|---|")
            for rel, stamp, age in general_stale:
                lines.append("| `%s` | %s | %d |" % (rel, stamp, age))
            lines.append("")

        if undated:
            lines.append("## Missing or unparseable `Last updated` header")
            lines.append("")
            for rel in undated:
                lines.append("- `%s`" % rel)
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("Reviewing a file means confirming its claims still hold, then bumping its "
                 "`Last updated` header. See the regulatory watchlist in "
                 "`eu-ai-act/risk-classification.md` for what to check.")
    lines.append("")
    lines.append("Primary sources: EUR-Lex blocks automated clients (HTTP 202, empty body). "
                 "Use the Publications Office CELLAR endpoint instead:")
    lines.append("")
    lines.append("```bash")
    lines.append('curl -H "Accept: application/xhtml+xml" '
                 "http://publications.europa.eu/resource/celex/32026R1744")
    lines.append("```")

    report = "\n".join(lines) + "\n"
    io.open(args.report, "w", encoding="utf-8", newline="\n").write(report)
    print(report)

    overdue = len(legal_stale) + len(general_stale)
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with io.open(gh_out, "a", encoding="utf-8") as handle:
            handle.write("overdue=%d\n" % overdue)
            handle.write("legal_overdue=%d\n" % len(legal_stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
