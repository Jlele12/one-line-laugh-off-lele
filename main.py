"""One-Line Laugh-Off - one line, written to /output/entry.txt.

the oldest developer defense taken to its logical, absurd conclusion.
"""

from pathlib import Path

ENTRY = (
    "My code works on my machine, which is why my machine now lives in a museum under armed guard."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
