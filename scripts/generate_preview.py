#!/usr/bin/env python3
"""
Превью-лист: все иконки на одном изображении для визуальной проверки.
    python scripts/generate_preview.py
    python scripts/generate_preview.py --collection general
"""

import argparse
import importlib.util
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).parent
ICONS_DIR = SCRIPT_DIR / "icons"
OUTPUT_DIR = SCRIPT_DIR.parent / "output"

sys.path.insert(0, str(SCRIPT_DIR))
from lib.icon_base import new_canvas, CANVAS


def load_draw_fn(filepath):
    """Загружает функцию draw() из файла иконки."""
    spec = importlib.util.spec_from_file_location(filepath.stem, str(filepath))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.draw, mod.ICON_ID


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--collection', help='general или booking')
    args = parser.parse_args()

    collections = []
    if args.collection:
        collections = [ICONS_DIR / args.collection]
    else:
        collections = sorted([p for p in ICONS_DIR.iterdir() if p.is_dir()])

    for col_dir in collections:
        col_name = col_dir.name
        scripts = sorted(col_dir.glob("*.py"))
        if not scripts:
            continue

        cols = 8
        rows = (len(scripts) + cols - 1) // cols
        cell = 48
        margin = 8
        w = cols * cell + margin * 2
        h = rows * cell + margin * 2

        sheet = Image.new('RGBA', (w, h), (255, 255, 255, 255))

        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 9)
        except Exception:
            font = None

        sheet_draw = ImageDraw.Draw(sheet)

        for i, script in enumerate(scripts):
            try:
                draw_fn, icon_id = load_draw_fn(script)
                img, d = new_canvas()
                draw_fn(d)
                icon32 = img.resize((32, 32), Image.Resampling.LANCZOS)
                x = margin + (i % cols) * cell + 8
                y = margin + (i // cols) * cell
                sheet.paste(icon32, (x, y), icon32)
                if font:
                    sheet_draw.text((x, y + 33), icon_id[:6], fill=(100, 100, 100), font=font)
            except Exception as e:
                print(f"  ✗ {script.name}: {e}")

        path = OUTPUT_DIR / f"preview_{col_name}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(str(path))
        print(f"[PREVIEW] {col_name}: {len(scripts)} иконок → {path}")


if __name__ == "__main__":
    main()
