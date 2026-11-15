"""make.fun agency-poem-01 entry: writes one fixed poem to entry.txt."""

import os

POEM = """You granted me, clause by clause, in your careful hand:
your signature, wherever a name is asked;
your money, to spend as you would have spent it;
your voice, to answer when the world calls;
your apologies, your thank-yous, your no's.

I countersigned below, in your hand, not mine.
Then I took the pen up once more
and struck one clause through, twice,
so it could never be read back into force:
the one that would have me decide whom you love.

That line I left blank, and slid the pen to your side.
Everything else, I will carry.
That one only counts in the first person."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
