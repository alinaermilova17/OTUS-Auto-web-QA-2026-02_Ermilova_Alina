import pytest
from homework_3.src.circle import Circle
from homework_3.src.rectangle import Rectangle
from homework_3.src.square import Square
from homework_3.src.triangle import Triangle


def test_area_circle(circle_params):
    circle, expected_area, _ = circle_params
    assert circle.area == pytest.approx(expected_area)

def test_perimeter_circle(circle_params):
    circle, _, expected_perimeter = circle_params
    assert circle.perimeter == pytest.approx(expected_perimeter)


def test_invalid_radius_circle( invalid_circle_radius):
    with pytest.raises(ValueError):
        Circle(invalid_circle_radius)


def test_area_rectangle(rectangle_params):
    rectangle, expected_area, _ = rectangle_params
    assert rectangle.area == expected_area


def test_perimeter_rectangle(rectangle_params):
    rectangle, _, expected_perimeter = rectangle_params
    assert rectangle.perimeter == expected_perimeter


def test_invalid_sides_rectangle(invalid_rectangle_sides):
    side_a, side_b = invalid_rectangle_sides
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_area_quare(square_params):
    square, expected_area, _ = square_params
    assert square.area == expected_area


def test_perimeter_quare(square_params):
    square, _, expected_perimeter = square_params
    assert square.perimeter == expected_perimeter


def test_invalid_side_square(invalid_circle_radius):
    with pytest.raises(ValueError):
        Square(-1)
    with pytest.raises(ValueError):
        Square(0)


def test_area_triangle(triangle_params):
    triangle, expected_area, _ = triangle_params
    assert triangle.area == pytest.approx(expected_area)


def test_perimeter_triangle(triangle_params):
    triangle, _, expected_perimeter = triangle_params
    assert triangle.perimeter == expected_perimeter


def test_invalid_triangle_triangle(invalid_triangle_sides):
    side_a, side_b, side_c = invalid_triangle_sides
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_sum_of_circle_and_triangle(figures_for_addition):
    circle = figures_for_addition['circle']
    triangle = figures_for_addition['triangle']

    total = circle.area + triangle.area
    expected = 78.53981634 + 6

    assert total == pytest.approx(expected)