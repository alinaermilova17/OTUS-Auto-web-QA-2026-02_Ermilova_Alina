
def test_rectangle(create_rectangle):
    r=create_rectangle
    assert r.area == 80, f'Area of rectangle with sides 8 and 10 must be 80, actual is {r.area}'

def test_square(create_square):
    s=create_square
    assert s.area == 121,f'Area of square with sides 11 and 11 must be 121, actual is {s.area}'


def test_multiple_area_minus_square(create_square,multiple_area, create_rectangle):
    s=create_square
    m=multiple_area
    r=create_rectangle
    assert m  < s.area + r.area,f'Sum area of square and rectangle is bigger than multiple area'
