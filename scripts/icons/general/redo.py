#!/usr/bin/env python3
"""Повторить (стрелка вправо)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "redo"
COLLECTION = "general"

def draw(d):
    # Дуга от лева через верх к правой стороне
    d.arc(R(4, 4, 27, 22), start=180, end=360, fill=PAL['blue'], width=W(3))
    # Хвост слева вниз (прямоугольник для чистого стыка)
    d.rectangle(R(2, 13, 7, 26), fill=PAL['blue'])
    # Наконечник стрелки справа
    d.polygon(P([(23, 6), (29, 13), (23, 20)]), fill=PAL['blue'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
