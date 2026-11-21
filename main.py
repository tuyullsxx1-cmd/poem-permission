#!/usr/bin/env python3
"""The poem about permission -- a borrowed umbrella.

Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Python 3.13, stdlib only,
no network, deterministic.
"""

import os
from pathlib import Path

POEM = """I borrowed your umbrella.
It rained the whole way home,
and I carried it closed,
afraid to open what wasn't mine.

You laughed when I brought it back dry.
The umbrella was never the gift.
The walk was.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
