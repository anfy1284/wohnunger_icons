#!/usr/bin/env python3
"""Чат / ИИ-ассистент (речевой пузырь с тремя точками)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "chat"
COLLECTION = "general"

def draw(d):
    # Тело пузыря (скруглённый прямоугольник)
    d.rounded_rectangle(R(3, 4, 29, 21), radius=W(3),
                        fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W(1.5))
    # Хвостик — рисуется поверх нижней границы (верхнее ребро на y=21)
    d.polygon(P([(9, 21), (9, 27), (16, 21)]),
              fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W(1.5))
    # Три точки диалога
    for cx in (10, 16, 22):
        d.ellipse(R(cx - 1.6, 11.0, cx + 1.6, 14.2), fill=PAL['blue_dk'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
