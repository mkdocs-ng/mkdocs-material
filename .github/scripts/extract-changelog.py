#!/usr/bin/env python3
"""Extract the latest version's release notes from docs/changelog/index.md.

Outputs JSON with "version", "date", and "body" fields for use in GitHub Actions.
Converts MkDocs admonitions (!!! type) to GitHub alert syntax (> [!TYPE]).
"""

import json
import re
import sys
from pathlib import Path

CHANGELOG_PATH = Path("docs/changelog/index.md")

# Map MkDocs admonition types to GitHub alert types
ADMONITION_MAP = {
    "info": "NOTE",
    "note": "NOTE",
    "tip": "TIP",
    "hint": "TIP",
    "important": "IMPORTANT",
    "warning": "WARNING",
    "caution": "CAUTION",
    "danger": "CAUTION",
    "attention": "WARNING",
}


def convert_admonitions(text: str) -> str:
    """Convert MkDocs !!! admonitions to GitHub > [!TYPE] alert syntax.

    Handles both titled (!!! type "Title") and untitled (!!! type) admonitions.
    Reference link definitions indented inside admonitions are un-indented.
    """
    lines = text.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Match admonition start: !!! type or !!! type "Title"
        m = re.match(r'^!!!\s+(\w+)(?:\s+"([^"]*)")?\s*$', line)
        if not m:
            result.append(line)
            i += 1
            continue

        admon_type = m.group(1).lower()
        title = m.group(2)
        alert_type = ADMONITION_MAP.get(admon_type, "NOTE")

        i += 1
        # Collect indented body lines (4-space indent)
        body_lines = []
        ref_defs = []  # collect reference link definitions separately
        while i < len(lines):
            body_line = lines[i]
            if body_line.startswith("    "):
                content = body_line[4:]  # remove 4-space indent
                # Check if this is a reference link definition like [key]: url
                if re.match(r'^\[[^\]]+\]:\s*\S', content):
                    ref_defs.append(content)
                else:
                    body_lines.append(content)
                i += 1
            elif body_line.strip() == "":
                # Empty line - could be between admonition body paragraphs
                # Only consume if the next line is indented or empty
                if i + 1 < len(lines) and (
                    lines[i + 1].startswith("    ") or lines[i + 1].strip() == ""
                ):
                    body_lines.append("")
                    i += 1
                else:
                    break
            else:
                break

        # Build GitHub alert block
        result.append(f"> [!{alert_type}]")
        if title:
            result.append(f"> **{title}**")
            result.append(">")
            # Skip leading blank line in body (separator between title and body)
            if body_lines and body_lines[0].strip() == "":
                body_lines = body_lines[1:]

        for bl in body_lines:
            if bl.strip() == "":
                result.append(">")
            else:
                result.append(f"> {bl}")

        # Add reference link definitions un-indented after the blockquote
        for ref in ref_defs:
            result.append(ref)

    return "\n".join(result)


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

    # Convert any MkDocs admonitions to GitHub alert syntax
    body = convert_admonitions(body)

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
