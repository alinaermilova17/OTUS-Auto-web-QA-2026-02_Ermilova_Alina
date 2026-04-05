import pytest

from homework_3.src.rectangle import (Rectangle)
from homework_3.src.circle import Circle
from homework_3.src.square import Square
from homework_3.src.triangle import Triangle


@pytest.fixture(scope='class')
def figure_class():
    print('\nСоздание фигур перед тестами класса')
    figures = {
        'circle': Circle(5),
        'rectangle': Rectangle(4, 6),
        'square': Square(4),
        'triangle': Triangle(3, 4, 5)
    }
    yield figures
    print('\nУдаление созданных фигур')

@pytest.fixture
def create_circle():
    return Circle(7)

@pytest.fixture
def create_rectangle():
    return Rectangle(8, 10)

@pytest.fixture
def create_square():
    return Square(11)

@pytest.fixture
def create_triangle():
    return Triangle(7, 8, 9)


@pytest.fixture
def multiple_area(figure_class):
    circle = figure_class['circle']
    rectangle = figure_class['rectangle']
    triangle = figure_class['triangle']

    area1 = circle.area
    area2 = rectangle.area
    area3 = triangle.area

    return area1 + area2 + area3

@pytest.fixture
def delete_circle():
    return None