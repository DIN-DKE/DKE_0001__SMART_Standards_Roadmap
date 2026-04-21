import fs from "fs";
import path from "path";
import mermaid from "mermaid";
import { JSDOM } from "jsdom";

// ----------------------------
// 1. Fake DOM erzeugen
// ----------------------------
const dom = new JSDOM("<div id='container'></div>");
global.window = dom.window;
global.document = dom.window.document;

// Mermaid initialisieren
mermaid.initialize({ startOnLoad: false });

// ----------------------------
// 2. Diagramme rendern
// ----------------------------
const dir = "build_out";
const files = fs.readdirSync(dir).filter(f => f.endsWith(".mmd"));

let idx = 0;

for (const file of files) {
    const code = fs.readFileSync(path.join(dir, file), "utf-8");

    try {
        const { svg } = await mermaid.render(
            "diagram_" + idx,
            code
        );

        fs.writeFileSync(
            path.join(dir, file + ".svg"),
            svg
        );

        idx++;
    } catch (err) {
        console.error("Mermaid render failed:", err);
        process.exit(1);
    }
}
