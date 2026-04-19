#!/usr/bin/env python3
"""Вставить (буфер обмена)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "paste"
COLLECTION = "general"

def draw(d):
    # Планшет (буфер обмена)
    d.rounded_rectangle(R(5, 5, 26, 28), radius=2*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W(1.5))
    # Зажим сверху
    d.rounded_rectangle(R(11, 2, 20, 7), radius=1*SCALE, fill=PAL['gray'], outline=PAL['gray_dk'], width=W(1))
    # Бумага
    d.rectangle(R(8, 10, 23, 26), fill=PAL['white'], outline=PAL['gray'], width=W(1))
    # Строки
    for y in (13, 16, 19, 22):
        d.line(P([(10, y), (21, y)]), fill=PAL['gray_lt'], width=W(0.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
