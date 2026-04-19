#!/usr/bin/env python3
"""Печать счёта (документ с $)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "invoice_print"
COLLECTION = "booking"

def draw(d):
    # Документ
    d.polygon(P([(7, 2), (22, 2), (27, 7), (27, 28), (7, 28)]), fill=PAL['paper'], outline=PAL['outline'], width=W(1.5))
    d.polygon(P([(22, 2), (22, 7), (27, 7)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W(1))
    # Строки
    for y in (12, 15, 18):
        d.line(P([(10, y), (24, y)]), fill=PAL['gray_lt'], width=W(0.5))
    # Зелёный кружок с $ (в пределах холста)
    d.ellipse(R(2, 17, 14, 29), fill=PAL['green'], outline=PAL['green_dk'], width=W(1))
    text_centered(d, "$", 8, PAL['white'], R(2, 16, 14, 29))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
