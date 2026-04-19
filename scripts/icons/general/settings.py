#!/usr/bin/env python3
"""Настройки (шестерёнка)"""

import sys
import math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "settings"
COLLECTION = "general"

def draw(d):
    c, cd = PAL['gray'], PAL['gray_dk']
    cx, cy = 15.5, 15.5
    # 8 зубцов шестерёнки (алгоритмически, равномерно)
    teeth = 8
    r_body = 9.5
    r_outer = 13.5
    half_w = 2.5
    for i in range(teeth):
        a = math.radians(i * 45)
        dx, dy = math.cos(a), math.sin(a)
        px, py = -dy, dx
        pts = [
            (cx + r_body * dx + half_w * px, cy + r_body * dy + half_w * py),
            (cx + r_outer * dx + half_w * px, cy + r_outer * dy + half_w * py),
            (cx + r_outer * dx - half_w * px, cy + r_outer * dy - half_w * py),
            (cx + r_body * dx - half_w * px, cy + r_body * dy - half_w * py),
        ]
        d.polygon(P(pts), fill=c)
    # Основной круг
    d.ellipse(R(6, 6, 25, 25), fill=c, outline=cd, width=W(1.5))
    # Центральное отверстие
    d.ellipse(R(11, 11, 20, 20), fill=PAL['white'])

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
