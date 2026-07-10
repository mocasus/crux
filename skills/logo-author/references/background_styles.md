# Showcase Background Styles

12 curated backgrounds for logo presentation. Use in HTML showcase.

## Dark Styles

### 1. The Void
```css
background: #000000;
/* Optional: subtle noise via SVG filter */
```
Absolute black. Silver micro noise. For premium, dramatic presentation.

### 2. Frosted Horizon
```css
background: linear-gradient(180deg, #2d2d2d 0%, #1a1a1a 100%);
/* Titanium gray with organic texture */
```

### 3. Fluid Abyss
```css
background: radial-gradient(ellipse at 30% 40%, #1e1b4b 0%, #0f0a2e 70%);
/* Deep purple with fluid fusion */
```

### 4. Studio Spotlight
```css
background: radial-gradient(circle at 50% 30%, #2a2a2a 0%, #0a0a0a 80%);
/* Carbon gray with editorial lighting */
```

### 5. Analog Liquid
```css
background: #1a1a2e;
/* Metallic shimmer overlay on solid base */
```

### 6. LED Matrix
```css
background: #0a0a0a;
/* Digital retro with glowing green dots pattern */
```

## Light Styles

### 7. Editorial Paper
```css
background: #f5f5f0;
/* Off-white with subtle paper texture */
```

### 8. Iridescent Frost
```css
background: linear-gradient(135deg, #e0e0e0 0%, #f0f0f5 50%, #e8e0f0 100%);
/* Silver-gray with holographic hints */
```

### 9. Morning Aura
```css
background: linear-gradient(180deg, #fffbeb 0%, #fef3c7 100%);
/* Warm ivory with pastel colors */
```

### 10. Clinical Studio
```css
background: #ffffff;
/* Pure white with geometric shadow */
box-shadow: 0 20px 60px rgba(0,0,0,0.08);
```

### 11. UI Container
```css
background: rgba(255,255,255,0.7);
backdrop-filter: blur(20px);
/* Frosted glass container effect */
```

### 12. Swiss Flat
```css
background: #e63946;
/* Pure solid color, zero effects */
/* Swap color to match logo palette */
```

## Usage in Showcase

```html
<div class="showcase-grid">
  <div class="bg-card" style="background: #000;">
    <img src="logo.svg" alt="Logo on Void">
    <span>The Void</span>
  </div>
  <div class="bg-card" style="background: linear-gradient(180deg, #2d2d2d, #1a1a1a);">
    <img src="logo.svg" alt="Logo on Frosted">
    <span>Frosted Horizon</span>
  </div>
  <!-- ... repeat for all 12 styles -->
</div>
```
