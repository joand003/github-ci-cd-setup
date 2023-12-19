import pytest
from my_project import Rectangle, Triangle, Circle
import math


class TestRectangle:
    def test_rectangle_area(self):
        rectangle = Rectangle(2, 4)
        assert rectangle.area() == 8

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(2, 4)
        assert rectangle.perimeter() == 12

    def test_rectangle_repr(self):
        rectangle = Rectangle(2, 4)
        assert repr(rectangle) == "<Rectangle 2x4>"

    def test_rectangle_invalid_args(self):
        with pytest.raises(ValueError):
            Rectangle(2, -4)

    def test_square_repr(self):
        square = Rectangle(2, 2)
        assert repr(square) == "<Rectangle 2x2>"


class TestTriangle:
    def test_triangle_area(self):
        triangle = Triangle(2, 4, 6, 8, 10)
        assert triangle.area() == 4

    def test_triangle_perimeter(self):
        triangle = Triangle(2, 4, 6, 8, 10)
        assert triangle.perimeter() == 24

    def test_triangle_type(self):
        triangle = Triangle(2, 4, 6, 8, 10)
        assert triangle.triangle_type() == "Scalene"

    def test_triangle_invalid_args(self):
        with pytest.raises(ValueError):
            Triangle(2, 4, 6, 8, -10)

    def test_triangle_repr(self):
        triangle = Triangle(2, 4, 6, 8, 10)
        assert repr(triangle) == "<Triangle 2x4>"

    def test_equilateral_triangle(self):
        triangle = Triangle(2, 2, 2, 2, 2)
        assert triangle.triangle_type() == "Equilateral"

    def test_isosceles_triangle(self):
        triangle = Triangle(2, 4, 2, 4, 4)
        assert triangle.triangle_type() == "Isosceles"


class TestCircle:
    def test_circle_area(self):
        circle = Circle(2)
        assert circle.area() == 4 * math.pi

    def test_circle_perimeter(self):
        circle = Circle(2)
        assert circle.perimeter() == 4 * math.pi

    def test_circle_repr(self):
        circle = Circle(2)
        assert repr(circle) == "<Circle with radius: 2>"

    def test_circle_invalid_args(self):
        with pytest.raises(ValueError):
            Circle(-2)
