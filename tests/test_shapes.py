import pytest
import my_project.shapes as shape
import math


class TestRectangle:
    def setup_method(self):
        self.rectangle = shape.Rectangle(2, 4)

    def teaerdown_method(self):
        del self.rectangle

    def test_rectangle_area(self):
        assert self.rectangle.area() == 8

    def test_rectangle_perimeter(self):
        assert self.rectangle.perimeter() == 12

    def test_rectangle_repr(self):
        assert repr(self.rectangle) == "<Rectangle 2x4>"

    def test_rectangle_invalid_args(self):
        with pytest.raises(ValueError):
            shape.Rectangle(2, -4)

    def test_square_repr(self):
        square = shape.Rectangle(2, 2)
        assert repr(square) == "<Rectangle 2x2>"
        del square


class TestTriangle:
    def setup_method(self):
        self.triangle = shape.Triangle(2, 4, 6, 8, 10)

    def teaerdown_method(self):
        del self.triangle

    def test_triangle_area(self):
        assert self.triangle.area() == 4

    def test_triangle_perimeter(self):
        assert self.triangle.perimeter() == 24

    def test_triangle_type(self):
        assert self.triangle.triangle_type() == "Scalene"

    def test_triangle_invalid_args(self):
        with pytest.raises(ValueError):
            shape.Triangle(2, 4, 6, 8, -10)

    def test_triangle_repr(self):
        assert repr(self.triangle) == "<Triangle 2x4>"

    def test_equilateral_triangle(self):
        triangle = shape.Triangle(2, 2, 2, 2, 2)
        assert triangle.triangle_type() == "Equilateral"
        del triangle

    def test_isosceles_triangle(self):
        triangle = shape.Triangle(2, 4, 2, 4, 4)
        assert triangle.triangle_type() == "Isosceles"
        del triangle


class TestCircle:
    def setup_method(self):
        self.circle = shape.Circle(2)

    def teaerdown_method(self):
        del self.circle

    def test_circle_area(self):
        assert self.circle.area() == 4 * math.pi

    def test_circle_perimeter(self):
        assert self.circle.perimeter() == 4 * math.pi

    def test_circle_repr(self):
        assert repr(self.circle) == "<Circle with radius: 2>"

    def test_circle_invalid_args(self):
        with pytest.raises(ValueError):
            shape.Circle(-2)
