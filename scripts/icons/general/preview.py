#!/usr/bin/env python3
"""Предпросмотр печати"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "preview"
COLLECTION = "general"

def draw(d):
    # Документ
    d.rectangle(R(3, 2, 21, 24), fill=PAL['paper'], outline=PAL['outline'], width=W(1.5))
    # Строки текста
    for y in (6, 9, 12, 15):
        d.line(P([(6, y), (18, y)]), fill=PAL['gray_lt'], width=W(0.5))
    # Лупа (побольше)
    d.ellipse(R(14, 14, 27, 27), fill=PAL['white'], outline=PAL['blue'], width=W(2.5))
    d.line(P([(25, 25), (29, 29)]), fill=PAL['blue_dk'], width=W(2.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
