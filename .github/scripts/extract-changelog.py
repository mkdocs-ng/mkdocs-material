#!/usr/bin/env python3
"""Extract the latest version's release notes from docs/changelog/index.md.

Outputs JSON with "version", "date", and "body" fields for use in GitHub Actions.
"""

import json
import re
import sys
from pathlib import Path

CHANGELOG_PATH = Path("docs/changelog/index.md")


def extract_latest() -> dict | None:
    """Extract the latest release entry from the changelog."""
    text = CHANGELOG_PATH.read_text(encoding="utf-8")

    # Match the first version heading: ### VERSION <small>DATE</small> { id="..." }
    pattern = re.compile(
        r'^###\s+(\S+)\s+<small>(.*?)</small>\s*\{[^}]*\}\s*$',
        re.MULTILINE,
    )

    match = pattern.search(text)
    if not match:
        return None

    version = match.group(1)
    date = match.group(2).strip()
    start = match.end()

    # Find the next version heading or the "---" separator
    next_pattern = re.compile(
        r'^###\s+\S+\s+<small>|^---\s*$',
        re.MULTILINE,
    )
    next_match = next_pattern.search(text, start)
    end = next_match.start() if next_match else len(text)

    body = text[start:end].strip()

    return {"version": version, "date": date, "body": body}


def main() -> None:
    entry = extract_latest()
    if not entry:
        print("No version entry found in changelog", file=sys.stderr)
        sys.exit(1)

    json.dump(entry, sys.stdout, ensure_ascii=False)
    print()  # trailing newline


if __name__ == "__main__":
    main()
