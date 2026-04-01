import math
from homework_2.src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        if radius <= 0:
            raise ValueError(f"Radius must be positive, got radius={radius}")

        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius