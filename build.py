#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PAGES = ["index.jemdoc", "publications.jemdoc", "projects.jemdoc", "biography.jemdoc"]

CANDIDATES = [
    ROOT / "vendor" / "jemdoc_mathjax" / "jemdoc",
    ROOT / "jemdoc",
]

def find_jemdoc():
    for path in CANDIDATES:
        if path.exists():
            return path
    return None

def main():
    jemdoc = find_jemdoc()
    if jemdoc is None:
        print("jemdoc+MathJax was not found.")
        print("Run: python setup_jemdoc.py")
        print("Then run this build command again.")
        return 1

    for page in PAGES:
        print(f"Building {page} ...")
        subprocess.run(
            [sys.executable, str(jemdoc), "-c", "mysite.conf", page],
            cwd=ROOT,
            check=True,
        )

    site = ROOT / "_site"
    if site.exists():
        shutil.rmtree(site)
    site.mkdir()

    for html in ROOT.glob("*.html"):
        shutil.copy2(html, site / html.name)
    shutil.copy2(ROOT / "jemdoc.css", site / "jemdoc.css")

    for dirname in ["assets", "files"]:
        src = ROOT / dirname
        if src.exists():
            shutil.copytree(src, site / dirname)

    print()
    print("Build complete:", site)
    print("Preview with:")
    print("  python -m http.server 8000 -d _site")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
