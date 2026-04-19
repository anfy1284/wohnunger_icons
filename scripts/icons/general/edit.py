#!/usr/bin/env python3
"""Редактировать (карандаш)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "edit"
COLLECTION = "general"

def draw(d):
    # Толстый карандаш (~45°)
    d.polygon(P([
        (8, 29), (3, 22), (22, 3), (27, 8)
    ]), fill=PAL['yellow'], outline=PAL['outline'], width=W(1.5))
    # Ластик (верх)
    d.polygon(P([
        (22, 3), (27, 8), (29, 5), (25, 1)
    ]), fill=PAL['red_lt'], outline=PAL['outline'], width=W(1))
    # Грифель (низ)
    d.polygon(P([(3, 22), (2, 29), (8, 29)]), fill=PAL['skin'], outline=PAL['outline'], width=W(1))
    # Острие
    d.polygon(P([(2, 29), (4, 26), (6, 28)]), fill=PAL['black'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
