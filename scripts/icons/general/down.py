#!/usr/bin/env python3
"""Вниз ▼"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "down"
COLLECTION = "general"

def draw(d):
    # Треугольник вниз
    d.polygon(P([(4, 8), (15.5, 25), (27, 8)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
