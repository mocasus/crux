---
name: readme-author
description: Generate high-impact GitHub README files using the Hook → Prove → Enable → Extend framework. Analyzes repo structure, creates hero sections, assembles badges, and embeds logos. Supports create, modify, validate, and optimize operations. Use when starting a new project or upgrading an existing README.
---

# README Author

Generate professional GitHub README files that make repos stand out. Framework based on analysis of 1000+ high-star GitHub repos — the patterns that actually drive stars, forks, and adoption.

## Operations

### `create` — New README from scratch
1. Scan repo → detect language, entry points, test framework, CI
2. Extract metadata → name, description, license, dependencies
3. Generate using Hook → Prove → Enable → Extend framework
4. Assemble badges → see `references/badges-and-visuals.md`
5. Write to project root

### `modify` — Improve existing README
1. Read existing README → preserve user's voice and style
2. Identify missing sections using validation checklist
3. Suggest targeted improvements (don't rewrite what works)
4. Apply changes with user approval

### `validate` — Score existing README
1. Run validation checklist (see `references/validation-guide.md`)
2. Score across 4 tiers: Essential (40%) / Professional (25%) / Elite (15%) / Virality (20%)
3. Output report with pass/fail per check and recommendations
4. Score tiers: Essential (0-40) / Professional (41-60) / Elite (61-80) / Viral (81-100)

### `optimize` — Maximize virality
1. Run validate first
2. Focus on Virality tier improvements
3. Add: pain point narrative, curiosity hook, comparison table, before/after demo
4. Re-score and report improvement

## Framework: Hook → Prove → Enable → Extend

### Phase 1 — Hook (first 3 seconds)
The hero section must communicate value instantly. This is where users decide to stay or leave.

**Required elements (in order):**
1. **Logo** — centered, width = half actual pixels (e.g., `width="180"` for 360px image). Use `logo-author` skill or existing logo. Use `<picture>` for dark/light mode support.
2. **Project name** — `# Title` immediately after logo
3. **Tagline** — one sentence: what it does + why it matters. NOT what it IS.
   - ✅ "Search 1M files in 0.2 seconds" (ripgrep)
   - ✅ "HTTP for Humans" (requests)
   - ❌ "A fast file search utility written in Rust"
4. **Badges** — 4-7 relevant badges. See `references/badges-and-visuals.md` for patterns.
   - Priority: CI status → version → license → stars (if >100) → downloads (if >1k/week)
   - Use ONE badge style consistently (flat, flat-square, or for-the-badge)
   - Never fake badges — if no CI, don't add a CI badge
5. **Demo visual** — GIF/screenshot showing the "aha moment" in the first 500px of scroll
   - CLI tools: terminal GIF (use vhs, terminalizer, or asciinema)
   - Web apps: screenshot of core interaction
   - Libraries: code snippet with commented output
6. **Archive notice** — if `.archived.md` exists, add notice at top

**Pain Point Narrative (Virality booster):**
```markdown
> Ever spent hours debugging X? Y solves this by...
```
Place between badges and demo. Transforms feature list into emotional connection.

### Phase 2 — Prove (next 30 seconds)
Show evidence the project works:
- **Quick start** — copy-paste install + run in under 30 seconds
  ```bash
  pip install mypackage
  mypackage --help
  ```
- **Feature list** — bullet points with benefits, not paragraphs
  - ✅ "🔒 Secure by default — AES-256 encryption out of the box"
  - ❌ "Security features"
- **Code example** — minimal working snippet with output
  ```python
  from mypackage import Feature
  result = Feature().run("input")
  print(result)  # Output: "Success"
  ```
- **Performance/benchmarks** — comparison table if available
  ```markdown
  | Tool | Time | Relative |
  |------|------|----------|
  | myapp | 0.082s | 1.00x |
  | alternative | 0.273s | 3.34x |
  ```

### Phase 3 — Enable (next 2 minutes)
Help users go deeper:
- **Configuration** — env vars table, config file examples
- **API reference** — link to docs, not inline walls of text
- **Architecture** — Mermaid diagram or directory tree
- **Advanced usage** — power user patterns and recipes
- **Multiple installation methods** — if applicable (pip, brew, apt, npm, cargo, from source)

### Phase 4 — Extend (ongoing)
Make it easy to contribute:
- **Contributing guide** — link to CONTRIBUTING.md
- **Roadmap** — what's coming next (shows active development)
- **License** — one line + link to LICENSE file
- **Credits** — acknowledge dependencies and contributors
- **Community links** — Discord, Twitter, etc. (if they exist)

**Tiered CTAs (pick 2-3 max):**
```markdown
- 🚀 [Try the demo](link) — see it in action
- 📖 [Read the docs](link) — go deeper
- 💬 [Join Discord](link) — get help fast
- ⭐ [Star on GitHub](link) — if this helped
```

## Section Order (Standard)

```markdown
<!-- Logo (centered) -->
# Project Name
<!-- Tagline -->
<!-- Badges -->

> Short description or pain point narrative.

<!-- Demo GIF/screenshot -->

## ✨ Features
## 🚀 Quick Start
## 📖 Usage
## ⚙️ Configuration
## 🏗️ Architecture
## 🤝 Contributing
## 🗺️ Roadmap
## 📄 License
```

## Project Type Adaptation

See `references/project-types.md` for detailed templates. Key adaptations:

- **CLI**: Terminal GIF, cross-platform install matrix, keybinding table, performance benchmarks
- **Library**: API reference table, 3-line quick example, changelog link
- **Web App**: Live demo link, screenshots (dark+light), env vars table, Docker quick start
- **AI/ML**: Model card (YAML), hardware requirements, benchmark table, Colab links, BibTeX citation
- **Bot**: Commands list, invite link, platform badge

## Writing Style

- **Bullet points over paragraphs** — scannability is everything
- **Bold key terms** — helps skimming
- **Code blocks with output** — proof > claims
- **Emoji in section headers only** — 1 per header, consistent set
- **No walls of text** — if a section exceeds 5 lines, break it up
- **Active voice** — "Install X" not "X can be installed"
- **Include thresholds** — "handles 10k+ req/s" not "high performance"

## Workflow

1. **Detect project type** — run `scripts/detect_project.py` or check manually:
   - `package.json` → Node.js (library/CLI/web app)
   - `pyproject.toml` / `setup.py` → Python (library/CLI)
   - `Cargo.toml` → Rust
   - `go.mod` → Go
   - `Dockerfile` → containerized app

2. **Extract metadata**:
   - Name: from package.json `name`, pyproject.toml `[project] name`, or directory
   - Description: from package.json `description`, or first line of existing README
   - License: from LICENSE file or package.json `license`
   - Dependencies: count from lockfile
   - Stars/forks: from GitHub API if available

3. **Select operation** — run `scripts/select_operation.py` or ask user:
   - No README? → `create`
   - Has README but missing sections? → `modify`
   - Want to score it? → `validate`
   - Want max impact? → `optimize`

4. **Generate README.md** — write to project root

5. **Validate** — run validation checklist against generated README

## Scripts

- `scripts/detect_project.py` — auto-detect language, type, and metadata from repo structure
- `scripts/select_operation.py` — analyze existing README and recommend operation

## References

- `references/badges-and-visuals.md` — badge patterns, social proof, GIF demos, testimonials
- `references/validation-guide.md` — scoring output format, checklists for all 4 tiers
- `references/project-types.md` — templates by type (CLI, library, web app, AI/ML, bot)

## Templates

- `templates/badges.md` — badge construction patterns and layouts
- `templates/hero_layout.md` — 4 hero section layout options

## Pitfalls

- **Don't overuse badges** — 5-7 max in hero, rest in collapsible section
- **Don't write essays** — bullet points beat paragraphs always
- **Don't fake status** — if no CI, don't add a CI badge
- **Don't forget the license** — it's the most important line
- **Don't skip the demo** — a GIF is worth 1000 words of description
- **Don't put Features before value proposition** — Hook order matters
- **Check existing README first** — preserve user's voice and style when modifying
- **Archive notice must match .archived.md** — present if file exists, absent if not
- **Don't include unimpressive metrics** — "2 stars" badge hurts more than it helps
