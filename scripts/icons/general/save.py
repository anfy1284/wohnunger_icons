#!/usr/bin/env python3
"""Сохранить (дискета)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "save"
COLLECTION = "general"

def draw(d):
    # Корпус дискеты
    d.rounded_rectangle(R(3, 3, 28, 29), radius=1*SCALE, fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1.5))
    # Этикетка сверху (белая с линиями)
    d.rectangle(R(7, 4, 24, 14), fill=PAL['white'])
    for y in (6, 8, 10, 12):
        d.line(P([(9, y), (22, y)]), fill=PAL['gray_lt'], width=W(0.5))
    # Металлическая шторка
    d.rectangle(R(9, 17, 22, 28), fill=PAL['gray_lt'], outline=PAL['gray'], width=W(1))
    # Прорезь
    d.rectangle(R(11, 19, 15, 26), fill=PAL['gray_dk'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
