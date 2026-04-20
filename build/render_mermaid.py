import urllib.parse
from pathlib import Path

base = Path("build_out")

for f in base.glob("*.mmd"):
    code = f.read_text()
    encoded = urllib.parse.quote(code)
    svg = f"{f}.svg"

    import urllib.request
    url = f"https://mermaid.ink/svg/{encoded}"
    urllib.request.urlretrieve(url, svg)
