#!/usr/bin/env python3
"""Выбрать все (чекбокс с галочкой)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "select_all"
COLLECTION = "general"

def draw(d):
    # Чекбокс
    d.rounded_rectangle(R(3, 3, 28, 28), radius=2*SCALE, fill=PAL['white'], outline=PAL['blue'], width=W(2))
    # Галочка
    d.line(P([(8, 16), (13, 22), (24, 8)]), fill=PAL['green'], width=W(3))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
