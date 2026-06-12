import math
from typing import override

class Shape:
    def calculate_area(self):
        print("Calculating area of a shape")
        return 0.0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @override
    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    @override
    def calculate_area(self):
        area = self.side ** 2
        return area

myShapes = [Circle(5), Square(4)]

for shape in myShapes:
    print(f"Area: {shape.calculate_area()}")