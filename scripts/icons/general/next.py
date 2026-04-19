#!/usr/bin/env python3
"""Вперёд ►"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "next"
COLLECTION = "general"

def draw(d):
    # Треугольник вправо
    d.polygon(P([(9, 4), (23, 15.5), (9, 27)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
