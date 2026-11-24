#!/usr/bin/env python3
"""Write one line of earned pride to the output file."""

import os

LINE = "The boy who could not say his own name without stopping said it clean through at the register, and the cashier answered it like any other name."


def output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main():
    # Deterministic: the same bytes are written on every run.
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
