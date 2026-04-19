#!/usr/bin/env python3
"""Отмена (красный X в круге)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "cancel"
COLLECTION = "general"

def draw(d):
    # Красный круг с крестом
    d.ellipse(R(3, 3, 28, 28), fill=PAL['red'], outline=PAL['red_dk'], width=W(1.5))
    d.line(P([(10, 10), (21, 21)]), fill=PAL['white'], width=W(3))
    d.line(P([(21, 10), (10, 21)]), fill=PAL['white'], width=W(3))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
