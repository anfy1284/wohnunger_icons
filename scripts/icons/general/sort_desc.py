#!/usr/bin/env python3
"""Сортировка по убыванию ↓"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "sort_desc"
COLLECTION = "general"

def draw(d):
    # Стрелка вниз
    d.line(P([(15.5, 4), (15.5, 27)]), fill=PAL['blue'], width=W(2.5))
    d.polygon(P([(9, 19), (15.5, 27), (22, 19)]), fill=PAL['blue'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
