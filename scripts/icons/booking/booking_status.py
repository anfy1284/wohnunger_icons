#!/usr/bin/env python3
"""Статус брони (документ с галочкой)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "booking_status"
COLLECTION = "booking"

def draw(d):
    # Документ
    d.polygon(P([(7, 2), (22, 2), (27, 7), (27, 28), (7, 28)]), fill=PAL['paper'], outline=PAL['outline'], width=W(1.5))
    d.polygon(P([(22, 2), (22, 7), (27, 7)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W(1))
    # Синий кружок с галочкой (в пределах холста)
    d.ellipse(R(2, 17, 14, 29), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))
    d.line(P([(4, 23), (7, 26), (12, 20)]), fill=PAL['white'], width=W(2))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
