import pytest
from test_figure.src import Circle
from test_figure.src.Rectangle import Rectangle
from test_figure.src import Square
from test_figure.src import Triangle


@pytest.mark.parametrize("triangle_side_a, triangle_side_b, triangle_side_c", [(2, 6, 5), (3, 4, 5), (3, 3, 3)])
def test_triangle_creation_positive(triangle_side_a, triangle_side_b, triangle_side_c):
    Triangle(triangle_side_a, triangle_side_b, triangle_side_c)


@pytest.mark.parametrize("triangle_side_a, triangle_side_b, triangle_side_c, expected_result",
                         [(2, 3, 4, 3), (3, 3, 3, 4)])
def test_triangle_creation_positive_area(triangle_side_a, triangle_side_b, triangle_side_c, expected_result):
    triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
    assert triangle.area == expected_result


@pytest.mark.parametrize("triangle_side_a, triangle_side_b, triangle_side_c, expected_result",
                         [(2, 3, 4, 9), (3, 3, 3, 9)])
def test_triangle_creation_positive_perimetr(triangle_side_a, triangle_side_b, triangle_side_c, expected_result):
    triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
    assert triangle.perimetr == expected_result


@pytest.mark.parametrize("triangle_side_a, triangle_side_b", [(2, 3)])
def test_triangle_negative_without_one_value(triangle_side_a, triangle_side_b):
    with pytest.raises(TypeError):
        triangle = Triangle(triangle_side_a, triangle_side_b)


@pytest.mark.parametrize("triangle_side_a, triangle_side_b, triangle_side_c", [(1, 1, 3), (3, 4, 18)])
def test_triangle_creation_negative_with_num(triangle_side_a, triangle_side_b, triangle_side_c):
    with pytest.raises(ValueError):
        Triangle(triangle_side_a, triangle_side_b, triangle_side_c)


@pytest.mark.parametrize("triangle_side_a, triangle_side_b, triangle_side_c", [(-1, 0, -2), (0, 0, -5)])
def test_triangle_creation_negative_with_num_less_zero(triangle_side_a, triangle_side_b, triangle_side_c):
    with pytest.raises(AssertionError):
        Triangle(triangle_side_a, triangle_side_b, triangle_side_c)


@pytest.mark.parametrize("triangle_side_a, triangle_side_b, triangle_side_c", [("a", 2, 3)])
def test_triangle_creation_negative_with_srt(triangle_side_a, triangle_side_b, triangle_side_c):
    with pytest.raises(TypeError):
        Triangle(triangle_side_a, triangle_side_b, triangle_side_c)


@pytest.mark.parametrize(
    "circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a, rectangle_side_b, square_side", [
        (8, 3, 3, 3, 6, 5, 2),
        (6, 4, 2, 3, 7, 3, 4),
        (2, 5, 6, 9, 8, 5, 13)])
def test_triangle_add_area_positive(circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a,
                                    rectangle_side_b, square_side):
    circle = Circle(circle_side)
    triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
    rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
    square = Square(square_side)
    triangle.add_area(circle)
    triangle.add_area(rectangle)
    triangle.add_area(square)


def test_triangle_add_area_negative(triangle_side_a=2, triangle_side_b=2, triangle_side_c=2):
    with pytest.raises(ValueError):
        triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)

        class Rhombus:
            pass

        rhombus = Rhombus()
        triangle.add_area(rhombus)
