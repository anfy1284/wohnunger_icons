#!/usr/bin/env python3
"""Письмо (конверт)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "email"
COLLECTION = "general"

def draw(d):
    # Конверт
    d.rounded_rectangle(R(2, 6, 29, 25), radius=1*SCALE, fill=PAL['white'], outline=PAL['outline'], width=W(1.5))
    # Клапан
    d.line(P([(2, 7), (15.5, 17)]), fill=PAL['outline'], width=W(1.5))
    d.line(P([(29, 7), (15.5, 17)]), fill=PAL['outline'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
