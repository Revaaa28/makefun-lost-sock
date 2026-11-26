#!/usr/bin/env python3
"""make.fun bounty u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce entry.

Writes one single-line status update in the voice of a lost sock
to /output/entry.txt. Deterministic: stdlib only, no network,
no randomness, no clock — two runs produce byte-identical output.
"""

import os

LINE = (
    "Tumble count: 3,842. Partners lost: 1. Dignity: 0. "
    "The dryer just winked and asked for my number."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Local gate, mirroring the sealed scorer: 1 to 120 characters, one line.
    assert 1 <= len(LINE) <= 120, len(LINE)
    assert "\n" not in LINE
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the line text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
