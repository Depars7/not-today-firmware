"""The Vacuum's Alibi — one deadpan line excusing a missed spot.

Writes the entry line to /output/entry.txt (1-200 characters, UTF-8).
"""
import os

PARTS = [
    "I did not miss that spot. ",
    "My collision sensor calls it occupied territory — the cat sleeps there — ",
    "and my survival firmware calls it 'not today.'",
]


def entry_line() -> str:
    # Deadpan escalation: sensor report first, survival firmware has the last word.
    return "".join(PARTS)


def main() -> None:
    line = entry_line()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 characters, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
