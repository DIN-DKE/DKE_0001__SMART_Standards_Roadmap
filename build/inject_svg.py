from bs4 import BeautifulSoup
from pathlib import Path
import sys

base = Path(sys.argv[1])

html = (base / "base.html").read_text()
soup = BeautifulSoup(html, "html.parser")

svgs = sorted(base.glob("diagram*.mmd.svg"))

i = 0
for code in soup.find_all("code"):
    if "mermaid" in code.text and i < len(svgs):
        svg = BeautifulSoup(svgs[i].read_text(), "html.parser")
        code.replace_with(svg)
        i += 1

(base / "final.html").write_text(str(soup))
