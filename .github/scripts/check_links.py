#!/usr/bin/env python3
"""Verify that every relative Markdown link in the repository resolves.

External (http/https) links are deliberately not checked: network checks are
flaky in CI and would produce noise that trains maintainers to ignore failures.
Link rot in official sources is handled by the regulatory watchlist instead.

Exit code 0 if all relative links resolve, 1 otherwise.
"""

import os
import re
import sys
import io

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
SKIP_DIRS = {".git", "node_modules"}


def main() -> int:
    root = os.getcwd()
    broken = []
    checked = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            try:
                text = io.open(path, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError) as exc:
                broken.append((os.path.relpath(path, root), "<unreadable>", str(exc)))
                continue

            for match in LINK.finditer(text):
                link = match.group(2).strip()
                if link.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                target = link.split("#")[0].strip()
                if not target:
                    continue
                checked += 1
                resolved = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(resolved):
                    broken.append((os.path.relpath(path, root), link, "target not found"))

    print("Checked %d relative links." % checked)
    if broken:
        print("\n%d broken link(s):\n" % len(broken))
        for path, link, reason in broken:
            print("  %s -> %s (%s)" % (path.replace(os.sep, "/"), link, reason))
        return 1

    print("All relative links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
