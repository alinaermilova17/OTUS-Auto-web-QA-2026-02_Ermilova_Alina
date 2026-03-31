from src.figure import Figure
from src.triangle import Triangle


class Rectangle(Figure):
    def __init__(self, side_a:int, side_b: int):
        if side_a <= 0 or side_b<= 0:
            raise ValueError(f'side_a and side_b must be positive now side_a = {side_a} and side_b = {side_b}')

        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b


    @property
    def perimeter(self):
        return (self.side_a + self.side_b)*2


rectangle = Rectangle(5, 8)
triangle = Triangle(5, 8,10)
rectangle.add_area(triangle)






