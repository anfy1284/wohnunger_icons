#!/usr/bin/env python3
"""
Одноразовый скрипт: создаёт индивидуальные .py файлы для каждой иконки.
Запустить один раз: python scripts/create_icon_files.py
После этого каждая иконка — отдельный файл в scripts/icons/{collection}/.
"""

import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ICONS_DIR = SCRIPT_DIR / "icons"

# ═══════════════════════════════════════════════════════════════
#  Описания всех иконок: (id, docstring, draw_code)
#  collection → category → [(id, doc, code), ...]
# ═══════════════════════════════════════════════════════════════

ICONS = {
    "general": {
        "crud": [
            ("add", "Добавить (зелёный плюс)", '''
    d.rounded_rectangle(R(12,3,19,28), radius=2*SCALE, fill=PAL['green'], outline=PAL['green_dk'], width=W())
    d.rounded_rectangle(R(3,12,28,19), radius=2*SCALE, fill=PAL['green'], outline=PAL['green_dk'], width=W())
'''),
            ("edit", "Редактировать (карандаш)", '''
    d.polygon(P([(8,27),(5,24),(21,4),(26,8)]), fill=PAL['yellow'], outline=PAL['outline'], width=W())
    d.polygon(P([(5,24),(3,29),(8,27)]), fill=PAL['skin'], outline=PAL['outline'], width=W())
    d.polygon(P([(21,4),(26,8),(29,5),(24,1)]), fill=PAL['red_lt'], outline=PAL['outline'], width=W())
    d.polygon(P([(3,29),(4,27),(6,29)]), fill=PAL['black'])
'''),
            ("delete", "Удалить (красная корзина)", '''
    d.rounded_rectangle(R(5,5,26,9), radius=1*SCALE, fill=PAL['red'], outline=PAL['red_dk'], width=W())
    d.rounded_rectangle(R(12,2,19,6), radius=1*SCALE, fill=PAL['red'], outline=PAL['red_dk'], width=W())
    d.polygon(P([(7,10),(24,10),(22,29),(9,29)]), fill=PAL['red_lt'], outline=PAL['red_dk'], width=W())
    for x in (12, 15.5, 19):
        d.line(P([(x,13),(x,26)]), fill=PAL['red_dk'], width=W())
'''),
            ("save", "Сохранить (дискета)", '''
    d.rounded_rectangle(R(3,2,28,29), radius=2*SCALE, fill=PAL['blue'], outline=PAL['blue_dk'], width=W())
    d.rectangle(R(8,4,23,13), fill=PAL['white'], outline=PAL['gray'], width=W())
    for y in range(6, 13, 2):
        d.line(P([(10,y),(21,y)]), fill=PAL['gray_lt'], width=max(1, SCALE//2))
    d.rectangle(R(10,17,21,27), fill=PAL['gray_lt'], outline=PAL['gray'], width=W())
    d.rectangle(R(12,19,16,25), fill=PAL['gray_dk'])
'''),
            ("cancel", "Отмена (красный X в круге)", '''
    d.ellipse(R(3,3,28,28), fill=PAL['red'], outline=PAL['red_dk'], width=W())
    d.line(P([(10,10),(21,21)]), fill=PAL['white'], width=W(3))
    d.line(P([(21,10),(10,21)]), fill=PAL['white'], width=W(3))
'''),
            ("open", "Открыть (папка со стрелкой)", '''
    d.rounded_rectangle(R(3,8,14,13), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W())
    d.rounded_rectangle(R(3,12,28,27), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W())
    d.polygon(P([(14,14),(21,18),(14,22)]), fill=PAL['green'], outline=PAL['green_dk'], width=W())
'''),
            ("copy", "Копировать (два документа)", '''
    d.rounded_rectangle(R(9,8,28,29), radius=1*SCALE, fill=PAL['paper'], outline=PAL['outline'], width=W())
    for y in (12, 16, 20, 24):
        d.line(P([(12,y),(25,y)]), fill=PAL['gray_lt'], width=max(1, SCALE//2))
    d.rounded_rectangle(R(3,2,22,23), radius=1*SCALE, fill=PAL['paper'], outline=PAL['outline'], width=W())
    for y in (6, 10, 14, 18):
        d.line(P([(6,y),(19,y)]), fill=PAL['gray_lt'], width=max(1, SCALE//2))
'''),
            ("paste", "Вставить (буфер обмена)", '''
    d.rounded_rectangle(R(5,5,27,29), radius=2*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W())
    d.rounded_rectangle(R(11,2,20,7), radius=1*SCALE, fill=PAL['gray'], outline=PAL['gray_dk'], width=W())
    d.rectangle(R(8,10,24,27), fill=PAL['white'], outline=PAL['gray'], width=W())
    for y in (13, 16, 19, 22):
        d.line(P([(10,y),(22,y)]), fill=PAL['gray_lt'], width=max(1, SCALE//2))
'''),
            ("cut", "Вырезать (ножницы)", '''
    d.ellipse(R(3,19,13,29), outline=PAL['red'], width=W(2))
    d.ellipse(R(18,19,28,29), outline=PAL['red'], width=W(2))
    d.line(P([(8,21),(20,3)]), fill=PAL['gray_dk'], width=W(2))
    d.line(P([(23,21),(11,3)]), fill=PAL['gray_dk'], width=W(2))
'''),
            ("undo", "Отменить (стрелка влево)", '''
    d.arc(R(6,6,27,24), start=180, end=360, fill=PAL['blue'], width=W(3))
    d.line(P([(27,15),(27,24)]), fill=PAL['blue'], width=W(3))
    d.polygon(P([(3,15),(12,8),(12,22)]), fill=PAL['blue'])
'''),
            ("redo", "Повторить (стрелка вправо)", '''
    d.arc(R(4,6,25,24), start=180, end=360, fill=PAL['blue'], width=W(3))
    d.line(P([(4,15),(4,24)]), fill=PAL['blue'], width=W(3))
    d.polygon(P([(28,15),(19,8),(19,22)]), fill=PAL['blue'])
'''),
            ("select", "Выбрать (зелёная галочка)", '''
    d.line(P([(5,17),(12,25),(27,7)]), fill=PAL['green'], width=W(4))
'''),
            ("select_all", "Выбрать все (чекбокс с галочкой)", '''
    d.rounded_rectangle(R(3,3,28,28), radius=2*SCALE, fill=PAL['white'], outline=PAL['blue'], width=W(2))
    d.line(P([(8,16),(13,22),(24,8)]), fill=PAL['green'], width=W(3))
'''),
        ],

        "navigation": [
            ("first", "В начало |◄◄", '''
    d.rectangle(R(4,7,7,24), fill=PAL['blue'], outline=PAL['blue_dk'])
    d.polygon(P([(19,7),(10,15.5),(19,24)]), fill=PAL['blue'], outline=PAL['blue_dk'])
    d.polygon(P([(27,7),(18,15.5),(27,24)]), fill=PAL['blue'], outline=PAL['blue_dk'])
'''),
            ("prev", "Назад ◄", '''
    d.polygon(P([(22,4),(8,15.5),(22,27)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W())
'''),
            ("next", "Вперёд ►", '''
    d.polygon(P([(9,4),(23,15.5),(9,27)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W())
'''),
            ("last", "В конец ►►|", '''
    d.rectangle(R(24,7,27,24), fill=PAL['blue'], outline=PAL['blue_dk'])
    d.polygon(P([(4,7),(13,15.5),(4,24)]), fill=PAL['blue'], outline=PAL['blue_dk'])
    d.polygon(P([(12,7),(21,15.5),(12,24)]), fill=PAL['blue'], outline=PAL['blue_dk'])
'''),
            ("up", "Вверх ▲", '''
    d.polygon(P([(4,23),(15.5,6),(27,23)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W())
'''),
            ("down", "Вниз ▼", '''
    d.polygon(P([(4,8),(15.5,25),(27,8)]), fill=PAL['blue'], outline=PAL['blue_dk'], width=W())
'''),
        ],

        "data": [
            ("refresh", "Обновить (круговая стрелка)", '''
    d.arc(R(4,4,27,27), start=30, end=330, fill=PAL['green'], width=W(3))
    d.polygon(P([(23,4),(28,11),(19,9)]), fill=PAL['green'])
'''),
            ("search", "Поиск (лупа)", '''
    d.ellipse(R(3,3,20,20), outline=PAL['blue'], width=W(3))
    d.line(P([(18,18),(28,28)]), fill=PAL['blue_dk'], width=W(3))
'''),
            ("filter", "Фильтр (воронка)", '''
    d.polygon(P([(3,4),(28,4),(18,17)]), fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W())
    d.rectangle(R(13,17,18,28), fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W())
'''),
            ("sort_asc", "Сортировка по возрастанию ↑", '''
    d.line(P([(15.5,4),(15.5,27)]), fill=PAL['blue'], width=W(2))
    d.polygon(P([(9,12),(15.5,4),(22,12)]), fill=PAL['blue'])
'''),
            ("sort_desc", "Сортировка по убыванию ↓", '''
    d.line(P([(15.5,4),(15.5,27)]), fill=PAL['blue'], width=W(2))
    d.polygon(P([(9,19),(15.5,27),(22,19)]), fill=PAL['blue'])
'''),
        ],

        "files": [
            ("folder", "Папка (жёлтая)", '''
    d.rounded_rectangle(R(3,6,14,11), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W())
    d.rounded_rectangle(R(3,10,28,27), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W())
'''),
            ("folder_open", "Открытая папка", '''
    d.rounded_rectangle(R(3,6,14,11), radius=1*SCALE, fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W())
    d.polygon(P([(1,14),(7,10),(28,10),(26,27),(3,27)]), fill=PAL['yellow'], outline=PAL['yellow_dk'], width=W())
'''),
            ("document", "Документ", '''
    d.polygon(P([(6,2),(22,2),(28,8),(28,29),(6,29)]), fill=PAL['paper'], outline=PAL['outline'], width=W())
    d.polygon(P([(22,2),(22,8),(28,8)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W())
    for y in (12, 15, 18, 21, 24):
        d.line(P([(9,y),(25,y)]), fill=PAL['gray_lt'], width=max(1, SCALE//2))
'''),
            ("document_new", "Новый документ", '''
    d.polygon(P([(6,2),(22,2),(28,8),(28,29),(6,29)]), fill=PAL['paper'], outline=PAL['outline'], width=W())
    d.polygon(P([(22,2),(22,8),(28,8)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W())
    d.ellipse(R(1,19,13,31), fill=PAL['green'], outline=PAL['green_dk'], width=W())
    d.line(P([(4,25),(10,25)]), fill=PAL['white'], width=W(2))
    d.line(P([(7,22),(7,28)]), fill=PAL['white'], width=W(2))
'''),
        ],

        "print": [
            ("print", "Принтер", '''
    d.rectangle(R(8,2,23,10), fill=PAL['paper'], outline=PAL['outline'], width=W())
    d.rounded_rectangle(R(3,10,28,22), radius=1*SCALE, fill=PAL['gray_lt'], outline=PAL['outline'], width=W())
    d.rectangle(R(7,22,24,28), fill=PAL['paper'], outline=PAL['outline'], width=W())
    d.ellipse(R(5,13,8,16), fill=PAL['green'])
'''),
            ("preview", "Предпросмотр печати", '''
    d.rectangle(R(3,2,24,26), fill=PAL['paper'], outline=PAL['outline'], width=W())
    for y in (7, 10, 13, 16, 19):
        d.line(P([(6,y),(21,y)]), fill=PAL['gray_lt'], width=max(1, SCALE//2))
    d.ellipse(R(16,16,27,27), fill=PAL['white'], outline=PAL['blue'], width=W(2))
    d.line(P([(26,26),(30,30)]), fill=PAL['blue_dk'], width=W(2))
'''),
        ],

        "system": [
            ("settings", "Настройки (шестерёнка)", '''
    c, cd = PAL['gray'], PAL['gray_dk']
    for t in [R(13,2,18,9), R(13,22,18,29), R(2,13,9,18), R(22,13,29,18)]:
        d.rectangle(t, fill=c)
    for pts in [
        [(7,4),(11,4),(9,10),(5,8)],
        [(20,4),(24,4),(26,8),(22,10)],
        [(5,23),(9,21),(11,27),(7,27)],
        [(22,21),(26,23),(24,27),(20,27)],
    ]:
        d.polygon(P(pts), fill=c)
    d.ellipse(R(6,6,25,25), fill=c, outline=cd, width=W())
    d.ellipse(R(11,11,20,20), fill=PAL['white'])
'''),
            ("help", "Помощь (вопросительный знак)", '''
    d.ellipse(R(4,4,27,27), fill=PAL['blue'], outline=PAL['blue_dk'], width=W())
    text_centered(d, "?", 18, PAL['white'], R(4,2,27,27))
'''),
            ("send", "Отправить (бумажный самолётик)", '''
    d.polygon(P([(3,5),(28,15.5),(3,26)]), fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W())
    d.line(P([(3,15.5),(28,15.5)]), fill=PAL['blue_dk'], width=W())
    d.line(P([(13,15.5),(10,24)]), fill=PAL['blue_dk'], width=W())
'''),
        ],

        "time": [
            ("clock", "Часы", '''
    d.ellipse(R(3,3,28,28), fill=PAL['white'], outline=PAL['outline'], width=W(2))
    for pts in [((15.5,5),(15.5,7)), ((15.5,24),(15.5,26)), ((5,15.5),(7,15.5)), ((24,15.5),(26,15.5))]:
        d.line(P(pts), fill=PAL['outline'], width=W())
    d.line(P([(15.5,15.5),(15.5,7)]), fill=PAL['black'], width=W(2))
    d.line(P([(15.5,15.5),(22,12)]), fill=PAL['black'], width=W())
    d.ellipse(R(14,14,17,17), fill=PAL['red'])
'''),
            ("calendar", "Календарь", '''
    d.rounded_rectangle(R(3,5,28,29), radius=1*SCALE, fill=PAL['white'], outline=PAL['outline'], width=W())
    d.rounded_rectangle(R(3,5,28,12), radius=1*SCALE, fill=PAL['red'], outline=PAL['red_dk'], width=W())
    for x in (9, 15.5, 22):
        d.line(P([(x,3),(x,8)]), fill=PAL['gray_dk'], width=W(2))
    for row in range(3):
        for col in range(4):
            x = 6 + col * 5.5
            y = 14 + row * 5
            d.rectangle(R(x, y, x+3, y+3), fill=PAL['gray_lt'])
    d.rectangle(R(11.5,19,14.5,22), fill=PAL['blue'])
'''),
        ],

        "other": [
            ("email", "Письмо (конверт)", '''
    d.rounded_rectangle(R(2,6,29,25), radius=1*SCALE, fill=PAL['white'], outline=PAL['outline'], width=W())
    d.line(P([(2,6),(15.5,17)]), fill=PAL['outline'], width=W())
    d.line(P([(29,6),(15.5,17)]), fill=PAL['outline'], width=W())
'''),
            ("money", "Деньги (знак доллара)", '''
    d.ellipse(R(4,4,27,27), fill=PAL['green'], outline=PAL['green_dk'], width=W())
    text_centered(d, "$", 18, PAL['white'], R(4,2,27,27))
'''),
            ("user", "Пользователь", '''
    d.ellipse(R(11,2,20,11), fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W())
    d.pieslice(R(5,15,26,38), start=180, end=360, fill=PAL['blue_lt'], outline=PAL['blue_dk'], width=W())
'''),
        ],
    },

    "booking": {
        "business": [
            ("booking_status", "Статус брони (документ с галочкой)", '''
    d.polygon(P([(6,2),(22,2),(28,8),(28,29),(6,29)]), fill=PAL['paper'], outline=PAL['outline'], width=W())
    d.polygon(P([(22,2),(22,8),(28,8)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W())
    d.ellipse(R(1,17,15,31), fill=PAL['blue'], outline=PAL['blue_dk'], width=W())
    d.line(P([(4,24),(7,27),(13,21)]), fill=PAL['white'], width=W(2))
'''),
            ("calculate", "Рассчитать стоимость (калькулятор)", '''
    d.rounded_rectangle(R(5,2,26,29), radius=2*SCALE, fill=PAL['gray_lt'], outline=PAL['outline'], width=W())
    d.rectangle(R(8,5,23,12), fill=PAL['green_lt'], outline=PAL['gray'], width=W())
    for row in range(3):
        for col in range(3):
            x = 9 + col * 5
            y = 15 + row * 5
            c = PAL['gray'] if col < 2 else PAL['orange']
            d.rectangle(R(x, y, x+3, y+3), fill=c)
'''),
            ("invoice_print", "Печать счёта (документ с $)", '''
    d.polygon(P([(6,2),(22,2),(28,8),(28,29),(6,29)]), fill=PAL['paper'], outline=PAL['outline'], width=W())
    d.polygon(P([(22,2),(22,8),(28,8)]), fill=PAL['gray_lt'], outline=PAL['outline'], width=W())
    for y in (12, 15, 18):
        d.line(P([(9,y),(25,y)]), fill=PAL['gray_lt'], width=max(1, SCALE//2))
    d.ellipse(R(1,17,15,31), fill=PAL['green'], outline=PAL['green_dk'], width=W())
    text_centered(d, "$", 9, PAL['white'], R(1,16,15,31))
'''),
        ],
    },
}


# ═══════════════════════════════════════════════════════════════
#  Шаблон файла иконки
# ═══════════════════════════════════════════════════════════════

TEMPLATE = '''#!/usr/bin/env python3
"""{doc}"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.icon_base import *

ICON_ID = "{icon_id}"
COLLECTION = "{collection}"

def draw(d):
{code}

if __name__ == "__main__":
    generate(ICON_ID, COLLECTION, draw)
'''


def main():
    total = 0

    for collection, categories in ICONS.items():
        for category, icons in categories.items():
            target_dir = ICONS_DIR / collection
            target_dir.mkdir(parents=True, exist_ok=True)

            for icon_id, doc, code in icons:
                filepath = target_dir / f"{icon_id}.py"

                # Не перезаписываем если файл уже есть (пользователь мог отредактировать)
                if filepath.exists():
                    print(f"  ⊘ {collection}/{icon_id}.py уже существует, пропускаю")
                    continue

                content = TEMPLATE.format(
                    doc=doc,
                    icon_id=icon_id,
                    collection=collection,
                    code=code.rstrip(),
                )

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

                total += 1
                print(f"  ✓ {collection}/{icon_id}.py")

    print(f"\n[DONE] Создано {total} файлов иконок.")


if __name__ == "__main__":
    main()
