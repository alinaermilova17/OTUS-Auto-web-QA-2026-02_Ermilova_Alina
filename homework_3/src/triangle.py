import math

from typing import Union

class Triangle:

    def __init__(self, side_a: Union[int, float, str], side_b: Union[int, float, str], side_c: Union[int, float, str]):

        try:
            self.side_a = float(side_a)
            self.side_b = float(side_b)
            self.side_c = float(side_c)
        except (ValueError, TypeError):
            raise ValueError(f"Стороны должны быть числами. Получено: a={side_a}, b={side_b}, c={side_c}")

        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError(
                f"Стороны должны быть положительными. Получено: a={self.side_a}, b={self.side_b}, c={self.side_c}")

        if (self.side_a + self.side_b <= self.side_c or
                self.side_a + self.side_c <= self.side_b or
                self.side_b + self.side_c <= self.side_a):
            raise ValueError(
                f"Треугольник с такими сторонами не существует. Стороны: {self.side_a}, {self.side_b}, {self.side_c}")

    @property
    def area(self) -> float:
        p = (self.side_a + self.side_b + self.side_c) / 2
        area = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return area

    @property
    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c