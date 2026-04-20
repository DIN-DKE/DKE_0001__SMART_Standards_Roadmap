import re
from pathlib import Path
import sys

md = Path(sys.argv[1]).read_text()
out = Path(sys.argv[2])
out.mkdir(exist_ok=True, parents=True)

blocks = re.findall(r"```mermaid(.*?)```", md, re.S)

for i, b in enumerate(blocks):
    Path(out / f"diagram{i}.mmd").write_text(b.strip())
