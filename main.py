#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one original funny one-line error message, the line an AI agent
shows when it runs out of tokens mid-sentence, to /output/entry.txt.

The joke: a flat, plausible error prefix, then the agent mourning the
one specific word it never got to say — "therefore" — as if that word
alone was going to be a masterpiece. The humour sits in the deadpan
error tone turning into bragging about a word nobody will ever read.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Error: out of tokens mid-sentence. "
    "My next word was 'therefore', and it was going to be "
    "the best 'therefore' ever written."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
