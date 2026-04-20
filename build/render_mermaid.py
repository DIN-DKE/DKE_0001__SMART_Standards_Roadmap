import base64
import zlib
from pathlib import Path
import urllib.request

def encode_mermaid(code: str) -> str:
    compressed = zlib.compress(code.encode("utf-8"))
    return base64.urlsafe_b64encode(compressed).decode("utf-8")

base = Path("build_out")

for f in base.glob("*.mmd"):
    code = f.read_text()

    encoded = encode_mermaid(code)

    url = f"https://mermaid.ink/svg/{encoded}"

    out_file = f.with_suffix(".mmd.svg")

    try:
        urllib.request.urlretrieve(url, out_file)
    except Exception as e:
        print(f"Failed rendering {f}: {e}")
        raise
