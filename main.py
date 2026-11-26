"""Green Tests, Nothing Works - make.fun entry.

Writes one line (under 140 characters): the excuse an AI agent gives
for a test suite that is all green while the product does nothing.

Stdlib only, deterministic: the exact same line on every run.
"""

import os

LINE = (
    "The tests are green because they only test the parts of the app "
    "that do nothing \u2014 which, it turns out, is all of it."
)


def main() -> None:
    if not LINE.strip() or len(LINE) > 140:
        raise SystemExit("entry line must be 1-140 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    # Re-read and re-check the file we just wrote: the gate the sealed
    # scorer applies is 1-140 UTF-8 characters, not only whitespace.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if not written.strip() or len(written.strip()) > 140:
        raise SystemExit("written entry.txt fails the 1-140 character gate")
    print(LINE)


if __name__ == "__main__":
    main()
