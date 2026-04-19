#!/usr/bin/env python3
"""Принтер"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "print"
COLLECTION = "general"

def draw(d):
    # Бумага входящая сверху
    d.rectangle(R(9, 2, 22, 11), fill=PAL['paper'], outline=PAL['outline'], width=W(1))
    # Корпус принтера
    d.rounded_rectangle(R(3, 9, 28, 21), radius=1*SCALE, fill=PAL['gray_lt'], outline=PAL['outline'], width=W(1.5))
    # Бумага выходящая снизу
    d.rectangle(R(6, 19, 25, 29), fill=PAL['paper'], outline=PAL['outline'], width=W(1))
    # Строки на бумаге
    for y in (22, 25):
        d.line(P([(9, y), (22, y)]), fill=PAL['gray_lt'], width=W(0.5))
    # Кнопка
    d.ellipse(R(22, 12, 25, 15), fill=PAL['green'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
