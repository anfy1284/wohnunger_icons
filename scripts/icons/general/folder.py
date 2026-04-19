#!/usr/bin/env python3
"""Папка (жёлтая)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "folder"
COLLECTION = "general"

def draw(d):
    # Таб папки
    d.rounded_rectangle(R(3, 6, 14, 11), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W(1))
    # Основной корпус
    d.rounded_rectangle(R(3, 10, 28, 27), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W(1.5))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
