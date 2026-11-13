"""Entry for the AI coding agent joke competition: writes one one-line joke."""

import os

JOKE = "My AI agent and I split the work 50/50: it writes the code, I write the postmortem."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
