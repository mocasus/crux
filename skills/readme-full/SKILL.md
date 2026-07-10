---
name: readme-full
description: All-in-one skill that generates logo + README in a single workflow. Detects project type, creates 6+ SVG logo variants, exports PNG, then builds a scored README using the Hook → Prove → Enable → Extend framework. Use when starting a new project or doing a full branding upgrade.
---

# README Full

One skill, full pipeline: **logo → README → validate**. Detects your project, generates a logo, builds a professional README, and scores it — all in one workflow.

## When to Use

- **New project** — no README, no logo yet
- **Rebrand** — existing project needs a visual identity + README upgrade
- **Quick polish** — got a repo but it looks bare

## Pipeline (5 Phases)

### Phase 1 — Detect

Auto-detect from repo structure:

```
python references/../scripts/detect_project.py ./
```

Or check manually:
- `package.json` → Node.js (library/CLI/web app)
- `pyproject.toml` / `setup.py` → Python
- `Cargo.toml` → Rust
- `go.mod` → Go
- `Dockerfile` → containerized app

Extract:
- **Name** — from package.json `name`, pyproject.toml `[project] name`, or directory
- **Description** — from manifest or first line of existing README
- **License** — from LICENSE file
- **CI** — check `.github/workflows/`
- **Test framework** — pytest, jest, go test, etc.

### Phase 2 — Logo

Generate **6+ SVG variants** across 5 design directions:

| # | Direction | Style |
|---|-----------|-------|
| A | Geometric | circles, hexagons, triangles |
| B | Lettermark | stylized initials |
| C | Symbolic | icon representing core concept |
| D | Negative Space | hidden meaning in gaps |
| E | Wordmark | custom typography |
| F | Wildcard | fusion of 2+ directions |

**Design checklist (must pass before presenting):**
- [ ] 1-2 core elements max
- [ ] 40-50% negative space
- [ ] Line weight 2.5-4px
- [ ] Clear focal point
- [ ] Works at 16x16 (favicon) and 512x512
- [ ] Tested on dark AND light backgrounds

**Color palette suggestions:**

| Vibe | Primary | Accent | Dark | Light |
|------|---------|--------|------|-------|
| Tech/Modern | `#6366f1` | `#ec4899` | `#1e1b4b` | `#f8fafc` |
| Trust/Finance | `#059669` | `#f59e0b` | `#064e3b` | `#f0fdf4` |
| Creative | `#f97316` | `#8b5cf6` | `#1c1917` | `#fffbeb` |
| Minimal | `#000000` | `#6b7280` | `#000000` | `#ffffff` |
| Bold | `#dc2626` | `#2563eb` | `#0f172a` | `#fef2f2` |

User picks favorite → refine → export:

```bash
# PNG export (7 sizes: 16-2048px)
python scripts/svg_to_png.py logo.svg --all
# OR
bash scripts/export.sh logo.svg ./logos/

# HTML showcase
python scripts/showcase.py logo.svg --output showcase.html
```

### Phase 3 — Refine Logo

User picks 1-2 favorites. Offer:
- Color swap
- Stroke weight change
- Element scale/position
- Add/remove detail
- Rotate/align
- Dark/light variant test

Save as `logo.svg` + export PNGs when approved.

### Phase 4 — Generate README

Build README using **Hook → Prove → Enable → Extend** framework:

**Hook (first 3 seconds):**
```markdown
<div align="center">

<!-- Logo -->
<img src="logo.png" width="180" alt="ProjectName">

# Project Name
<!-- Tagline: what it does + why it matters -->

<!-- Badges: 4-7, consistent style, no fakes -->
[![License](...)](...)
[![CI](...)](...)

</div>

> Pain point narrative or one-liner description.

<!-- Demo GIF/screenshot -->
```

**Prove (next 30 seconds):**
- Quick start — install + run in 30 seconds
- Feature list — bullets with benefits
- Code example — minimal working snippet with output
- Benchmarks — comparison table if available

**Enable (next 2 minutes):**
- Configuration — env vars, config files
- API reference — link, not inline
- Architecture — Mermaid diagram or tree
- Advanced usage — power user patterns

**Extend (ongoing):**
- Contributing guide
- Roadmap
- License
- Credits
- Community links
- Tiered CTAs (pick 2-3 max)

**Section order:**
```markdown
<!-- Logo (centered) -->
# Project Name
<!-- Tagline -->
<!-- Badges -->
> Description.
<!-- Demo -->

## ✨ Features
## 🚀 Quick Start
## 📖 Usage
## ⚙️ Configuration
## 🏗️ Architecture
## 🤝 Contributing
## 🗺️ Roadmap
## 📄 License
```

**Project type adaptation:**
- **CLI** → terminal GIF, cross-platform install matrix, keybinding table, perf benchmarks
- **Library** → API reference table, 3-line quick example, changelog link
- **Web App** → live demo link, screenshots, env vars table, Docker quick start
- **AI/ML** → model card (YAML), hardware requirements, benchmark table, Colab links, BibTeX
- **Bot** → commands list, invite link, platform badge

### Phase 5 — Validate & Score

Run validation checklist against generated README:

**Scoring (100 points):**

| Tier | Weight | Key Checks |
|------|--------|------------|
| Essential | 40% | Logo, badges, one-liner, demo, install, code example, license, section order |
| Professional | 25% | TOC, feature highlights, multiple install methods, docs links, contributing, "used by" |
| Elite | 15% | Architecture diagram, contributor avatars |
| Virality | 20% | Aha moment in first 500px, comparison table, pain point narrative, CTAs, curiosity hook |

**Score tiers:**
- 0-40: Essential (missing critical elements)
- 41-60: Professional (solid, room for improvement)
- 61-80: Elite (exceptional)
- 81-100: Viral (maximum engagement)

Output report + recommendations. Target: 70+ for new projects.

## Scripts

- `scripts/svg_to_png.py` — PNG export via cairosvg (Python)
- `scripts/export.sh` — Multi-tool PNG export (resvg/sharp/inkscape/rsvg)
- `scripts/showcase.py` — Static HTML showcase generator
- `scripts/generate_showcase.py` — AI showcase via Gemini/Nano Banana (optional)
- `scripts/detect_project.py` — Auto-detect language/type/metadata
- `scripts/select_operation.py` — Analyze README → recommend operation

## References

- `references/design_patterns.md` — SVG design pattern library (dot matrix, geometric, lines, nodes)
- `references/background_styles.md` — 12 showcase backgrounds (6 dark + 6 light)
- `references/webgl_backgrounds.md` — 6 WebGL shader backgrounds
- `references/badges-and-visuals.md` — Badge patterns, social proof, GIF demos
- `references/validation-guide.md` — Scoring system + checklists (4 tiers)
- `references/project-types.md` — Templates: CLI, library, web app, AI/ML, bot

## Assets

- `assets/showcase_template.html` — React interactive showcase template

## Templates

- `templates/badges.md` — Badge construction patterns
- `templates/hero_layout.md` — 4 hero section layouts

## Pitfalls

- **Don't generate README before logo** — logo placement affects hero layout
- **Don't skip the favicon check** — if logo doesn't read at 16x16, simplify
- **Don't overuse badges** — 5-7 max in hero
- **Don't fake status** — if no CI, don't add a CI badge
- **Don't write essays** — bullet points beat paragraphs always
- **Don't put Features before value proposition** — Hook order matters
- **Don't use emoji as logos** — render differently across platforms
- **Don't use external fonts in SVG** — won't render without embedding
- **Keep SVG under 5KB** — complex paths bloat file size
- **Test logo on dark AND light backgrounds** — use currentColor or provide variants
