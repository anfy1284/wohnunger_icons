#!/usr/bin/env python3
"""Фильтр (воронка)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "filter"
COLLECTION = "general"

def draw(d):
    # Воронка — единый полигон (без внутренних швов)
    d.polygon(P([
        (3, 4), (28, 4), (18, 16), (18, 28), (13, 28), (13, 16)
    ]), fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
