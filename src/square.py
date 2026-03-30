from src.figure import add_area, Figure
from src.rectangle import rectangle


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

    def print_results(self):
        print(f'square side_a = {self.side_a}')
        print(f'square area = {self.area}')
        print(f'square perimeter = {self.perimeter}')
        print(f'Сумма площадей = {add_area(square, figure=rectangle)}')
        print()


square = Square(10)
square.print_results()

