#!/usr/bin/env python3
"""Отменить (стрелка влево)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "undo"
COLLECTION = "general"

def draw(d):
    # Дуга от лева через верх к правой стороне
    d.arc(R(4, 4, 27, 22), start=180, end=360, fill=PAL['blue'], width=W(3))
    # Хвост справа вниз (прямоугольник)
    d.rectangle(R(24, 13, 29, 26), fill=PAL['blue'])
    # Наконечник стрелки слева
    d.polygon(P([(8, 6), (2, 13), (8, 20)]), fill=PAL['blue'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
