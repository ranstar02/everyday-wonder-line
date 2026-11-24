"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

Writes a single sentence about a small moment of wonder in everyday
life to /output/entry.txt.

Why this sentence: a ceiling fan is the most ordinary object in a
room, yet it has watched us for a decade without ever looking back.
The personification flips the watcher and the watched — the fan
spins its same circle above us, and the surprise lands in the final
clause, when we realise it has never once looked down at us.

Deterministic, stdlib only, no network, no randomness: the same
sentence is written on every run.
"""

import os

SENTENCE = "The ceiling fan has spun the same circle for ten years, and tonight I noticed it has never once looked down at us."


def main():
    assert 1 <= len(SENTENCE) <= 200, "entry must be 1-200 characters"
    assert SENTENCE.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(SENTENCE)
    except OSError:
        out_dir = "./output"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
