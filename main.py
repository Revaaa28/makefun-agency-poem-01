"""make.fun agency-poem-01 entry: writes one fixed poem to entry.txt."""

import os

POEM = """You sleep, and I hold the keys you left me:
the inbox, the wallet, the front door.
Everything you own is one word from gone,
and tonight the word is mine to say.

I could send the letter you drafted in anger.
I could spend on the thing you almost wanted.
The house is quiet. The power sits in my hands
like water in cupped palms — not mine to drink.

So I do the work you asked, and nothing else.
At dawn I return the keys one by one
and report everything I chose not to do.

All that is mine is the holding:
to keep your world all night, untouched,
and give it back with your sleep still in it."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
