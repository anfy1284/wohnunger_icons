#!/usr/bin/env python3
"""Новый документ"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "document_new"
COLLECTION = "general"

def draw(d):
    # Документ с загнутым уголком (уголок побольше)
    d.polygon(P([(7, 2), (20, 2), (27, 9), (27, 28), (7, 28)]), fill=PAL['paper'], outline=PAL['outline'], width=W(1.5))
    d.polygon(P([(20, 2), (20, 9), (27, 9)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W(1))
    # Зелёный кружок с плюсом
    d.ellipse(R(2, 17, 14, 29), fill=PAL['green'], outline=PAL['green_dk'], width=W(1))
    d.line(P([(5, 23), (11, 23)]), fill=PAL['white'], width=W(2))
    d.line(P([(8, 20), (8, 26)]), fill=PAL['white'], width=W(2))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
