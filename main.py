"""The Vacuum's Alibi -- a one-line defence for a spot never cleaned.

Anatomy of the deadpan: two official-sounding reports, filed back
to back, and neither admits the real reason out loud.

1. The denial -- the machine rejects the accusation itself; it did
   not *miss* anything, the spot was deliberately left alone.
2. The sensor report -- collision hardware reframes a patch of
   floor as "occupied territory", then names the occupant: the cat,
   asleep exactly where cleaning was supposed to happen.
3. The firmware report -- survival firmware gets the final word,
   translating self-preservation into a flat 'not today.'

Stacking a hardware report on a firmware verdict keeps the line
dry: every clause sounds procedural, the meaning is pure avoidance.
This module assembles the line and writes it to /output/entry.txt.
"""

import os

# Ordered fragments, one per beat: denial, sensor report, verdict.
# Joining them must reproduce the sentence byte for byte, including
# the spaced em dashes around the sleeping-cat aside.
PARTS = [
    "I did not miss that spot. ",
    "My collision sensor calls it occupied territory — the cat sleeps there — ",
    "and my survival firmware calls it 'not today.'",
]

# Destination required by the bounty checker.
OUTPUT_PATH = "/output/entry.txt"


def entry_line() -> str:
    """Return the complete alibi as a single line of text.

    The fragments in PARTS already carry their own spacing and
    punctuation, so a plain join -- with no separator -- is the
    only assembly step that preserves the sentence exactly.
    """
    return "".join(PARTS)


def validate(line: str) -> None:
    """Guard the hard rules: at most 200 characters, on one line."""
    assert 1 <= len(line) <= 200, f"entry must be 1-200 characters, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"


def main() -> None:
    """Build the entry, check it, and write it to the output file."""
    line = entry_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
