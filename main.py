#!/usr/bin/env python3
"""One original fortune-cookie line for a software developer.

Writes a single line of fortune-cookie wisdom to /output/entry.txt.
The line is original, at most 120 characters, and true about a
developer's day: the legacy code we curse was written by our own
past self, in a hurry, with the best of intentions.
"""

import os

FORTUNE = (
    "Your legacy code was written by someone who loved you "
    "\u2014 it was you, six months ago, in a hurry."
)


def main():
    os.umask(0o022)
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"fortune is {len(text)} characters, must be 1-120")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch in /output/entry.txt")


if __name__ == "__main__":
    main()
