import math
from src.figure import Figure
from src.triangle import Triangle


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


circle = Circle(7)
triangle = Triangle(3,8,10)
circle.add_area(triangle)

