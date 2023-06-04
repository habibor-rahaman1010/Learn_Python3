# polymorphism implement in python programming

class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        return (self.length * self.width)
    
class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return (self.length * self.width)
    
class Circle(Shape):
    def __init__(self, name, redius) -> None:
        self.radius = redius
        super().__init__(name,)

    def area(self):
        return (3.1416 * self.radius * 2)
    
class Triangle(Shape):
    def __init__(self, name, base, height) -> None:
        self.base = base
        self.height = height
        super().__init__(name)

    def area(self):
        return ((1/2) * self.base * self.height)
    

rectangle = Rectangle('Rectangle', 6, 12)
print(f'Area of rectangle: {rectangle.area()}')

circle = Circle('Circle', 6)
print(f'Area of circle: {circle.area()}')

triangle = Triangle('Triangle', 4, 7)
print(f'Area of triangle: {triangle.area()}')

