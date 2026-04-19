#!/usr/bin/env python3
"""Календарь"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "calendar"
COLLECTION = "general"

def draw(d):
    # Основа календаря
    d.rounded_rectangle(R(3, 5, 28, 29), radius=1*SCALE, fill=PAL['white'], outline=PAL['outline'], width=W(1.5))
    # Красная шапка
    d.rectangle(R(4, 6, 27, 12), fill=PAL['red'])
    # Штырьки (прямоугольники)
    for x in (9, 15, 21):
        d.rectangle(R(x, 3, x+2, 8), fill=PAL['gray_dk'])
    # Дни — сетка 4×3
    for row in range(3):
        for col in range(4):
            x = 6 + col * 5.5
            y = 14 + row * 5
            d.rectangle(R(x, y, x+3, y+3), fill=PAL['gray_lt'])
    # Выделенный день
    d.rectangle(R(11.5, 19, 14.5, 22), fill=PAL['blue'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
