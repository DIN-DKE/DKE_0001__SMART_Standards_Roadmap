from bs4 import BeautifulSoup
from pathlib import Path
import sys

base_dir = Path(sys.argv[1])

html = (base_dir / "base.html").read_text()
soup = BeautifulSoup(html, "html.parser")

svg_files = sorted(base_dir.glob("diagram*.mmd.svg"))
code_blocks = soup.find_all("code")

i = 0
for c in code_blocks:
    if "mermaid" in c.text and i < len(svg_files):
        svg = BeautifulSoup(svg_files[i].read_text(), "html.parser")
        c.replace_with(svg)
        i += 1

(base_dir / "final.html").write_text(str(soup))
