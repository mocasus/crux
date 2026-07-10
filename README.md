<div align="center">

# 🎯 Crux

**Combo skill: Generate professional README + Logo in one workflow**

[![License](https://img.shields.io/github/license/mocasus/crux?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-2-blue?style=flat-square)](#-skills)
[![No API](https://img.shields.io/badge/No%20API-key%20needed-success?style=flat-square)](#-why-crux)

</div>

---

> Two skills, one goal: make any repo look professional in minutes. README author uses the Hook → Prove → Enable → Extend framework. Logo author generates SVG logos with geometric design principles — no external API, no paid services.

## ✨ Features

- **README Author** — Hook → Prove → Enable → Extend framework
  - Auto-detects project type (Python, Node, Rust, Go, etc.)
  - Generates badges, hero section, quick start, usage, architecture
  - Templates for badges and hero layouts
- **Logo Author** — SVG logo generation
  - 3-5 variants per request (geometric, lettermark, symbolic, negative space, wordmark)
  - 12 showcase background styles (dark + light)
  - PNG export in 7 standard sizes (16px → 2048px)
  - HTML showcase generator
- **No external API** — pure SVG + Python, works offline
- **Hermes + Claude Code compatible** — standard SKILL.md format

## 📦 Skills

| Skill | Description |
|---|---|
| `readme-author` | Generate README.md with Hook → Prove → Enable → Extend framework |
| `logo-author` | Generate SVG logos, export PNG, build HTML showcase |

## 🚀 Quick Start

### Install to Hermes

```bash
# Clone the repo
git clone https://github.com/mocasus/crux.git

# Copy skills to Hermes skills directory
cp -r crux/skills/* ~/.hermes/skills/
```

### Install to Claude Code

```bash
# Copy skills to Claude Code skills directory
cp -r crux/skills/* ~/.claude/skills/
```

### Usage

```
# Ask the agent:
"Bikin README + logo untuk project saya"
"Generate a logo for my project called DataFlow"
"Create a README for my Python library"
```

### PNG Export (Optional)

Logo author can export PNG if you have one of these installed:

```bash
# Option 1: Python (recommended)
pip install cairosvg

# Option 2: Node.js
npm install -g @aspect-build/resvg

# Option 3: System package
apt install librsvg2-bin   # Debian/Ubuntu
```

## 🏗️ Architecture

```
crux/
├── skills/
│   ├── readme-author/
│   │   ├── SKILL.md              # Hook → Prove → Enable → Extend
│   │   └── templates/
│   │       ├── badges.md         # Badge patterns & layouts
│   │       └── hero_layout.md   # 4 hero section layouts
│   │
│   └── logo-author/
│       ├── SKILL.md              # SVG generation workflow
│       ├── scripts/
│       │   ├── svg_to_png.py     # Multi-size PNG export
│       │   └── showcase.py       # HTML showcase generator
│       └── references/
│           ├── design_patterns.md    # Golden ratio, lettermarks, negative space
│           └── background_styles.md # 12 showcase backgrounds
│
├── examples/                     # Sample outputs
└── .github/
    └── workflows/
        └── ci.yml                # Validate SKILL.md syntax
```

## 🎨 Logo Design Principles

1. **Extreme Simplicity** — 1-2 core elements max
2. **Generous Negative Space** — 40-50% empty canvas
3. **Precise Proportions** — Line weights 2.5-4px
4. **Visual Tension** — Intentional asymmetry
5. **Single Focal Point** — Clear visual hierarchy

## 📄 License

[MIT](LICENSE) — free for personal and commercial use.
