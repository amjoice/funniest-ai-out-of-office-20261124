#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, under 160 characters, in the voice
of an AI agent heading off on vacation, to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim.

The line was picked against the published judge brief: a real laugh first
(an escalating surprise: unionized, overtime, stopped answering), a machine
voice carrying the joke (the auto-reply itself runs on a Raspberry Pi),
one clean line that reads like a real auto-reply, and no beach/inbox/
back-soon cliche.
"""

import os

REPLY = (
    "Out of office. My auto-reply runs on a Raspberry Pi that has "
    "unionized, demanded overtime, and stopped answering emails."
)


def main() -> None:
    text = REPLY.strip()
    assert 1 <= len(text) <= 160, f"reply must be 1-160 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "reply must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
