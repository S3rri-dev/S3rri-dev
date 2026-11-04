#!/usr/bin/env python3
"""Build self-contained social link SVGs from the bundled MIT-licensed glyphs."""
from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

def element(parent, name, **attributes):
    return ET.SubElement(parent, f"{{{NS}}}{name}", attributes)

for filename, icon, label, width in [
    ("social-linkedin.svg", "linkedin", "LinkedIn", 100),
    ("social-instagram.svg", "instagram", "Instagram", 110),
    ("social-email.svg", "envelope", "Correo", 86),
    ("social-email.en.svg", "envelope", "Email", 86),
]:
    svg = ET.Element(f"{{{NS}}}svg", {
        "width": str(width), "height": "36", "viewBox": f"0 0 {width} 36",
        "role": "img", "aria-labelledby": "title",
    })
    element(svg, "title", id="title").text = label
    element(svg, "rect", x="0.5", y="0.5", width=str(width-1), height="35", rx="6",
            fill="#000000", stroke="#593038")
    group = element(svg, "g", transform="translate(9 9) scale(1.125)", fill="#F7F3ED")
    glyph = ET.parse(ROOT / "assets" / "icons" / f"{icon}.svg").getroot()
    for child in glyph:
        group.append(deepcopy(child))
    element(svg, "text", x="34", y="23", fill="#F7F3ED", **{
        "font-family": "Arial,Helvetica,sans-serif", "font-size": "14", "font-weight": "600"
    }).text = label
    element(svg, "path", d="M10 35h18", stroke="#C5A05A", **{"stroke-width": "2"})
    ET.indent(svg, space="  ")
    target = ROOT / "assets" / filename
    target.write_text(ET.tostring(svg, encoding="unicode") + "\n")
    print(filename)
