import pytest

from homework_3.src.rectangle import Rectangle
from homework_3.src.circle import Circle
from homework_3.src.square import Square
from homework_3.src.triangle import Triangle


@pytest.fixture(params=[
    (5, 78.53981634, 31.41592654),
    (1, 3.14159265, 6.28318531),
    (0.5, 0.78539816, 3.14159265),
    (100, 31415.92654, 628.3185307)])
def circle_params(request):
    radius, expected_area, expected_perimeter = request.param
    circle = Circle(radius)
    return circle, expected_area, expected_perimeter


@pytest.fixture(params=[(4, 6, 24, 20),
                        (1, 1, 1, 4),
                        (1, 10, 10, 22),
                        (0.5, 0.5, 0.25, 2),])
def rectangle_params(request):
    side_a, side_b, expected_area, expected_perimeter = request.param
    rectangle = Rectangle(side_a, side_b)
    return rectangle, expected_area, expected_perimeter


@pytest.fixture(params=[(4, 16, 16),
                        (1, 1, 4),
                        (0.5, 0.25, 2),
                        (10, 100, 40)])
def square_params(request):
    side, expected_area, expected_perimeter = request.param
    square = Square(side)
    return square, expected_area, expected_perimeter


@pytest.fixture(params=[(3, 4, 5, 6, 12),
                        (5, 5, 6, 12, 16),
                        (5, 5, 5, 10.82531755, 15),
                        (7, 8, 9, 26.83281573, 24)])
def triangle_params(request):
    side_a, side_b, side_c, expected_area, expected_perimeter = request.param
    triangle = Triangle(side_a, side_b, side_c)
    return triangle, expected_area, expected_perimeter


@pytest.fixture(params=[ -1,0,-5.5, -100])
def invalid_circle_radius(request):
    return request.param


@pytest.fixture(params=[(-2, 5),
                        (2, -5),
                        (-2, -5),
                        (0, 5),
                        (2, 0),
                        (0, 0), ])
def invalid_rectangle_sides(request):
    return request.param


@pytest.fixture(params=[(-1, 2, 2),
                        (0, 2, 2),
                        (1, 1, 10),
                        (1, 10, 1),
                        (10, 1, 1) ])
def invalid_triangle_sides(request):
    return request.param


@pytest.fixture
def figures_for_addition():
    return {
        'circle': Circle(5),
        'rectangle': Rectangle(4, 6),
        'square': Square(4),
        'triangle': Triangle(3, 4, 5)
    }