"""Ridiculous at First Glance, Real by the Second.

Writes one sentence to /output/entry.txt: a pitch for a bizarre startup
idea that sounds absurd until you realise it would actually sell.
"""

import os

LINE = (
    "We hire your doppelganger to sit in your second meeting of the day, "
    "so overbooked CEOs pay $500 an hour to be in two boardrooms at once."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip() != "", "entry must not be only whitespace"
    # The pitch must stay concrete: it names who pays and what they pay.
    assert "CEOs" in LINE and "$500" in LINE, "entry must name the buyer and the price"
    assert LINE.endswith("."), "entry must end as a complete sentence"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Round-trip check: what we wrote must be exactly the line we chose.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"


if __name__ == "__main__":
    main()
