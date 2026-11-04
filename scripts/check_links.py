#!/usr/bin/env python3
"""Validate local Markdown/HTML targets and self-contained SVG assets. No packages."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
external = set()
checked = 0
for document in ROOT.rglob("*.md"):
    if any(part in {".git", "build", "output"} for part in document.relative_to(ROOT).parts):
        continue
    text = document.read_text()
    targets = re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text)
    targets += re.findall(r'(?:src|href)="([^"]+)"', text)
    for target in targets:
        parsed = urlsplit(target)
        if parsed.scheme in {"http", "https"}:
            external.add(target)
            continue
        if parsed.scheme or not parsed.path:
            continue
        checked += 1
        candidate = (document.parent / unquote(parsed.path)).resolve()
        if not candidate.is_relative_to(ROOT) or not candidate.exists():
            errors.append(f"{document.relative_to(ROOT)}: missing local target {target}")
for asset in (ROOT / "assets").glob("*.svg"):
    tree = ET.parse(asset)
    for element in tree.iter():
        if element.tag.rsplit("}", 1)[-1] in {"script", "foreignObject"}:
            errors.append(f"{asset.name}: active SVG content")
        for key, value in element.attrib.items():
            if key.rsplit("}", 1)[-1] == "href" and not value.startswith("#"):
                errors.append(f"{asset.name}: external SVG reference")
if "--list-remote" in sys.argv:
    print("\n".join(sorted(external)))
else:
    print(f"Local links checked: {checked}; unique remote links: {len(external)}; SVG assets checked.")
for error in errors:
    print(error, file=sys.stderr)
sys.exit(bool(errors))
