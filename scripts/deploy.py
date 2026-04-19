#!/usr/bin/env python3
"""
Деплой иконок из output/ в приложения фреймворка и проекта.
    python scripts/deploy.py
"""

import json
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
CONFIG_DIR = PROJECT_DIR / "config"
OUTPUT_DIR = PROJECT_DIR / "output"


def main():
    settings = json.loads((CONFIG_DIR / "deploy.json").read_text(encoding="utf-8"))

    targets = settings["targets"]

    for entry in targets:
        collection = entry["collection"]
        target = Path(entry["target"])

        for size in (16, 32):
            src = OUTPUT_DIR / f"{size}x{size}" / collection
            if not src.exists():
                continue
            dst = target / f"{size}x{size}"
            dst.mkdir(parents=True, exist_ok=True)
            count = 0
            for png in src.glob("*.png"):
                shutil.copy2(str(png), str(dst / png.name))
                count += 1
            if count:
                print(f"[DEPLOY] {collection}/{size}x{size}: {count} → {dst}")

    print("[DONE]")


if __name__ == "__main__":
    main()
