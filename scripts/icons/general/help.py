#!/usr/bin/env python3
"""Помощь (вопросительный знак)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "help"
COLLECTION = "general"

def draw(d):
    # Синий круг с ?
    d.ellipse(R(4, 4, 27, 27), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1.5))
    text_centered(d, "?", 16, PAL['white'], R(4, 4, 27, 29))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
