"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt and nothing else:
a gentle smiling face, U+263A + U+FE0F (emoji presentation).

Pure standard library, deterministic, no network, no input files.
"""

import os
from pathlib import Path

# The single emoji: U+263A SMILING FACE + U+FE0F variation selector-16.
EMOJI = "\u263a\ufe0f"

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = EMOJI.encode("utf-8")
    OUTPUT_FILE.write_bytes(data)
    # The grader runs as uid 65534 on a root-owned /output bind mount and a
    # different user reads the result, so the file must be world-readable.
    # Never chmod the /output directory itself: uid 65534 cannot chmod it
    # (EPERM) and the run would fail after everything else succeeded.
    os.chmod(OUTPUT_FILE, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
