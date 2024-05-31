"""
The Open/Closed Principle (OCP) is one of the five SOLID principles of object-oriented design. It states that a class
should be open for extension but closed for modification. This means that you should be able to add new functionality
to a class without changing its existing code. This principle aims to make the system more robust and maintainable by
reducing the risk of introducing bugs when the system is extended.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


shapes = [
    Rectangle(10, 20),
    Circle(15),
    Triangle(10, 5),
    Square(7)
]

for shape in shapes:
    print(f'The area of the {type(shape).__name__} is {shape.area()}')
