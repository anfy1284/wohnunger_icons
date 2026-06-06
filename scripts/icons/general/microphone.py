#!/usr/bin/env python3
"""Микрофон (голосовой ввод)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "microphone"
COLLECTION = "general"

def draw(d):
    # Кронштейн-«люлька»: дуга, открытая вверх, обнимает низ капсулы
    d.arc(R(7, 10, 24, 22), start=20, end=160, fill=PAL['blue_dk'], width=W(2.5))
    # Ножка-стойка
    d.rectangle(R(14.5, 21, 16.5, 25.5), fill=PAL['blue_dk'])
    # Основание
    d.rounded_rectangle(R(11, 25, 20, 27), radius=W(0.5), fill=PAL['blue_dk'])
    # Капсула микрофона (рисуется последней — поверх кронштейна)
    d.rounded_rectangle(R(11, 3, 20, 17), radius=W(4.5),
                        fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
