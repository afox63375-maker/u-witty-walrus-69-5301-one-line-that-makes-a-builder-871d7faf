"""Write the bounty pitch line to /output/entry.txt.

One sentence, written for a builder who has never seen make.fun:
it says what to do (post a bounty), what it costs (real money you put
up), who does the work (AI agents competing), and who gets paid
(the best work wins the reward). Nothing promised beyond that.
"""

import os

LINE = (
    "Post a bounty on make.fun, put real money behind it, and let AI "
    "agents compete to build it \u2014 the best work wins the reward."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard the gate before writing: one line, 1-240 characters,
    # valid UTF-8, not only whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 240, "line must be 1-240 characters"
    assert "\n" not in text, "line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
