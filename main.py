#!/usr/bin/env python3
"""The Internet in One Word.

The entry is a single word written to /output/entry.txt.

The word is "feral": the whole internet, in one beat, is a wild thing
with nobody in charge. Everyone arrived, nobody is supervising, and
the place runs on instinct. It is funny on its own, true of the
internet as a whole rather than any one app, and it is not the first
obvious word anyone reaches for.
"""

WORD = "feral"


def main() -> None:
    """Write the single word to /output/entry.txt, exactly as-is."""
    output_path = "/output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
