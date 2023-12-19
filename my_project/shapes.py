import math


class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        if length == width:
            super().__init__("Square", 4)
        else:
            super().__init__("Rectangle", 4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __repr__(self):
        return f"<Rectangle {self.length}x{self.width}>"


class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        if (base <= 0 or height <= 0 or side_a <= 0 or
                side_b <= 0 or side_c <= 0):
            raise ValueError("All measurements must be positive")
        super().__init__("Triangle", 3)
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def triangle_type(self):
        if self.side_a == self.side_b == self.side_c:
            return "Equilateral"
        elif (
            self.side_a == self.side_b
            or self.side_a == self.side_c
            or self.side_b == self.side_c
        ):
            return "Isosceles"
        else:
            return "Scalene"

    def __repr__(self):
        return f"<Triangle {self.base}x{self.height}>"


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        super().__init__("Circle", 0)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"<Circle with radius: {self.radius}>"
