#!/usr/bin/env python3
"""Открыть (папка со стрелкой)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "open"
COLLECTION = "general"

def draw(d):
    # Папка (нижняя часть)
    d.rounded_rectangle(R(1, 12, 10, 16), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W(1))
    d.rounded_rectangle(R(1, 15, 20, 27), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W(1.5))
    # Горизонтальная стрелка вправо (открыть)
    d.line(P([(15, 7), (27, 7)]), fill=PAL['blue'], width=W(2.5))
    d.polygon(P([(24, 3), (29, 7), (24, 11)]), fill=PAL['blue'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
