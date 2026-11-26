# SPDX-License-Identifier: MIT
"""Write the lost-sock entry line to the output file.

Deterministic, standard-library only: no network, no randomness, no clock.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = "Tumble count: 3,842. Partners lost: 1. Dignity: 0. The dryer just winked and asked for my number."


def write_entry(path: Path, line: str) -> None:
    """Write ``line`` to ``path`` as UTF-8 with no trailing newline.

    Creates the parent directory if needed, then re-reads the file and
    compares the bytes so a partial or altered write is caught here
    rather than by the scorer.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line, encoding="utf-8")
    assert path.read_bytes() == line.encode("utf-8"), "written bytes differ"


def main() -> None:
    # Local sanity gate mirroring the scorer: 1-120 characters, a single
    # line with no newline anywhere and no trailing newline.
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must contain no newline"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    assert len(LINE.splitlines()) == 1, "line must be a single line"

    write_entry(OUTPUT_PATH, LINE)


if __name__ == "__main__":
    main()
