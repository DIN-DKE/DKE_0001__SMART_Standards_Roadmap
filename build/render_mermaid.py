import fs from "fs";
import path from "path";
import mermaid from "mermaid";

const dir = "build_out";

const files = fs.readdirSync(dir).filter(f => f.endsWith(".mmd"));

for (const f of files) {
    const code = fs.readFileSync(path.join(dir, f), "utf-8");

    const { svg } = await mermaid.render(
        "graphDiv",
        code
    );

    fs.writeFileSync(
        path.join(dir, f + ".svg"),
        svg
    );
}
