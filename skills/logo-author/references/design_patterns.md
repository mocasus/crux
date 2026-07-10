# Design Patterns for Logo Generation

## Golden Ratio Layout

The golden ratio (1:1.618) creates naturally pleasing proportions:

```
┌─────────────────────────────────┐
│                                 │
│   ┌──────────────────┐          │
│   │                  │          │
│   │    Logo Element  │  1.618x  │
│   │      (1x)        │  margin  │
│   │                  │          │
│   └──────────────────┘          │
│                                 │
└─────────────────────────────────┘
```

- Logo element occupies ~62% of canvas width
- Margins follow golden ratio spacing
- Focal point slightly above center (optical center)

## Lettermark Construction

### Grid-Based Letters

```
Build letters on a 5x7 grid:

  █████████
  ██     ██
  ██     ██
  █████████
  ██     ██
  ██     ██
  █████████

  → Convert grid cells to rounded rects
  → Vary stroke weight for visual interest
```

### Techniques

| Technique | Effect | Example |
|---|---|---|
| **Overlap** | Two letters share a stroke | "CR" sharing vertical line |
| **Negative** | Cut one letter from another | "U" cut from "C" |
| **Shared Stroke** | One stroke serves both letters | "X" where two lines cross |
| **Rotation** | Rotate a letter to form another | "N" rotated = "Z" base |
| **Stacking** | Stack letters vertically | Monogram style |

## Negative Space Techniques

### Hidden Meaning

```
Pattern 1 — Shape within shape:
  ┌──────────────┐
  │ ████████████ │
  │ ██  ██  ██  │  ← gaps form a letter
  │ ████████████ │
  └──────────────┘

Pattern 2 — Counter-form:
  A solid circle with a bite = moon shape
  A solid square with a circle cut = frame

Pattern 3 — Dual image:
  Arrow hidden in negative space of "E"
```

## Monochrome vs Duotone

### Monochrome
- Single color + opacity variations
- Best for: minimal, corporate, timeless
- Works on any background with color swap

### Duotone
- Two colors maximum
- Best for: modern, tech, creative
- Use complementary or analogous colors:
  - Indigo + Pink (tech)
  - Emerald + Amber (finance)
  - Orange + Violet (creative)

## Shape Psychology

| Shape | Conveys | Industries |
|---|---|---|
| **Circle** | Unity, completeness, community | Social, health, education |
| **Square** | Stability, trust, order | Finance, enterprise, legal |
| **Triangle** | Direction, growth, energy | Startups, transport, energy |
| **Hexagon** | Efficiency, nature, structure | Tech, engineering, bio |
| **Pentagon** | Human, organic, balanced | Wellness, food, lifestyle |

## Stroke Weight Guide

| Weight | Use Case |
|---|---|
| 1px | Fine detail, decorative |
| 2px | Secondary elements |
| 3px (default) | Main logo strokes |
| 4px | Bold, heavy logos |
| 6px+ | Very large display only |

## Alignment Rules

1. Optical center is 2-3% above mathematical center
2. Round corners to 1/4 of stroke width
3. Maintain 15% padding from canvas edge minimum
4. Elements should align to a consistent grid (8px or 10px)
