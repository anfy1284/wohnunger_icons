#!/usr/bin/env python3
"""
Генерация ВСЕХ иконок. Находит все .py файлы в scripts/icons/ и запускает их.
    python scripts/generate_all.py
    python scripts/generate_all.py --collection general
    python scripts/generate_all.py --collection booking
"""

import argparse
import importlib.util
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ICONS_DIR = SCRIPT_DIR / "icons"

sys.path.insert(0, str(SCRIPT_DIR))


def run_icon_script(filepath):
    """Загружает и выполняет один скрипт иконки."""
    spec = importlib.util.spec_from_file_location(filepath.stem, str(filepath))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        if hasattr(mod, 'generate') and hasattr(mod, 'draw'):
            mod.generate(mod.ICON_ID, mod.COLLECTION, mod.draw)
    except Exception as e:
        print(f"  ✗ {filepath.name}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Генерация всех иконок")
    parser.add_argument('--collection', help='general или booking')
    args = parser.parse_args()

    collections = []
    if args.collection:
        collections = [ICONS_DIR / args.collection]
    else:
        collections = sorted([p for p in ICONS_DIR.iterdir() if p.is_dir()])

    total = 0
    for col_dir in collections:
        col_name = col_dir.name
        scripts = sorted(col_dir.glob("*.py"))
        if not scripts:
            continue
        print(f"\n[{col_name}] {len(scripts)} иконок:")
        for script in scripts:
            run_icon_script(script)
            total += 1

    print(f"\n[DONE] Сгенерировано {total} иконок.")


if __name__ == "__main__":
    main()
