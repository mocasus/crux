<div align="center">

<img src="logo.png" width="180" alt="Crux">

# Crux

**Generate professional README + Logo in one workflow — no external API needed**

[![License](https://img.shields.io/github/license/mocasus/crux?style=flat-square)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/mocasus/crux/ci.yml?style=flat-square&label=CI)](https://github.com/mocasus/crux/actions)
[![Skills](https://img.shields.io/badge/skills-2-blue?style=flat-square)](#-skills)
[![No%20API](https://img.shields.io/badge/No%20API-key%20needed-success?style=flat-square)](#-why-crux)

</div>

---

> Two skills, one goal: make any repo look professional in minutes. **readme-author** uses the Hook → Prove → Enable → Extend framework. **logo-author** generates SVG logos with geometric design principles — no external API, no paid services.

## ✨ Features

**readme-author**
- Hook → Prove → Enable → Extend framework
- Auto-detects project type (Python, Node, Rust, Go, etc.)
- Generates badges, hero section, quick start, usage, architecture
- Templates for badges and hero layouts

**logo-author**
- 3–5 SVG variants per request (geometric, lettermark, symbolic, negative space, wordmark)
- 12 showcase background styles (dark + light)
- PNG export in 7 standard sizes (16px → 2048px)
- HTML showcase generator
- Color palette suggestions by industry

## 🚀 Quick Start

### Install

```bash
# Clone
git clone https://github.com/mocasus/crux.git

# Copy skills to Hermes
cp -r crux/skills/* ~/.hermes/skills/

# Or copy to Claude Code
cp -r crux/skills/* ~/.claude/skills/
```

### Use

```
# Ask the agent:
"Bikin README + logo untuk project saya"
"Generate a logo for my project called DataFlow"
"Create a README for my Python library"
```

That's it. The agent loads the skill automatically and follows the workflow.

### PNG Export (Optional)

Logo export needs one of these:

```bash
pip install cairosvg                    # Python (recommended)
npm install -g @aspect-build/resvg      # Node.js
apt install librsvg2-bin                # Debian/Ubuntu
```

## 📖 Usage

### Logo Workflow

1. **Gather** — product name, industry, core concept, color preference
2. **Generate** — 3–5 SVG variants exploring different directions
3. **Refine** — pick a favorite, adjust colors/strokes/layout
4. **Export** — SVG + PNG (7 sizes) + HTML showcase (12 backgrounds)

```bash
# Export PNGs
python skills/logo-author/scripts/svg_to_png.py logo.svg --all

# Generate showcase
python skills/logo-author/scripts/showcase.py logo.svg --output showcase.html
```

### README Workflow

1. **Scan** — detect language, entry points, test framework, CI
2. **Extract** — name, description, license, dependencies
3. **Generate** — Hook → Prove → Enable → Extend sections
4. **Assemble** — badges, hero, quick start, architecture

## 📦 Skills

| Skill | Description |
|---|---|
| `readme-author` | Generate README.md with Hook → Prove → Enable → Extend framework |
| `logo-author` | Generate SVG logos, export PNG, build HTML showcase |

## 🏗️ Architecture

```
crux/
├── logo.svg                    # Crux's own logo (dogfooded)
├── logo.png                    # 512×512 PNG for README
├── skills/
│   ├── readme-author/
│   │   ├── SKILL.md            # Hook → Prove → Enable → Extend
│   │   └── templates/
│   │       ├── badges.md       # Badge patterns & layouts
│   │       └── hero_layout.md  # 4 hero section layouts
│   │
│   └── logo-author/
│       ├── SKILL.md            # SVG generation workflow
│       ├── scripts/
│       │   ├── svg_to_png.py   # Multi-size PNG export
│       │   └── showcase.py     # HTML showcase generator
│       └── references/
│           ├── design_patterns.md     # Golden ratio, lettermarks, negative space
│           └── background_styles.md   # 12 showcase backgrounds
│
├── logos/                      # Variants + showcase from logo design
└── .github/
    └── workflows/
        └── ci.yml              # Validate SKILL.md + Python scripts
```

## 🎨 Logo Design Principles

1. **Extreme Simplicity** — 1–2 core elements max
2. **Generous Negative Space** — 40–50% empty canvas
3. **Precise Proportions** — Line weights 2.5–4px
4. **Visual Tension** — Intentional asymmetry
5. **Single Focal Point** — Clear visual hierarchy

## 🤝 Contributing

PRs welcome. Areas to contribute:

- New logo variant styles (beyond the 5 default directions)
- New showcase background styles
- README templates for specific project types (CLI, web app, bot)
- Additional SVG-to-PNG exporter support

## 🗺️ Roadmap

- [ ] `combo` meta-skill that chains readme-author + logo-author
- [ ] Dark/light logo variants auto-generated from single source
- [ ] Social card generator (1200×630px)
- [ ] Favicon pack export (ICO + PNG + Apple touch icon)

## 📄 License

[MIT](LICENSE) — free for personal and commercial use.
