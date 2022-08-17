import pytest
from test_figure.src import Circle
from test_figure.src.Rectangle import Rectangle
from test_figure.src import Square
from test_figure.src import Triangle


@pytest.mark.parametrize("rectangle_side_a, rectangle_side_b", [(2, 6), (3, 4), (3, 3)])
def test_rectangle_creation_positive(rectangle_side_a, rectangle_side_b):
    Rectangle(rectangle_side_a, rectangle_side_b)


@pytest.mark.parametrize("rectangle_side_a, rectangle_side_b, expected_result",
                         [(2, 3, 6), (3, 3, 9)])
def test_rectangle_creation_positive_area(rectangle_side_a, rectangle_side_b, expected_result):
    rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
    assert rectangle.area == expected_result


@pytest.mark.parametrize("rectangle_side_a, rectangle_side_b, expected_result",
                         [(2, 3, 10), (3, 3, 12)])
def test_rectangle_creation_positive_perimetr(rectangle_side_a, rectangle_side_b, expected_result):
    rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
    assert rectangle.perimetr == expected_result


@pytest.mark.parametrize("rectangle_side_a", [2])
def test_triangle_negative_without_one_value(rectangle_side_a):
    with pytest.raises(TypeError):
        rectangle = Rectangle(rectangle_side_a)


@pytest.mark.parametrize("rectangle_side_a, rectangle_side_b", [(-1, 0), (0, 0)])
def test_triangle_creation_negative_with_num_less_zero(rectangle_side_a, rectangle_side_b):
    with pytest.raises(AssertionError):
        Rectangle(rectangle_side_a, rectangle_side_b)


@pytest.mark.parametrize("rectangle_side_a, rectangle_side_b", [("a", 8)])
def test_triangle_creation_negative_with_srt(rectangle_side_a, rectangle_side_b):
    with pytest.raises(TypeError):
        Rectangle(rectangle_side_a, rectangle_side_b)


@pytest.mark.parametrize(
    "circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a, rectangle_side_b, square_side", [
        (1, 2, 2, 2, 2, 4, 3),
        (3, 2, 3, 4, 2, 3, 9),
        (7, 5, 6, 9, 6, 5, 11)])
def test_rectangle_add_area_positive(circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a,
                                     rectangle_side_b, square_side):
    circle = Circle(circle_side)
    triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
    rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
    square = Square(square_side)
    rectangle.add_area(triangle)
    rectangle.add_area(circle)
    rectangle.add_area(square)


def test_rectangle_add_area_negative(rectangle_side_a=4, rectangle_side_b=3):
    with pytest.raises(ValueError):
        rectangle = Rectangle(rectangle_side_a, rectangle_side_b)

        class Rhombus:
            pass

        rhombus = Rhombus()
        rectangle.add_area(rhombus)
