# wohnunger_icons — Генератор иконок для MySpace

Программная генерация иконок через Pillow (стиль 1С:8.2).

## Структура

```
config/
  deploy.json              ← пути деплоя в приложения
scripts/
  lib/icon_base.py         ← общая библиотека (палитра, суперсемплинг 4x)
  icons/general/*.py       ← 38 скриптов системных иконок (по одному на иконку)
  icons/booking/*.py       ← 3 скрипта прикладных иконок
  generate_all.py          ← генерация всех иконок
  generate_preview.py      ← превью-лист с подписями
  deploy.py                ← деплой в приложения проекта
  create_icon_files.py     ← одноразовый bootstrap (уже выполнен)
output/
  16x16/{collection}/      ← финальные иконки 16×16
  32x32/{collection}/      ← финальные иконки 32×32
  preview_*.png            ← превью-листы
ICONS_CATALOG.txt          ← каталог всех иконок с описаниями
```

## Установка

```bash
python -m venv venv
venv\Scripts\activate
pip install Pillow
```

## Использование

```bash
# Сгенерировать все иконки
python scripts/generate_all.py

# Только одну коллекцию
python scripts/generate_all.py --collection general

# Превью
python scripts/generate_preview.py

# Деплой в приложения проекта
python scripts/deploy.py
```

## Как добавить новую иконку

1. Создай `scripts/icons/<коллекция>/<id>.py` по образцу существующих
2. `python scripts/generate_all.py`
3. Обнови `ICONS_CATALOG.txt`
4. `python scripts/deploy.py`
