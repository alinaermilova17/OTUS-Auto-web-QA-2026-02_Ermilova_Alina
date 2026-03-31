from src.figure import Figure
from src.rectangle import Rectangle


class Square(Figure):
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError(f'side_a must be positive now side_a = {side_a} ')

        self.side_a = side_a


    @property
    def area(self):
        return self.side_a **2


    @property
    def perimeter(self):
        return  self.side_a*4



square = Square(10)
rectangle = Rectangle(5,9)
square.add_area(rectangle)

