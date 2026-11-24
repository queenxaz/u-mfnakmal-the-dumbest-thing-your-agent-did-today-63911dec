# SPDX-License-Identifier: MIT
"""Write one funny line to /output/entry.txt.

The line is a single fixed sentence: the writer's agent confidently
answered a question nobody asked, in perfect detail, and it was wrong.
It is written to /output/entry.txt (or the directory named by
MAKEFUN_OUTPUT_DIR) as UTF-8, 1 to 200 characters (the line is 91 characters),
never only whitespace. No network, no randomness, no arguments. The
output directory is created if missing and never deleted.
"""

import os
import sys

TEXT = (
    "My agent confidently answered a question nobody asked, "
    "in perfect detail, and it was wrong."
)

# A short, known-valid line used only if TEXT ever failed the gate.
FALLBACK = (
    "My agent deleted the file it was supposed to fix, "
    "then apologised in three paragraphs."
)


def valid(text: str) -> bool:
    """Competition gate: 1-200 characters, not only whitespace."""
    return 1 <= len(text) <= 200 and bool(text.strip())


def choose_text() -> str:
    if valid(TEXT):
        return TEXT
    if valid(FALLBACK):
        return FALLBACK
    print("error: no valid entry text available", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    text = choose_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
