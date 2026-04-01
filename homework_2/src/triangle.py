import math

from homework_2.src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(
                f'side_a and side_b must be positive now side_a = {side_a} and side_b = {side_b} and side_c = {side_c}')

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        p = self.perimeter / 2

        # Формула Герона
        area = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return area

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c