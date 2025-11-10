"""
rectangle.py

Функции для вычисления площади и периметра прямоугольника.
"""
from typing import Union

Number = Union[int, float]


def area(a: Number, b: Number) -> float:
    """
    Вычисляет площадь прямоугольника: a * b.
    Входные параметры должны быть числами (int/float) и >= 0.

    :raises TypeError: если a или b не являются числами
    :raises ValueError: если a или b < 0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a и b должны быть числами (int или float)")
    if a < 0 or b < 0:
        raise ValueError("a и b должны быть >= 0")
    return float(a * b)


def perimeter(a: Number, b: Number) -> float:
    """
    Вычисляет периметр прямоугольника: 2*(a + b).
    Входные параметры должны быть числами (int/float) и >= 0.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a и b должны быть числами (int или float)")
    if a < 0 or b < 0:
        raise ValueError("a и b должны быть >= 0")
    return float(2 * (a + b))
