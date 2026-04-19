#!/usr/bin/env python3
"""Назад ◄"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "prev"
COLLECTION = "general"

def draw(d):
    # Треугольник влево
    d.polygon(P([(22, 4), (8, 15.5), (22, 27)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
