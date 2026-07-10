#!/usr/bin/env python3
"""Export SVG to PNG in multiple sizes.

Usage:
    python svg_to_png.py logo.svg --sizes 16,32,48,192,512,1024,2048
    python svg_to_png.py logo.svg --size 512
    python svg_to_png.py logo.svg --all

Requires: cairosvg (pip install cairosvg) or resvg (npm install -g @aspect-build/resvg)
"""

import argparse
import subprocess
import sys
from pathlib import Path

DEFAULT_SIZES = [16, 32, 48, 192, 512, 1024, 2048]


def export_cairosvg(svg_path: str, output_dir: str, sizes: list[int]) -> bool:
    """Export using cairosvg (Python)."""
    try:
        import cairosvg
    except ImportError:
        print("cairosvg not installed. Install with: pip install cairosvg", file=sys.stderr)
        return False

    svg_file = Path(svg_path)
    for size in sizes:
        output = Path(output_dir) / f"{svg_file.stem}_{size}.png"
        cairosvg.svg2png(
            url=str(svg_file),
            write_to=str(output),
            output_width=size,
            output_height=size,
        )
        print(f"  ✓ {output.name} ({size}x{size})")
    return True


def export_resvg(svg_path: str, output_dir: str, sizes: list[int]) -> bool:
    """Export using resvg (Node.js)."""
    svg_file = Path(svg_path)
    for size in sizes:
        output = Path(output_dir) / f"{svg_file.stem}_{size}.png"
        try:
            subprocess.run(
                ["resvg", str(svg_file), str(output), "--width", str(size), "--height", str(size)],
                check=True,
                capture_output=True,
            )
            print(f"  ✓ {output.name} ({size}x{size})")
        except FileNotFoundError:
            return False
        except subprocess.CalledProcessError as e:
            print(f"  ✗ resvg error: {e.stderr.decode()}", file=sys.stderr)
            return False
    return True


def export_rsvg(svg_path: str, output_dir: str, sizes: list[int]) -> bool:
    """Export using librsvg (rsvg-convert)."""
    svg_file = Path(svg_path)
    for size in sizes:
        output = Path(output_dir) / f"{svg_file.stem}_{size}.png"
        try:
            subprocess.run(
                ["rsvg-convert", "-w", str(size), "-h", str(size),
                 "-o", str(output), str(svg_file)],
                check=True,
                capture_output=True,
            )
            print(f"  ✓ {output.name} ({size}x{size})")
        except FileNotFoundError:
            return False
        except subprocess.CalledProcessError as e:
            print(f"  ✗ rsvg error: {e.stderr.decode()}", file=sys.stderr)
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Export SVG to PNG in multiple sizes")
    parser.add_argument("svg", help="Path to SVG file")
    parser.add_argument("--sizes", help="Comma-separated sizes (default: 16,32,48,192,512,1024,2048)")
    parser.add_argument("--size", type=int, help="Single size")
    parser.add_argument("--all", action="store_true", help="Export all default sizes")
    parser.add_argument("--output-dir", default=".", help="Output directory")
    args = parser.parse_args()

    if args.size:
        sizes = [args.size]
    elif args.sizes:
        sizes = [int(s.strip()) for s in args.sizes.split(",")]
    else:
        sizes = DEFAULT_SIZES

    svg_path = Path(args.svg)
    if not svg_path.exists():
        print(f"Error: {svg_path} not found", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Exporting {svg_path.name} → {len(sizes)} PNG(s)")

    # Try exporters in order of preference
    for exporter_name, exporter_fn in [
        ("cairosvg", export_cairosvg),
        ("resvg", export_resvg),
        ("rsvg-convert", export_rsvg),
    ]:
        if exporter_fn(str(svg_path), str(output_dir), sizes):
            print(f"\nDone! Exported via {exporter_name}.")
            return

    print("\nNo SVG-to-PNG converter found. Install one of:", file=sys.stderr)
    print("  pip install cairosvg", file=sys.stderr)
    print("  npm install -g @aspect-build/resvg", file=sys.stderr)
    print("  apt install librsvg2-bin  (provides rsvg-convert)", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
