import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize("circle_side", [2, 3, 13])
def test_circle_creation_positive(circle_side):
    circle = Circle(circle_side)


@pytest.mark.parametrize("circle_side", [-1, 0, -2])
def test_circle_creation_negative_with_num(circle_side):
    with pytest.raises(AssertionError):
        Circle(circle_side)


@pytest.mark.parametrize("circle_side", ["q", ""])
def test_circle_creation_negative_with_srt(circle_side):
    with pytest.raises(TypeError):
        Circle(circle_side)


@pytest.mark.parametrize(
    "circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a, rectangle_side_b, square_side", [
        (1, 2, 2, 3, 2, 4, 3),
        (3, 2, 3, 4, 2, 3, 9),
        (7, 5, 4, 3, 6, 5, 11)])
def test_circle_add_area_positive(circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a,
                                  rectangle_side_b, square_side):
    circle = Circle(circle_side)
    triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
    rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
    square = Square(square_side)
    circle.add_area(triangle)
    circle.add_area(rectangle)
    circle.add_area(square)


def test_circle_add_area_negative(circle_side=3):
    with pytest.raises(ValueError):
        circle = Circle(circle_side)

        class Rhombus:
            pass

        rhombus = Rhombus()
        circle.add_area(rhombus)
