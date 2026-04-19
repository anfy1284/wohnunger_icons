#!/usr/bin/env python3
"""Открытая папка"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "folder_open"
COLLECTION = "general"

def draw(d):
    # Табличка папки сверху
    d.rectangle(R(3, 6, 13, 11), fill=PAL['yellow_dk'])
    # Задняя стенка
    d.rectangle(R(3, 10, 28, 27), fill=PAL['yellow_dk'])
    # Передняя откидная панель (симметричная трапеция)
    d.polygon(P([(2, 27), (5, 14), (26, 14), (29, 27)]), fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
