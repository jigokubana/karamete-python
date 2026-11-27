"""Drill 01: append notes to a text file with auto-created directory."""

import os


def append_note(filepath: str, text: str) -> None:
    folder = os.path.dirname(filepath)
    if folder:
        os.makedirs(folder, exist_ok=True)
    is_new = not os.path.exists(filepath)
    with open(filepath, "a", encoding="utf-8") as f:
        if is_new:
            f.write("=== NOTES ===\n")
        f.write(text + "\n")


if __name__ == "__main__":
    append_note("tmp_logs/notes.txt", "Первая запись")
    append_note("tmp_logs/notes.txt", "Вторая запись")
