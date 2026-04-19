"""
Общая библиотека для программной генерации иконок в стиле 1С:8.2.
Каждый скрипт в scripts/icons/ импортирует эту базу.

Используется 4x supersampling: рисуем 128x128, сжимаем до 32x32 и 16x16.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ─── Пути ────────────────────────────────────────────────────
SCRIPTS_DIR = Path(__file__).parent.parent
PROJECT_DIR = SCRIPTS_DIR.parent
OUTPUT_DIR = PROJECT_DIR / "output"

# ─── Масштаб ─────────────────────────────────────────────────
SCALE = 4
CANVAS = 32 * SCALE  # 128px

# ═══════════════════════════════════════════════════════════════
#  Палитра — стиль 1С:8.2
# ═══════════════════════════════════════════════════════════════
PAL = {
    'blue':      (70, 105, 165),
    'blue_dk':   (45, 75, 130),
    'blue_lt':   (145, 170, 210),
    'green':     (75, 135, 95),
    'green_dk':  (50, 100, 65),
    'green_lt':  (140, 185, 155),
    'red':       (180, 65, 65),
    'red_dk':    (140, 45, 45),
    'red_lt':    (210, 145, 140),
    'yellow':    (195, 170, 75),
    'yellow_dk': (155, 135, 50),
    'yellow_lt': (220, 205, 145),
    'orange':    (200, 130, 60),
    'gray':      (140, 145, 150),
    'gray_lt':   (200, 205, 210),
    'gray_dk':   (80, 85, 90),
    'outline':   (55, 60, 65),
    'black':     (35, 38, 42),
    'white':     (255, 255, 255),
    'paper':     (248, 248, 245),
    'skin':      (230, 200, 170),
}


# ═══════════════════════════════════════════════════════════════
#  Хелперы для рисования
# ═══════════════════════════════════════════════════════════════

def R(x1, y1, x2, y2):
    """Масштабировать bounding box."""
    return [int(x1*SCALE), int(y1*SCALE), int(x2*SCALE), int(y2*SCALE)]

def P(points):
    """Масштабировать список точек [(x,y), ...]."""
    return [(int(x*SCALE), int(y*SCALE)) for x, y in points]

def W(n=1):
    """Масштабировать толщину линии."""
    return max(1, int(n * SCALE))

def new_canvas():
    """Создать холст 128x128 RGBA с прозрачным фоном."""
    img = Image.new('RGBA', (CANVAS, CANVAS), (0, 0, 0, 0))
    return img, ImageDraw.Draw(img)

def text_centered(d, text, font_size, color, bbox=None):
    """Нарисовать текст по центру области."""
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(font_size * SCALE))
    except Exception:
        return
    if bbox is None:
        bbox = [0, 0, CANVAS, CANVAS]
    tb = d.textbbox((0, 0), text, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    x = bbox[0] + (bbox[2] - bbox[0] - tw) // 2 - tb[0]
    y = bbox[1] + (bbox[3] - bbox[1] - th) // 2 - tb[1]
    d.text((x, y), text, fill=color, font=font)


# ═══════════════════════════════════════════════════════════════
#  Генерация и сохранение
# ═══════════════════════════════════════════════════════════════

def generate(icon_id, collection, draw_fn):
    """
    Сгенерировать одну иконку.
    icon_id:    имя иконки (save, add, ...)
    collection: "general" или "booking"
    draw_fn:    функция рисования draw(d)
    """
    img, d = new_canvas()
    draw_fn(d)

    for size in (32, 16):
        d_out = OUTPUT_DIR / f"{size}x{size}" / collection
        d_out.mkdir(parents=True, exist_ok=True)
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        path = d_out / f"{icon_id}.png"
        resized.save(str(path))

    print(f"  ✓ {icon_id}")
    return img
