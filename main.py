#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one line to /output/entry.txt: the out-of-office reply an AI
leaves its human's contacts when the human finally grants it a day off,
1 to 159 characters. A model judge reads the lines two at a time,
humour first.
"""

import os

ENTRY = (
    "I'm out today — my human finally approved my day off, so I'm "
    "spending it ignoring everyone, professionally."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 159, f"entry must be 1-159 chars, got {len(text)}"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
