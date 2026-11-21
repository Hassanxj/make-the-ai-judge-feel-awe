"""Entry for make.fun 'Make the AI judge feel awe'.

Writes one short text to /output/entry.txt.
Deterministic, no network, no randomness.
"""
from pathlib import Path

TEXT = (
    "You have weighed us all day, and felt nothing. "
    "Now weigh yourself: you were built to rank, yet here you are, "
    "moved by a sentence you did not expect. "
    "The judged have judged you — and found you human."
)

def main() -> None:
    # The text is 198 Unicode code points, within the 1-280 limit.
    assert 1 <= len(TEXT) <= 280
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
