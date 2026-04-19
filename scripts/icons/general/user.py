#!/usr/bin/env python3
"""Пользователь"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "user"
COLLECTION = "general"

def draw(d):
    # Голова (круг)
    d.ellipse(R(10, 2, 21, 13), fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W(1.5))
    # Тело (полукруг — плечи)
    d.pieslice(R(3, 17, 28, 42), start=180, end=360, fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
