#!/usr/bin/env python3
"""Generate HTML showcase for a logo across 12 background styles.

Usage:
    python showcase.py logo.svg --output showcase.html
    python showcase.py logo.svg --open
"""

import argparse
import base64
from pathlib import Path

BG_STYLES = [
    ("The Void", "#000000", "#ffffff"),
    ("Frosted Horizon", "linear-gradient(180deg, #2d2d2d 0%, #1a1a1a 100%)", "#ffffff"),
    ("Fluid Abyss", "radial-gradient(ellipse at 30% 40%, #1e1b4b 0%, #0f0a2e 70%)", "#ffffff"),
    ("Studio Spotlight", "radial-gradient(circle at 50% 30%, #2a2a2a 0%, #0a0a0a 80%)", "#ffffff"),
    ("Analog Liquid", "#1a1a2e", "#e0e0e0"),
    ("LED Matrix", "#0a0a0a", "#00ff00"),
    ("Editorial Paper", "#f5f5f0", "#1a1a1a"),
    ("Iridescent Frost", "linear-gradient(135deg, #e0e0e0 0%, #f0f0f5 50%, #e8e0f0 100%)", "#1a1a1a"),
    ("Morning Aura", "linear-gradient(180deg, #fffbeb 0%, #fef3c7 100%)", "#1a1a1a"),
    ("Clinical Studio", "#ffffff", "#1a1a1a"),
    ("UI Container", "rgba(255,255,255,0.7)", "#1a1a1a"),
    ("Swiss Flat", "#e63946", "#ffffff"),
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — Logo Showcase</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0a0a0a; color: #fff; }}
.header {{ text-align: center; padding: 60px 20px 40px; }}
.header h1 {{ font-size: 2.5rem; font-weight: 700; letter-spacing: -0.02em; }}
.header p {{ color: #888; margin-top: 8px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2px; }}
.card {{ position: relative; aspect-ratio: 1; display: flex; align-items: center; justify-content: center; overflow: hidden; }}
.card img {{ width: 40%; height: auto; filter: drop-shadow(0 4px 20px rgba(0,0,0,0.3)); }}
.card .label {{ position: absolute; bottom: 16px; left: 16px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.7; }}
</style>
</head>
<body>
<div class="header">
  <h1>{name}</h1>
  <p>Logo Showcase — 12 background styles</p>
</div>
<div class="grid">
{cards}
</div>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Generate HTML logo showcase")
    parser.add_argument("svg", help="Path to SVG file")
    parser.add_argument("--output", default="showcase.html", help="Output HTML file")
    args = parser.parse_args()

    svg_path = Path(args.svg)
    if not svg_path.exists():
        print(f"Error: {svg_path} not found", file=sys.stderr)
        return

    # Embed SVG as base64 data URI
    svg_data = svg_path.read_bytes()
    svg_b64 = base64.b64encode(svg_data).decode()
    svg_uri = f"data:image/svg+xml;base64,{svg_b64}"

    cards = []
    for name, bg, fg in BG_STYLES:
        card = f'''    <div class="card" style="background: {bg}; color: {fg};">
      <img src="{svg_uri}" alt="{name}">
      <span class="label">{name}</span>
    </div>'''
        cards.append(card)

    html = HTML_TEMPLATE.format(
        name=svg_path.stem.replace("-", " ").replace("_", " ").title(),
        cards="\n".join(cards),
    )

    output = Path(args.output)
    output.write_text(html, encoding="utf-8")
    print(f"✓ Showcase generated: {output}")
    print(f"  Logo: {svg_path.name}")
    print(f"  Styles: {len(BG_STYLES)}")


if __name__ == "__main__":
    main()
