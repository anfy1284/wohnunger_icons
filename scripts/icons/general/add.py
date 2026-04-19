#!/usr/bin/env python3
"""Добавить (зелёный плюс)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "add"
COLLECTION = "general"

def draw(d):
    # Плюс — единый полигон (без внутренних швов)
    d.polygon(P([
        (13, 4), (18, 4), (18, 13), (27, 13), (27, 18), (18, 18),
        (18, 27), (13, 27), (13, 18), (4, 18), (4, 13), (13, 13)
    ]), fill=PAL['green'], outline=PAL['green_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
