#!/usr/bin/env python3
"""Документ"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "document"
COLLECTION = "general"

def draw(d):
    # Документ с загнутым уголком (уголок побольше)
    d.polygon(P([(7, 2), (20, 2), (27, 9), (27, 28), (7, 28)]), fill=PAL['paper'], outline=PAL['outline'], width=W(1.5))
    d.polygon(P([(20, 2), (20, 9), (27, 9)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W(1))
    # Строки текста
    for y in (14, 17, 20, 23):
        d.line(P([(10, y), (24, y)]), fill=PAL['gray_lt'], width=W(0.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
