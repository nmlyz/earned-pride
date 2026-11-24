"""Write one line of earned pride to /output/entry.txt.

The line: a boy who stutters says his own name clean through at the
register, and the cashier answers it like any other name. Standard
library only, deterministic: every run writes the same bytes.
"""

import os

LINE = (
    "The boy who could not say his own name without stopping said it "
    "clean through at the register, and the cashier answered it like "
    "any other name."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
