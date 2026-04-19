#!/usr/bin/env python3
"""В конец ►►|"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "last"
COLLECTION = "general"

def draw(d):
    # ►►| — в конец
    d.polygon(P([(4, 8), (12, 15.5), (4, 23)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))
    d.polygon(P([(13, 8), (21, 15.5), (13, 23)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))
    d.rectangle(R(24, 8, 27, 23), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
