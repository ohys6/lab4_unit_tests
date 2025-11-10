# Лабораторная работа №4 — Написание Unit-тестов

В этом репозитории:
- `rectangle.py` — реализация функций `area(width, height)` и `perimeter(width, height)`
- `test_rectangle.py` — набор unit-тестов с использованием `unittest`
- `lab_report.md` — отчет по лабораторной работе (план тестирования, результаты и т.д.)

Запуск тестов:
```bash
python -m unittest test_rectangle.py
```
или все тесты в каталоге:
```bash
python -m unittest discover -v
```