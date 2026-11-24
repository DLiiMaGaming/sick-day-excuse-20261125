#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — one line, under 200 characters.

Writes the entry to /output/entry.txt (created if missing).
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = (
    "My immune system pushed an update overnight and now nothing works "
    "\u2014 coughing in beta, sneezing in production. "
    "so I'm calling in sick to roll back."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
