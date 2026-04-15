import math

import pytest
from homework_3.src.triangle import Triangle

@pytest.mark.parametrize('a, b, c', [
    (0, 0, 0),
    (-1, -1, -1),
    ('ddd', 'fff', 'nnn'),
    (1, 1, 3),
    (0.5, 0.5, 2),
])

def test_area_triangle(a, b, c):
    with pytest.raises(ValueError):
        triangle = Triangle(a, b, c)
        p=(a+b+c)/2
        assert triangle.area > math.sqrt(p*(p-a)*(p-b)*(p-c))




