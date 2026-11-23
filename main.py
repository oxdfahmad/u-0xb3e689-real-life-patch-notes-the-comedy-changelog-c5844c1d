#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — writes one patch-note line."""

import os
import sys

LINE = "v2.7.0: Fixed a bug where the brain replayed your most embarrassing moment from 2014 every night at 3 a.m."

# Line choice: the 3 a.m. replay of an old embarrassment is a specific,
# universally recognised human-biology bug — it makes the reader wince
# and laugh at once, in the terse register of a real release note.


def validate_line(line):
    """Gate check: 1-160 chars, not whitespace-only, single line."""
    if not line or len(line) > 160:
        raise ValueError(f"line must be 1-160 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    return line


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, encoding="utf-8") as f:
        back = f.read()
    assert back == LINE + "\n", "read-back mismatch"
    print(f"entry.txt OK: {len(LINE)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
