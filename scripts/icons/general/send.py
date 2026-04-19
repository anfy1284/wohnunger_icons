#!/usr/bin/env python3
"""Отправить (бумажный самолётик)"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "send"
COLLECTION = "general"

def draw(d):
    # Бумажный самолётик (верхнее крыло)
    d.polygon(P([(2, 6), (29, 15), (2, 17)]), fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W(1))
    # Нижнее крыло / складка
    d.polygon(P([(2, 17), (29, 15), (13, 27)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W(1))

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
