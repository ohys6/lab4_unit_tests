# Отчет по лабораторной работе №4 — Написание Unit тестов

## 1. Цели и задачи тестирования
- Цель: показать методику написания и запуска unit-тестов для простого модуля.
- Задачи:
  - Реализовать функции вычисления площади и периметра прямоугольника.
  - Написать покрывающие unit-тесты, отражающие обычные и пограничные случаи.
  - Продемонстрировать отчёт и инструкции по запуску.

## 2. Описание тестируемого продукта
Модуль `rectangle.py` с функциями:
- `area(a, b)` — возвращает площадь (float)
- `perimeter(a, b)` — возвращает периметр (float)

Требования:
- Параметры должны быть числами (int/float).
- Параметры должны быть >= 0.

## 3. Область тестирования
Покрытие:
- Положительные случаи (целые, дробные).
- Нулевые значения.
- Большие числа.
- Негативные числа (ожидается ValueError).
- Неподходящие типы (ожидается TypeError).

## 4. Стратегия тестирования
- Используется функциональное тестирование (unit-тесты).
- Автоматизация: `unittest` (стандартный модуль Python).
- Для каждого типа поведения — отдельный тестовый метод.
- Критерии прохождения: все тесты должны завершиться успешно.

## 5. Критерии приёмки
- Все тесты в `test_rectangle.py` выполнены успешно (0 ошибок, 0 неудач).
- Код корректно обрабатывает недопустимые входные значения и типы.

## 6. Ожидаемые результаты
- Детализированный отчёт о тестировании (этот файл).
- Логи тестов — вывод `unittest` (ниже приведён фактический результат выполнения).

---

## План тестирования
1. Подготовка тестовых данных:
   - (0,0), (0,10), (3,5), (2.5,4.2), (10**6, 2)
   - Негативные: (-1,5), (5,-1)
   - Неверные типы: "a", None, [1,2]
2. Ожидаемые результаты:
   - Соответствующие числовые значения или возбуждение исключений.
3. Выполнение тестов: запустить `python -m unittest discover -v`
4. Сохранение результатов в протоколе тестирования.

---

## История версий 
- initial commit: добавлены `rectangle.py`, `test_rectangle.py`, `lab_report.md`, `README.md`

---

## Фактический результат выполнения тестов 
```

test_area_floats (test_rectangle.RectangleTestCase.test_area_floats) ... ok
test_area_invalid_type_raises (test_rectangle.RectangleTestCase.test_area_invalid_type_raises) ... ok
test_area_large_numbers (test_rectangle.RectangleTestCase.test_area_large_numbers) ... ok
test_area_negative_raises (test_rectangle.RectangleTestCase.test_area_negative_raises) ... ok
test_area_positive_integers (test_rectangle.RectangleTestCase.test_area_positive_integers) ... ok
test_area_zero (test_rectangle.RectangleTestCase.test_area_zero) ... ok
test_perimeter_floats (test_rectangle.RectangleTestCase.test_perimeter_floats) ... ok
test_perimeter_invalid_type_raises (test_rectangle.RectangleTestCase.test_perimeter_invalid_type_raises) ... ok
test_perimeter_negative_raises (test_rectangle.RectangleTestCase.test_perimeter_negative_raises) ... ok
test_perimeter_positive (test_rectangle.RectangleTestCase.test_perimeter_positive) ... ok
test_perimeter_zero (test_rectangle.RectangleTestCase.test_perimeter_zero) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK

```
