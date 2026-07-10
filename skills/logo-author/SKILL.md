---
name: logo-author
description: Generate professional SVG logos with geometric design principles. Creates 6+ variants per request across 5 design directions. Exports PNG in 7 sizes (16px–2048px). Builds interactive HTML showcase with 12 background styles. Optional AI showcase via Gemini/Nano Banana. No external API needed for core workflow — pure SVG + Python.
---

# Logo Author

Generate high-quality SVG logos using geometric design principles. Merges three approaches: op7418's multi-variant generation + showcase system, neonwatty's iterative interview workflow, and a pure-SVG design pattern library.

## Critical Design Principles (READ THIS FIRST)

These principles are non-negotiable. Every logo must pass the design checklist before presenting.

### What Makes a Logo "High-End"?

1. **Extreme Simplicity** — Each logo should have 1-2 core elements maximum
   - Bad: 15 hexagons in a grid (too busy, no focal point)
   - Good: A single thick circle, or 2 merging nodes

2. **Generous Negative Space** — At least 40-50% of the canvas should be empty
   - Negative space is not "wasted space" — it's part of the design

3. **Precise Proportions**
   - Line weights: 2.5-4px (in viewBox 0 0 100 100)
   - Dot sizes: 2-8px radius
   - Spacing between elements: minimum 8-12px
   - Bad: strokeWidth="1.5" looks weak, strokeWidth="6" looks clumsy

4. **Visual Tension Through Asymmetry** — Perfect symmetry is boring
   - Intentional imbalance: heavy bottom-left, light top-right

5. **Restraint Over Decoration** — Every element must justify its existence
   - Pure black on white/light gray, no unnecessary effects

6. **Single Focal Point** — The eye should know where to look immediately
   - One dominant element (large circle, main node cluster, central burst)

7. **Structural Stability** — Logos must have visual weight
   - Bad: 2-3 thin lines (strokeWidth < 2.5) with no solid mass
   - Good: Dense line systems (6-8 lines), solid shapes, or thick strokes (3-4)
   - Exception: If using line systems, use dense repetition (6+ lines)

8. **Rounded Negative Space Cuts** — When using cutouts, openings must be rounded
   - Circular or rounded-rectangle cutouts, never sharp corners

### Design Checklist (Use Before Finalizing)

- [ ] **Element count**: 1-2 core elements (max 5-6 total shapes)
- [ ] **Negative space**: At least 40% of canvas is empty
- [ ] **Line weight**: Primary elements use strokeWidth 2.5-4
- [ ] **Focal point**: Clear visual hierarchy
- [ ] **Asymmetry**: Intentional imbalance creates interest
- [ ] **Scalability**: Works at 16x16 (favicon) and 512x512
- [ ] **Restraint**: No unnecessary decoration or effects
- [ ] **Breathing room**: Minimum 8-12px spacing between elements

---

## Workflow (5 Phases)

### Phase 1 — Interview & Gather Context

Ask the user (or infer from project repo):

**Essential:**
- **Product name** — what's it called?
- **Industry/Category** — tech, finance, health, creative, etc.
- **Core concept** — what's the one thing it does? (one sentence)

**Optional (provide defaults if skipped):**
- **Design preferences** — minimal, geometric, playful, corporate?
- **Color palette** — or suggest one (see palette table below)
- **Brand personality** — serious, friendly, bold, calm?
- **Competitor logos** — what to differentiate from?
- **Existing brand assets** — fonts, colors, style guides?

**If working with a repo:**
- Read package.json / pyproject.toml for project name and description
- Check for existing logo or brand assets
- Infer industry from dependencies and keywords

### Phase 2 — Generate Variants (6+)

Generate **6+ distinct SVG logo variants**. Each variant explores a different design direction. Use `references/design_patterns.md` for SVG implementations.

| # | Direction | Description | Best For |
|---|-----------|-------------|----------|
| A | **Geometric** — circles, hexagons, triangles | Abstract mark from pure shapes | Tech, data, AI/ML |
| B | **Lettermark** — stylized first letter(s) | Monogram from initials | Short names, corporate |
| C | **Symbolic** — represent the core concept | Icon that maps to function | Any product |
| D | **Negative Space** — hidden meaning in gaps | Dual-meaning mark | Clever, memorable brands |
| E | **Wordmark** — stylized text only | Custom typography | Established names |
| F | **Bonus** — wildcard direction | Creative fusion of 2+ directions | Surprise factor |

**SVG Requirements:**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <!-- Always use viewBox for scalability -->
  <!-- Use currentColor for theme-adaptive logos -->
  <!-- Keep under 5KB — complex paths bloat file size -->
  <!-- Test on dark AND light backgrounds -->
</svg>
```

**Color Palette Suggestions:**

| Vibe | Primary | Accent | Dark | Light |
|------|---------|--------|------|-------|
| **Tech/Modern** | `#6366f1` (indigo) | `#ec4899` (pink) | `#1e1b4b` | `#f8fafc` |
| **Trust/Finance** | `#059669` (emerald) | `#f59e0b` (amber) | `#064e3b` | `#f0fdf4` |
| **Creative** | `#f97316` (orange) | `#8b5cf6` (violet) | `#1c1917` | `#fffbeb` |
| **Minimal** | `#000000` | `#6b7280` | `#000000` | `#ffffff` |
| **Bold** | `#dc2626` (red) | `#2563eb` (blue) | `#0f172a` | `#fef2f2` |

**Design Pattern Categories** (see `references/design_patterns.md` for full SVG code):
1. **Dot Matrix** — concentric rings, grid layout, capsule path, hexagon honeycomb
2. **Geometric Shapes** — concentric circles, arc segments, boolean intersections, nested polygons
3. **Line Systems** — horizontal fill (circle mask), wave/curve, spiral/fibonacci
4. **Node Networks** — basic topology, asymmetric clusters
5. **Combination Strategies** — dot+shape, dot+lines, line+shape fusion

**Iteration tracking:** Save numbered files: `logo_v1_a_geometric.svg`, `logo_v2_b_lettermark.svg`, etc.

### Phase 3 — Refine & Iterate

User picks 1-2 favorites. Offer targeted adjustments:

- **Color swap** — try different palette from suggestions
- **Stroke weight** — thicker (more bold) or thinner (more delicate)
- **Element scale/position** — adjust proportions
- **Add/remove detail** — simplify or add complexity
- **Rotate/align** — change orientation
- **Background adaptation** — test on dark vs light

**Refinement loop:**
1. User: "I like variant C, but make it bolder"
2. Generate 2-3 refinements of variant C: `logo_v2_c_bold.svg`, `logo_v2_c_bold_alt.svg`
3. User picks → or requests more changes → repeat

**Favicon check:** Always verify the logo works at 16x16px. If it doesn't read at favicon size, simplify.

### Phase 4 — Export

1. **Save final SVG** as `logo.svg` in project root

2. **Export PNG** using one of two methods:

   **Method A — Python (cairosvg):**
   ```bash
   python scripts/svg_to_png.py logo.svg --sizes 16,32,48,192,512,1024,2048
   ```

   **Method B — Shell (auto-detect best tool):**
   ```bash
   bash scripts/export.sh logo.svg ./logos/
   # Auto-detects: resvg → sharp → inkscape → rsvg-convert
   # Exports: 16, 32, 48, 192, 512, 1024, 2048px
   ```

3. **Generate HTML showcase** (pure SVG, no API needed):
   ```bash
   python scripts/showcase.py logo.svg --output showcase.html
   ```

4. **Optional: AI Showcase Images** (requires Gemini API):
   ```bash
   python scripts/generate_showcase.py "ProductName" logo_512.png --style iridescent
   python scripts/generate_showcase.py "ProductName" logo_512.png --all-styles
   ```
   Uses Nano Banana (Gemini 3.1 Flash Image Preview) to place the logo on 12 professional background styles. See `references/background_styles.md` and `references/webgl_backgrounds.md` for style descriptions.

### Phase 5 — Deliver & Integrate (Optional)

- **README integration** — add logo with `logo-author` companion skill
- **Favicon pack** — export ICO + PNG + Apple touch icon
- **Social card** — 1200×630px preview image
- **Dark/light variants** — auto-generate from single source

---

## References

- `references/design_patterns.md` — Comprehensive SVG design pattern library with code examples (dot matrix, geometric shapes, line systems, node networks, combination strategies)
- `references/background_styles.md` — 12 showcase background styles (6 dark: Void, Frosted Horizon, Fluid Abyss, Studio Spotlight, Analog Liquid, LED Matrix; 6 light: Editorial Paper, Iridescent Frost, Morning Aura, Clinical Studio, UI Container, Swiss Flat)
- `references/webgl_backgrounds.md` — 6 WebGL shader-based dynamic backgrounds (LED Matrix, Fluid Warping, Fabric Wave, Off-Center Ripple, Holographic Dispersion, Spiral Vortex)

## Scripts

- `scripts/svg_to_png.py` — Convert SVG to PNG using cairosvg (Python)
- `scripts/export.sh` — Multi-tool PNG export (auto-detects resvg/sharp/inkscape/rsvg-convert)
- `scripts/showcase.py` — Generate static HTML showcase page with all variants
- `scripts/generate_showcase.py` — Generate AI showcase images via Gemini/Nano Banana (optional, requires GEMINI_API_KEY)

## Assets

- `assets/showcase_template.html` — React-based interactive showcase template with dark/light toggle, logo aura effects, and responsive grid

## Pitfalls

- **Don't use emoji as logos** — they render differently across platforms
- **Don't use external fonts** — they won't render in SVG without embedding
- **Always set viewBox** — never rely on width/height alone
- **Keep SVG under 5KB** — complex paths bloat file size and slow rendering
- **Test on dark AND light backgrounds** — use `currentColor` or provide variants
- **Don't use raster images inside SVG** — defeats the purpose of vector
- **Don't skip the favicon check** — if it doesn't read at 16x16, simplify
- **Don't add gradients/shadows "because we can"** — restraint signals confidence
- **Don't use strokeWidth < 2.5** — looks fragile and weak
- **Don't pack elements tightly** — minimum 8-12px spacing for breathing room
