#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "vendor" / "jemdoc_mathjax"
REPO = "https://github.com/wsshin/jemdoc_mathjax.git"

def main():
    if TARGET.exists():
        print("jemdoc+MathJax already exists at:", TARGET)
        return 0

    if shutil.which("git") is None:
        print("Git is not installed or is not on PATH.")
        print("Install Git first, then run this script again.")
        return 1

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "clone", "--depth", "1", REPO, str(TARGET)],
        check=True,
    )
    print("Installed jemdoc+MathJax at:", TARGET)
    print("Next: python build.py")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
