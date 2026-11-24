#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label (82 chars, within the 1-120 gate) to /output/entry.txt.

The label turns a real time-travel hazard — meeting your duplicate self —
into the joke, in the straight-faced tone of a genuine safety notice, with
the surprise saved for the last few words: lending money to yourself is a
bad idea, because the borrower is you, and you never pay it back.
"""

import os

ENTRY = "CAUTION: If you meet yourself, do not lend yourself money \u2014 he never pays it back."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
