#!/usr/bin/env python3
"""В начало |◄◄"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "first"
COLLECTION = "general"

def draw(d):
    # |◄◄ — в начало
    d.rectangle(R(4, 8, 7, 23), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))
    d.polygon(P([(18, 8), (10, 15.5), (18, 23)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))
    d.polygon(P([(27, 8), (19, 15.5), (27, 23)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
