#!/usr/bin/env python3
"""Удалить (красная корзина)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "delete"
COLLECTION = "general"

def draw(d):
    # Красный крестик (удалить)
    d.line(P([(6, 6), (25, 25)]), fill=PAL['red'], width=W(3.5))
    d.line(P([(25, 6), (6, 25)]), fill=PAL['red'], width=W(3.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
