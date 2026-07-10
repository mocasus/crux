---
name: readme-author
description: Generate high-impact GitHub README files using the Hook → Prove → Enable → Extend framework. Analyzes repo structure, creates hero sections, assembles badges, and embeds logos. Use when starting a new project or upgrading an existing README.
---

# README Author

Generate professional GitHub README files that make repos stand out.

## Framework: Hook → Prove → Enable → Extend

### Phase 1 — Hook (first 3 seconds)
The hero section must communicate value instantly:
- **Logo** (if available, use logo-author skill or existing logo)
- **One-line tagline** — what this project does, not what it is
- **Key badges** — CI, version, license, stars (max 5, no clutter)
- **Screenshot/demo** — visual proof if applicable

### Phase 2 — Prove (next 30 seconds)
Show evidence the project works:
- **Quick start** — copy-paste install + run in under 30 seconds
- **Feature list** — bullet points, not paragraphs
- **Code example** — minimal working snippet
- **Performance/benchmarks** — if available

### Phase 3 — Enable (next 2 minutes)
Help users go deeper:
- **Configuration** — env vars, config files, options table
- **API reference** — link to docs, not inline
- **Architecture** — diagram or tree structure
- **Advanced usage** — power user patterns

### Phase 4 — Extend (ongoing)
Make it easy to contribute:
- **Contributing guide** — link to CONTRIBUTING.md
- **Roadmap** — what's coming next
- **License** — one line + link
- **Credits** — acknowledge dependencies and contributors

## Workflow

1. **Scan repo structure**
   - Identify language: check `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.
   - Find entry points: `main.py`, `index.js`, `src/lib.rs`, etc.
   - Detect test framework: `pytest`, `jest`, `go test`, etc.
   - Check for CI: `.github/workflows/`, `.gitlab-ci.yml`, etc.

2. **Extract metadata**
   - Project name (from package.json name field, pyproject.toml [project] name, or directory name)
   - Description (from package.json description, pyproject.toml description, or first line of existing README)
   - License (from LICENSE file or package.json license field)
   - Dependencies count

3. **Generate README**
   - Use templates from `templates/` directory
   - Adapt sections based on project type (library, CLI, web app, bot, etc.)
   - If logo-author skill is available, offer to generate logo first

4. **Assemble badges**
   - See `templates/badges.md` for badge patterns
   - Only include badges that are accurate — never fake CI status

5. **Write README.md**
   - Write to project root
   - Offer to preview before overwriting existing README

## Section Order (Standard)

```markdown
# Project Name
<!-- logo if available -->
<!-- tagline -->
<!-- badges -->

> Short description.

## ✨ Features
## 🚀 Quick Start
## 📖 Usage
## ⚙️ Configuration
## 🏗️ Architecture
## 🤝 Contributing
## 📄 License
```

## Project Type Adaptation

| Type | Extra Sections | Badge Style |
|---|---|---|
| **Library** | API Reference, Changelog | npm/pypi version |
| **CLI** | Commands, Flags table | install count |
| **Web App** | Demo link, Screenshots | deploy status |
| **Bot** | Commands list, Invite link | platform badge |
| **Skill** | Skill list, Installation | skill count |

## Pitfalls

- **Don't overuse badges** — 5 max in hero, rest in a collapsible section
- **Don't write essays** — bullet points beat paragraphs
- **Don't fake status** — if no CI, don't add a CI badge
- **Don't forget the license** — it's the most important line
- **Check existing README first** — preserve user's voice and style
