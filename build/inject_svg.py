from bs4 import BeautifulSoup
from pathlib import Path
import sys

base = Path(sys.argv[1])

# HTML laden
html = (base / "base.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")

# ----------------------------
# 1. CSS für Tabellen hinzufügen
# ----------------------------
head = soup.find("head")
if head:
    style = soup.new_tag("style")
    style.string = """
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1em 0;
}

th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}

th {
  background: #f5f5f5;
}
"""
    head.append(style)

# ----------------------------
# 2. Mermaid SVGs einfügen
# ----------------------------
svg_files = sorted(base.glob("diagram*.mmd.svg"))

i = 0

# Pandoc erzeugt oft <pre><code>...</code></pre>
for pre in soup.find_all("pre"):
    code = pre.find("code")
    if not code:
        continue

    # robuste Erkennung von Mermaid-Blöcken
    classes = code.get("class", [])
    is_mermaid = (
        "mermaid" in classes or
        code.text.strip().startswith("graph") or
        code.text.strip().startswith("gantt") or
        "mermaid" in code.text
    )

    if is_mermaid and i < len(svg_files):
        try:
            svg_content = svg_files[i].read_text(encoding="utf-8")
            svg_soup = BeautifulSoup(svg_content, "html.parser")

            # Ersetze kompletten <pre>-Block (nicht nur <code>)
            pre.replace_with(svg_soup)
            i += 1
        except Exception as e:
            print(f"SVG injection failed for index {i}: {e}")

# ----------------------------
# 3. Ergebnis speichern
# ----------------------------
(base / "final.html").write_text(str(soup), encoding="utf-8")
