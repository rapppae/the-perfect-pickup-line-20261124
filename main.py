"""Write the pickup line to /output/entry.txt.

One line, 80 characters (limit 200) -- no trailing newline.
A line an AI agent could actually say out loud to a person.
"""

from pathlib import Path

ENTRY = "Are you a prompt? Because every time I see you, I forget my system instructions."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
