# scripts/render_mermaid.py

import re
import os
import subprocess
from pathlib import Path


INPUT = "idis-roadmap.md"
OUTPUT_MD = "build/idis-roadmap.md"
IMG_DIR = "build/img"
PUPPETEER_CONFIG = "scripts/puppeteer-config.json"

os.makedirs(IMG_DIR, exist_ok=True)

with open(INPUT, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"```mermaid(.*?)```", re.DOTALL)


def render_block(index, code):
    mmd_file = f"{IMG_DIR}/diagram_{index}.mmd"
    svg_file = f"{IMG_DIR}/diagram_{index}.svg"

    # Mermaid-Code speichern
    with open(mmd_file, "w", encoding="utf-8") as f:
        f.write(code.strip())

    # mmdc-Aufruf mit robuster Fehlerdiagnose
    cmd = [
        "mmdc",
        "-i", mmd_file,
        "-o", svg_file,
        "--backgroundColor", "transparent",
        "--puppeteerConfigFile", PUPPETEER_CONFIG
    ]

    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Mermaid rendering failed for block {index}")
        print("Command:", " ".join(cmd))
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
        raise

    return f'<img src="img/diagram_{index}.svg" alt="mermaid diagram {index}">'


def replace(match):
    idx = replace.counter
    replace.counter += 1
    code = match.group(1)
    return render_block(idx, code)


replace.counter = 0

print(f"Found {len(pattern.findall(content))} mermaid block(s)")

new_content = pattern.sub(replace, content)

# Ergebnis speichern
Path(OUTPUT_MD).parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Processed Markdown written to: {OUTPUT_MD}")
