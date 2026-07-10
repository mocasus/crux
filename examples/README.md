# Examples

Sample outputs from the logo-author and readme-author skills.

## Logo Variants

When you run logo-author, it generates 3-5 SVG variants:

| Variant | Style | Description |
|---|---|---|
| A | Geometric | Abstract mark from circles, hexagons, triangles |
| B | Lettermark | Stylized first letter(s) as monogram |
| C | Symbolic | Icon representing the core concept |
| D | Negative Space | Hidden meaning in gaps |
| E | Wordmark | Custom typography, text only |

## PNG Export

```bash
python skills/logo-author/scripts/svg_to_png.py logo.svg --all
```

Generates: `logo_16.png`, `logo_32.png`, `logo_48.png`, `logo_192.png`, `logo_512.png`, `logo_1024.png`, `logo_2048.png`

## HTML Showcase

```bash
python skills/logo-author/scripts/showcase.py logo.svg --output showcase.html
```

Generates an HTML page showing the logo on 12 background styles.
