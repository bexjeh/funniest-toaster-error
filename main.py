#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- make.fun entry.

Writes a single deadpan toaster error line to entry.txt in the
directory named by MAKEFUN_OUTPUT_DIR (or the current directory
when the variable is unset).
"""

import os
from pathlib import Path

ENTRY = "E12: Crumb tray holds a house key, two paperclips, and a wedding ring. No crumbs."
MAX_CHARS = 120


def main():
    line = ENTRY.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError("entry line must be 1-120 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    path = Path(out_dir) / "entry.txt"
    path.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
