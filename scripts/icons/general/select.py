#!/usr/bin/env python3
"""Выбрать (зелёная галочка)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "select"
COLLECTION = "general"

def draw(d):
    # Галочка — единый полигон (без стыка линий)
    d.polygon(P([
        (4, 17), (7, 13), (12, 19), (27, 3), (29, 6), (12, 26)
    ]), fill=PAL['green'], outline=PAL['green_dk'], width=W(1))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
