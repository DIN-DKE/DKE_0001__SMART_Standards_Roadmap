# scripts/render_mermaid.py
import re
import os
import subprocess
from pathlib import Path

INPUT = "README.md"
OUTPUT_MD = "build/processed.md"
IMG_DIR = "build/img"

os.makedirs(IMG_DIR, exist_ok=True)

with open(INPUT, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"```mermaid(.*?)```", re.DOTALL)

def render_block(index, code):
    mmd_file = f"{IMG_DIR}/diagram_{index}.mmd"
    svg_file = f"{IMG_DIR}/diagram_{index}.svg"

    with open(mmd_file, "w", encoding="utf-8") as f:
        f.write(code.strip())

    subprocess.run([
        "mmdc",
        "-i", mmd_file,
        "-o", svg_file,
        "--backgroundColor", "transparent"
    ], check=True)

    return f'<img src="{svg_file}" alt="mermaid diagram {index}">'

def replace(match):
    idx = replace.counter
    replace.counter += 1
    code = match.group(1)
    return render_block(idx, code)

replace.counter = 0

new_content = pattern.sub(replace, content)

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write(new_content)
