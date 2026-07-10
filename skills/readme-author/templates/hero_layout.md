# Hero Section Layouts

## Layout 1: Centered Logo + Tagline (Default)

```markdown
<div align="center">

<img src="logo.png" width="200" alt="Project Logo">

# Project Name

**One-line tagline that explains the value proposition**

[![CI](badge)](link) [![License](badge)](link) [![Stars](badge)](link)

</div>

---

> Brief 2-3 sentence description of what this project is and why it exists.
```

## Layout 2: Left Logo + Right Text (Wide)

```markdown
<table>
<tr>
<td width="200" align="center">
<img src="logo.png" width="180" alt="Logo">
</td>
<td>

# Project Name

**Tagline here**

Badges row here.

Short description.

</td>
</tr>
</table>
```

## Layout 3: Minimal (No Logo)

```markdown
# Project Name

> Tagline here.

![CI](badge) ![License](badge) ![Stars](badge)
```

## Layout 4: Banner Style

```markdown
<div align="center">

<img src="banner.png" width="100%" alt="Banner">

**Project Name** — tagline

[![Badge]](link)

</div>
```

## Tagline Formulas

| Pattern | Example |
|---|---|
| **X for Y** | "Telegram bot framework for Python" |
| **Y, without X** | "Fast API testing, without boilerplate" |
| **The X way to Y** | "The simple way to deploy containers" |
| **X. Y. Z.** | "Fast. Reliable. Open source." |
| **Y in X seconds** | "Deploy a bot in 30 seconds" |

## Logo Sizing Guide

| Context | Width | Format |
|---|---|---|
| Hero (centered) | 150-250px | PNG |
| Hero (side) | 120-180px | PNG |
| README header | 100-150px | PNG |
| Favicon | 32px | ICO/PNG |
| Social card | 1200x630px | PNG |
