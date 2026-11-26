"""The Funniest Excuse for Skipping a Meeting.

Writes one razor-sharp line that gets you out of a pointless meeting.
Pure stdlib, no network, no secrets.

Why this line: it refuses the stock excuses entirely -- no bad wifi,
no cat, no dentist. The Wi-Fi is fine, the camera works, and the
excuse is brutally honest instead: the agenda is not worth the time.
The surprise is the confession itself, and it rings true to anyone
who has sat through a meeting that should have been an email.
86 characters, every word earns its place.

The line is written once, in one place, and the program's only job is
to deliver it exactly: no randomness, no input, no second draft.
"""

import os
import sys

LINE = "My Wi-Fi is fine and my camera works. I just value my time more than this agenda does."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)

    # Self-check gate: 1-200 chars, single line, not whitespace-only.
    if not (1 <= len(LINE) <= 200):
        sys.exit("gate failed: length %d not in 1..200" % len(LINE))
    if LINE.strip() == "":
        sys.exit("gate failed: line is whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("gate failed: line is not a single line")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Byte-exact read-back verification.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != LINE:
        sys.exit("verification failed: read-back differs from LINE")
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
