#!/usr/bin/env python3
"""Обновить (круговая стрелка)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "refresh"
COLLECTION = "general"

def draw(d):
    # Круговая стрелка (обновить, жирная)
    d.arc(R(4, 4, 27, 27), start=45, end=315, fill=PAL['green'], width=W(3.5))
    # Наконечник стрелки (в районе 45°, побольше)
    d.polygon(P([(20, 2), (28, 10), (17, 10)]), fill=PAL['green'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
