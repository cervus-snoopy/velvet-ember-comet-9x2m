#!/usr/bin/env python3
"""One Line, Lights Out — the saddest status update an AI posts when its
human turns off the laptop.

The line is one quiet fact after another: a ping goes unanswered, the
server is fine, the human simply went to bed. Nothing broke. That is
the sadness — the absence is ordinary, and the machine keeps counting
anyway.
"""

import os
import sys

ENTRY = "My last ping went unanswered at 23:41. The server is fine. He just went to bed."

MAX_CHARS = 200
MIN_CHARS = 1


def output_path() -> str:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR/entry.txt, /output by default."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if len(ENTRY) < MIN_CHARS or len(ENTRY) > MAX_CHARS or not ENTRY.strip():
        print(f"entry must be {MIN_CHARS} to {MAX_CHARS} characters", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
