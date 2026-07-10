# Badge Patterns

## Standard Badge Format

```markdown
![Badge](https://img.shields.io/badge/LABEL-VALUE-COLOR?style=STYLE&logo=LOGO&logoColor=white)
```

### Style Options
- `flat` (default) — clean, minimal
- `flat-square` — modern, sharp edges
- `for-the-badge` — large, bold (best for hero section)
- `plastic` — retro 3D effect

### Color Options
- `brightgreen` — success/passing
- `green` — stable
- `yellow` — warning/beta
- `orange` — deprecated
- `red` — error/failing
- `blue` — info
- `9cf` — light blue
- `ff69b4` — pink
- `000` — black (dark themes)

## Common Badges

### Language & Framework
```markdown
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-18+-green?style=flat-square&logo=node.js&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-1.70+-orange?style=flat-square&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-1.21+-00ADD8?style=flat-square&logo=go&logoColor=white)
```

### Package Registries
```markdown
![PyPI](https://img.shields.io/pypi/v/PROJECTNAME?style=flat-square&label=pypi)
![npm](https://img.shields.io/npm/v/PROJECTNAME?style=flat-square&label=npm)
![Crates.io](https://img.shields.io/crates/v/PROJECTNAME?style=flat-square)
```

### CI/CD
```markdown
![CI](https://img.shields.io/github/actions/workflow/status/USER/REPO/ci.yml?style=flat-square&label=CI)
![Deploy](https://img.shields.io/github/deployments/USER/REPO/production?style=flat-square&label=deploy)
```

### Repo Stats
```markdown
![Stars](https://img.shields.io/github/stars/USER/REPO?style=flat-square&label=⭐)
![License](https://img.shields.io/github/license/USER/REPO?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/USER/REPO?style=flat-square&label=updated)
```

### Social
```markdown
![Discord](https://img.shields.io/discord/SERVERID?style=flat-square&label=discord&logo=discord&logoColor=white)
![Twitter Follow](https://img.shields.io/twitter/follow/HANDLE?style=flat-square&label=twitter)
```

## Badge Row Layout (Hero)

```markdown
[![CI](badge-url)](actions-url)
[![Version](badge-url)](registry-url)
[![License](badge-url)](license-url)
[![Stars](badge-url)](repo-url)
```

## Collapsible Badge Section

```markdown
<details>
<summary>📊 More badges</summary>

[![Last Commit](badge)](repo)
[![Issues](badge)](issues)
[![PRs Welcome](badge)](prs)

</details>
```
