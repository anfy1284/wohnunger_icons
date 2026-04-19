#!/usr/bin/env python3
"""Вырезать (ножницы)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "cut"
COLLECTION = "general"

def draw(d):
    # Лезвия (толстые, перекрещиваются)
    d.line(P([(7, 22), (24, 3)]), fill=PAL['gray_dk'], width=W(2.5))
    d.line(P([(24, 22), (7, 3)]), fill=PAL['gray_dk'], width=W(2.5))
    # Кольца для пальцев (поверх лезвий)
    d.ellipse(R(3, 20, 11, 28), fill=PAL['white'], outline=PAL['outline'], width=W(1.5))
    d.ellipse(R(20, 20, 28, 28), fill=PAL['white'], outline=PAL['outline'], width=W(1.5))
    # Ось/винт
    d.ellipse(R(14, 11, 17, 14), fill=PAL['gray'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
