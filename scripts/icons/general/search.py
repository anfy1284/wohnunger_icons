#!/usr/bin/env python3
"""Поиск (лупа)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "search"
COLLECTION = "general"

def draw(d):
    # Линза
    d.ellipse(R(3, 3, 20, 20), fill=PAL['white'], outline=PAL['blue'], width=W(2.5))
    # Ручка
    d.line(P([(18, 18), (28, 28)]), fill=PAL['blue_dk'], width=W(3))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
