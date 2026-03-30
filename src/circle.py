import math
from src.figure import Figure



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

    def print_results(self):
        print(f'radius: {self.radius}')
        print(f'circle area: {self.area}')
        print(f'circle perimeter: {self.perimeter}')
        print()


circle = Circle(7)
circle.print_results()

