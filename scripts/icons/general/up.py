#!/usr/bin/env python3
"""Вверх ▲"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "up"
COLLECTION = "general"

def draw(d):
    # Треугольник вверх
    d.polygon(P([(4, 23), (15.5, 6), (27, 23)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
