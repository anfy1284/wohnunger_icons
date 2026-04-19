#!/usr/bin/env python3
"""Часы"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "clock"
COLLECTION = "general"

def draw(d):
    # Циферблат
    d.ellipse(R(3, 3, 28, 28), fill=PAL['white'], outline=PAL['outline'], width=W(1.5))
    # Метки часов (12, 3, 6, 9)
    d.line(P([(15.5, 5), (15.5, 7)]), fill=PAL['outline'], width=W(1))
    d.line(P([(15.5, 24), (15.5, 26)]), fill=PAL['outline'], width=W(1))
    d.line(P([(5, 15.5), (7, 15.5)]), fill=PAL['outline'], width=W(1))
    d.line(P([(24, 15.5), (26, 15.5)]), fill=PAL['outline'], width=W(1))
    # Часовая стрелка (вверх)
    d.line(P([(15.5, 15.5), (15.5, 7)]), fill=PAL['black'], width=W(2))
    # Минутная стрелка (вправо-вверх)
    d.line(P([(15.5, 15.5), (22, 11)]), fill=PAL['black'], width=W(1.5))
    # Центральная точка
    d.ellipse(R(14, 14, 17, 17), fill=PAL['red'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
