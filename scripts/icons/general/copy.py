#!/usr/bin/env python3
"""Копировать (два документа)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "copy"
COLLECTION = "general"

def draw(d):
    # Задний документ
    d.rounded_rectangle(R(9, 8, 28, 28), radius=1*SCALE, fill=PAL['paper'], outline=PAL['outline'], width=W(1.5))
    for y in (12, 16, 20, 24):
        d.line(P([(12, y), (25, y)]), fill=PAL['gray_lt'], width=W(0.5))
    # Передний документ
    d.rounded_rectangle(R(3, 3, 22, 23), radius=1*SCALE, fill=PAL['paper'], outline=PAL['outline'], width=W(1.5))
    for y in (7, 11, 15, 19):
        d.line(P([(6, y), (19, y)]), fill=PAL['gray_lt'], width=W(0.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
