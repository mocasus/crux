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

#### Step 1: MANDATORY — Load Design Patterns

**You MUST load `references/design_patterns.md` via skill_view BEFORE writing any SVG.** This file contains copy-paste-ready SVG patterns with exact coordinates. Generating logos without loading it produces low-quality results — every time.

```
skill_view(name='logo-author', file_path='references/design_patterns.md')
```

#### Step 2: SVG Construction Rules (NON-NEGOTIABLE)

These rules exist because they were violated repeatedly. Follow them exactly:

| Rule | Correct | Wrong | Why It Matters |
|------|---------|-------|----------------|
| **viewBox** | `viewBox="0 0 100 100"` | `viewBox="0 0 200 200"` | Stroke widths (2.5-4px) are calibrated for 100x100. Doubling the viewBox halves effective stroke thickness → fragile logos |
| **Color** | `fill="currentColor"` / `stroke="currentColor"` | `fill="#6366f1"` / hardcoded hex | `currentColor` = theme-adaptive (works on dark+light). Hardcoded = breaks on one theme |
| **Accent color** | At most ONE accent: `fill="#3b82f6"` on a single element | Multiple accent colors, gradients | Restraint = confidence. Gradient = generic AI startup |
| **Stroke width** | 3-5px for primary elements (in 100x100 viewBox) | 1.5-2px | Thin strokes look fragile and unprofessional |
| **Element count** | 1-3 core shapes | 5+ shapes | Simplicity = memorability |
| **Negative space** | 40-50% empty canvas | Elements filling most of canvas | Breathing room = sophistication |

#### Step 3: Generate Using Design Pattern Categories

Generate **6+ distinct SVG variants**. Use the pattern categories from `design_patterns.md` as your generation framework — NOT the abstract "directions" (geometric/lettermark/etc). The patterns have concrete SVG code you can adapt.

| # | Pattern Category | Source in design_patterns.md | Best For |
|---|-----------------|----------------------------|----------|
| A | **Geometric Shape** — concentric rings, arc segments, nested polygons, boolean intersections | Part 1.2 | Tech, data, infrastructure |
| B | **Dot Matrix** — circle dots (ring/grid), capsule dots (path-aligned), hexagon honeycomb | Part 1.1 | AI/ML, networks, data platforms |
| C | **Line System** — horizontal fill (circle mask), wave/curve, spiral/fibonacci | Part 1.3 | Code tools, audio, analytics |
| D | **Node Network** — topology with curved edges, asymmetric clusters | Part 1.4 | Agent frameworks, graphs, social |
| E | **Combination** — dot+shape, dot+lines, geometry+lines, layered composition | Part 2 | Complex products needing richer marks |
| F | **Letter/Symbol Integration** — geometric letter abstraction, dot matrix letter | Part 3 | Brand names, monograms |

**For each variant:**
1. Pick a pattern from design_patterns.md
2. Adapt its SVG code to the product's concept (change shapes, counts, positions)
3. Apply the construction rules above (viewBox 100, currentColor, stroke 3-5)
4. Add at most ONE accent color element if the concept demands it
5. Verify it passes the quality checklist (below)

**Color Palette Suggestions (accent only — base is always `currentColor`):**

| Vibe | Accent Color | Hex |
|------|-------------|-----|
| **Tech/Modern** | Indigo | `#6366f1` |
| **Trust/Finance** | Emerald | `#059669` |
| **Creative** | Orange | `#f97316` |
| **Bold** | Red | `#dc2626` |
| **Calm** | Teal | `#14b8a6` |
| **Energy** | Amber | `#f59e0b` |

**Iteration tracking:** Save numbered files: `logo_v1_a_geometric.svg`, `logo_v2_b_lettermark.svg`, etc.

#### Step 4: Quality Gate (SELF-CHECK BEFORE PRESENTING)

Before showing variants to the user, verify EACH variant against this checklist. If any fail, fix before presenting.

```
QUALITY GATE — check each variant:
[ ] viewBox="0 0 100 100" (NOT 200)
[ ] Uses currentColor for base (NOT hardcoded hex for main elements)
[ ] At most ONE accent color (NOT multiple, NOT gradient)
[ ] Primary stroke width ≥ 3px (NOT < 2.5)
[ ] Element count ≤ 3 core shapes (NOT 5+)
[ ] Negative space ≥ 40% (NOT packed tight)
[ ] Works at 16x16 favicon (mentally render at tiny size — still recognizable?)
[ ] Works on both dark AND light backgrounds (currentColor handles this)
[ ] Total SVG size < 3KB (NOT bloated with complex paths)
```

If you cannot honestly check all boxes for a variant, regenerate it.
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

**Presenting variants on messaging platforms (Telegram, Discord):** HTML showcases don't render in chat. Generate a PIL grid image (3×2 layout, 300px cells, white background, labeled) to send as a single photo. Example:
```python
from PIL import Image, ImageDraw, ImageFont
# Grid: 3 cols × 2 rows, each cell 300px, paste 200px logo centered + label
# Save as showcase_grid.png, send via MEDIA:path
```
This lets the user see all variants at once and pick by letter (A/B/C/D/E/F).

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

### Generation Pitfalls (Learned the Hard Way)

- **DON'T skip loading design_patterns.md** — Generating SVG from scratch without the reference produces consistently worse results. The reference has copy-paste patterns with exact coordinates. Always load it first.
- **DON'T use viewBox 200x200** — All stroke widths, dot sizes, and spacing in design_patterns.md are calibrated for viewBox 100x100. Using 200 halves everything → thin, fragile logos. Always use `viewBox="0 0 100 100"`.
- **DON'T use gradients** — Gradients look generic ("AI startup template"). Use solid fills only. If you need depth, use opacity (0.3-0.6 for secondary elements), not gradients.
- **DON'T hardcode multiple colors** — Use `currentColor` for base + at most ONE accent hex. Multiple hardcoded colors break theme-adaptivity and look busy.
- **DON'T use stroke < 2.5px** — Looks fragile and weak. Use 3-5px for primary elements in 100x100 viewBox.
- **DON'T use emoji as logos** — they render differently across platforms
- **DON'T use external fonts** — they won't render in SVG without embedding
- **DON'T set viewBox incorrectly** — always use `viewBox="0 0 100 100"`, never 200x200 or arbitrary sizes
- **DON'T use raster images inside SVG** — defeats the purpose of vector
- **DON'T skip the favicon check** — if it doesn't read at 16x16, simplify
- **DON'T add shadows or filters "because we can"** — restraint signals confidence
- **DON'T pack elements tightly** — minimum 8-12px spacing for breathing room
- **DON'T present variants without passing the Quality Gate** — self-check EVERY variant before showing to user. Fix failures first.
- **Don't pack elements tightly** — minimum 8-12px spacing for breathing room
- **`svg_to_png.py` exports to CWD, not next to the SVG** — always run it from the directory where you want PNGs, or move them after. The script does NOT honor the SVG's parent directory.
