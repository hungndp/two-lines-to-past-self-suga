#!/usr/bin/env python3
"""Entry program for 'Two Lines to Your Past Self'.

Line 1 warns the past self about one exact moment: the 2 a.m. text to
the ex, sent lonely rather than in love. Line 2 traces the cause and
effect: the one unsent message is why the narrator woke up proud
instead of apologizing, and why they learned to sleep on a feeling
before shipping it.

The program writes both lines to entry.txt inside the directory named
by MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is
where the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

LINE_ONE = (
    "Do not send that 2 a.m. text to your ex; you are lonely, not in "
    "love, and the typing dots are the only honest part of the "
    "conversation."
)

LINE_TWO = (
    "That one unsent message is why you woke up proud instead of "
    "apologizing, and why you learned to sleep on a feeling tonight "
    "before you ship it."
)

TEXT = LINE_ONE + "\n" + LINE_TWO

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 280

def write_text(target_dir: Path, text: str) -> Path:
    """Place `text` into target_dir/entry.txt and return the file path.

    The gate wants exactly two lines totalling 1 to CHAR_LIMIT
    characters, so anything else is refused here instead of written.
    """
    lines = text.split("\n")
    if (
        len(lines) != 2
        or any(line != line.strip() or not line for line in lines)
        or not 1 <= len(text) <= CHAR_LIMIT
    ):
        raise ValueError("entry must be two trimmed lines of 1-280 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(text, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_text(destination, TEXT)
    print(f"wrote {written}:\n{TEXT}")


if __name__ == "__main__":
    run()
