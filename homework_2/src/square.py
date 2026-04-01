from homework_2.src.figure import Figure


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