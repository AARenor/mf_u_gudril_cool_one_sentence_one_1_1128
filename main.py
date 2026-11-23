#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt.

Entry for bounty u-gudril-cool-one-sentence-one-journey-410686ca:
a complete journey told in exactly one sentence.
"""

import os
import sys

TEXT = "My grandfather ran the same eleven-minute ferry for forty years, and on his last crossing he handed me the wheel at the whistle buoy and stood at the rail with his back to the town, so I brought us in by the smell of the cannery and he arrived a passenger."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "text must be 1..280 characters"

    out_dir = "/output"
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            out_dir = value
            break
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
