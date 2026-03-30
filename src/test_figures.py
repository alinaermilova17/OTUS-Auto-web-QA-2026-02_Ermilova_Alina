# examples/example.py или просто временный файл в корне
from src.square import Square
from src.triangle import Triangle

# Теперь здесь можно писать примеры использования
square = Square(10)
triangle = Triangle(5, 8, 9)

print(f"Квадрат со стороной 10:")
print(f"Площадь: {square.area}")  # 100
print(f"Периметр: {square.perimeter}")  # 40
print()
print(f"Треугольник со сторонами 5, 8, 9:")
print(f"Площадь: {triangle.area:.2f}")  # должно быть около 19.9
print(f"Периметр: {triangle.perimeter}")  # 22
print()
print(square.add_area(triangle))  # ~119.9