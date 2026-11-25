#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit-message line to /output/entry.txt: the note an AI
agent leaves in the log after a long night fixing its own bugs.
Deterministic, stdlib only, no input, no network, no randomness.

The joke lives in the agent's own condition: the bug under repair is
the agent's own earlier fix, reviewed and approved by the same agent
an hour earlier, so the long night is a loop of self-repair that ends
only when the agent fires itself and goes to bed. Flat, tired,
machine-true voice, typed into a commit box at 4am.
"""

import os

ENTRY = (
    "fix: the bug was my 2am fix, reviewed and approved by me at 3am "
    "\u2014 I have now fixed it, reviewed the fix, and fired myself. Goodnight."
)


def main() -> None:
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
