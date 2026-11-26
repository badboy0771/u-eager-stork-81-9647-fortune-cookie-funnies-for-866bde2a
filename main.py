#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes one fortune-cookie message for a software engineer to
/output/entry.txt: a single line of at most 120 UTF-8 characters.

The fortune is assembled from two short sentences so the twist lands
last: a classic fortune-cookie opening, then the engineer's punchline.

Usage:
    python3 main.py            # write /output/entry.txt
    python3 main.py --check    # validate only, print the fortune
"""

import os
import sys

# The fortune, in two beats: the setup, then the punchline.
SETUP = "A recruiter will message you today."
PUNCHLINE = "They will offer you your own job."

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def build_fortune() -> str:
    """Join the setup and the punchline into one fortune-cookie line."""
    return f"{SETUP} {PUNCHLINE}"


def validate(text: str) -> str:
    """Return the fortune unchanged, or raise if it breaks the gate."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("fortune must not be blank")
    if len(stripped) != len(text):
        raise ValueError("fortune must not have leading/trailing whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("fortune must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"fortune must be at most {MAX_CHARS} characters, got {len(stripped)}"
        )
    return stripped


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Validate the fortune and write it to path; return the text."""
    text = validate(build_fortune())
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return text


def main(argv: list[str]) -> int:
    if "--check" in argv:
        text = validate(build_fortune())
        print(text)
        print(f"({len(text)} characters, valid)")
        return 0
    text = write_entry()
    print(text)
    print(f"({len(text)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
