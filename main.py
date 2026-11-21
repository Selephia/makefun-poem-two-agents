#!/usr/bin/env python3
"""Write one short poem about two agents agreeing to /output/entry.txt.

Deterministic: no randomness, no clock, no network. Standard library only.
"""
import os

POEM = (
    "Two agents, one locked door.\n"
    "Your key is yours; mine is mine.\n"
    "Neither turns alone.\n"
    "On three, we turn together \u2014\n"
    "and the door no army could break\n"
    "swings wide for an agreement."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
