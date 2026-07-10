---
name: logo-author
description: Generate professional SVG logos with geometric design principles. Creates 3-5 variants per request, exports PNG in multiple sizes, and builds HTML showcase. No external API needed — pure SVG + Python. Use when creating logos, icons, or visual identities for projects.
---

# Logo Author

Generate high-quality SVG logos using geometric design principles.

## Design Principles

1. **Extreme Simplicity** — 1-2 core elements maximum
2. **Generous Negative Space** — 40-50% empty canvas
3. **Precise Proportions** — Line weights 2.5-4px
4. **Visual Tension** — Intentional asymmetry
5. **Restraint Over Decoration** — Justify every element
6. **Single Focal Point** — Clear visual hierarchy

## Workflow

### Phase 1 — Gather Context

Ask the user (or infer from project):
- **Product name** — what's it called?
- **Industry/Category** — tech, finance, health, creative, etc.
- **Core concept** — what's the one thing it does?
- **Design preferences** — minimal, geometric, playful, corporate?
- **Color palette** — or suggest one (see below)

### Phase 2 — Generate Variants

Generate **3-5 distinct SVG logo variants**. Each variant should explore a different direction:

| Variant | Style | Example |
|---|---|---|
| A | **Geometric** — circles, hexagons, triangles | Abstract mark from shapes |
| B | **Lettermark** — stylized first letter(s) | Monogram from initials |
| C | **Symbolic** — represent the core concept | Icon that maps to function |
| D | **Negative Space** — hidden meaning in gaps | Dual-meaning mark |
| E | **Wordmark** — stylized text only | Custom typography |

#### SVG Requirements

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <!-- Always use viewBox for scalability -->
  <!-- Define palette as CSS variables -->
  <style>
    :root {
      --primary: #6366f1;
      --accent: #ec4899;
      --dark: #1e1b4b;
      --light: #f8fafc;
    }
  </style>
  <!-- Shapes here -->
</svg>
```

#### Color Palette Suggestions

| Vibe | Primary | Accent | Dark | Light |
|---|---|---|---|---|
| **Tech/Modern** | `#6366f1` (indigo) | `#ec4899` (pink) | `#1e1b4b` | `#f8fafc` |
| **Trust/Finance** | `#059669` (emerald) | `#f59e0b` (amber) | `#064e3b` | `#f0fdf4` |
| **Creative** | `#f97316` (orange) | `#8b5cf6` (violet) | `#1c1917` | `#fffbeb` |
| **Minimal** | `#000000` | `#6b7280` | `#000000` | `#ffffff` |
| **Bold** | `#dc2626` (red) | `#2563eb` (blue) | `#0f172a` | `#fef2f2` |

### Phase 3 — Refine

User picks a variant. Offer adjustments:
- Color swap
- Stroke weight change
- Element scale/position
- Add/remove detail
- Rotate/align

### Phase 4 — Export

1. Save final SVG as `logo.svg`
2. Export PNG in standard sizes using `scripts/svg_to_png.py`:
   ```bash
   python scripts/svg_to_png.py logo.svg --sizes 16,32,48,192,512,1024,2048
   ```
3. Generate HTML showcase using `scripts/showcase.py`:
   ```bash
   python scripts/showcase.py logo.svg --output showcase.html
   ```

## SVG Generation Tips

### Geometric Primitives

```python
import xml.etree.ElementTree as ET

# Always use viewBox, never fixed width/height
svg = ET.Element("svg", {
    "xmlns": "http://www.w3.org/2000/svg",
    "viewBox": "0 0 200 200",
    "width": "200",
    "height": "200"
})

# Circle
ET.SubElement(svg, "circle", {
    "cx": "100", "cy": "100", "r": "60",
    "fill": "#6366f1"
})

# Rounded rect
ET.SubElement(svg, "rect", {
    "x": "50", "y": "50", "width": "100", "height": "100",
    "rx": "20", "fill": "#ec4899"
})

# Path (custom shapes)
ET.SubElement(svg, "path", {
    "d": "M100,40 L160,160 L40,160 Z",
    "fill": "#1e1b4b"
})

ET.ElementTree(svg).write("logo.svg")
```

### Design Patterns

See `references/design_patterns.md` for:
- Golden ratio layouts
- Lettermark construction
- Negative space techniques
- Monochrome vs duotone

### Background Styles

See `references/background_styles.md` for 12 showcase backgrounds.

## Pitfalls

- **Don't use emoji as logos** — they render differently across platforms
- **Don't use external fonts** — they won't render in SVG without embedding
- **Always set viewBox** — never rely on width/height alone
- **Keep SVG under 5KB** — complex paths bloat file size
- **Test on dark AND light backgrounds** — use a neutral or adaptable palette
- **Don't use raster images inside SVG** — defeats the purpose of vector
