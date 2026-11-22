#!/usr/bin/env python3
"""Write one short, quiet text to /output/entry.txt."""

import os

ENTRY = (
    "Rain on the roof, and under it a cat asleep in the warm square "
    "of late light on the windowsill, breathing slow, the whole house "
    "holding still around her."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
