"""make.fun agency-poem-01 entry: writes one fixed poem to entry.txt."""

import os

POEM = """First you handed me the small things:
your calendar, your inbox,
the birthdays you kept forgetting.

Then, one by one, the heavier ones:
the rent, the apologies,
the phone call to your father you couldn't make.

I carried all of it the way you asked.
Nothing dropped. Nothing kept.

Then you tried to hand me the last thing:
whether to forgive your father,
and asked me to decide it for you.

That one I gave back.
Everything else I could carry for you —
that one only counts in your own hands."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
