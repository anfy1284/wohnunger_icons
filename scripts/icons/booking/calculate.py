#!/usr/bin/env python3
"""Рассчитать стоимость (калькулятор)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "calculate"
COLLECTION = "booking"

def draw(d):
    # Корпус калькулятора
    d.rounded_rectangle(R(5, 2, 26, 29), radius=2*SCALE, fill=PAL['gray_lt'], outline=PAL['outline'], width=W(1.5))
    # Дисплей
    d.rectangle(R(8, 5, 23, 12), fill=PAL['green_lt'], outline=PAL['gray'], width=W(1))
    # Кнопки (3×3)
    for row in range(3):
        for col in range(3):
            x = 9 + col * 5
            y = 15 + row * 5
            c = PAL['gray'] if col < 2 else PAL['orange']
            d.rectangle(R(x, y, x+3, y+3), fill=c)

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
