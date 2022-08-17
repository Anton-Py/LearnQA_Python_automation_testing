import pytest
from test_figure.src import Circle
from test_figure.src.Rectangle import Rectangle
from test_figure.src import Square
from test_figure.src import Triangle


@pytest.mark.parametrize("square_side", [5, 4, 3, 8])
def test_square_creation_positive(square_side):
    Square(square_side)


@pytest.mark.parametrize("square_side, expected_result",
                         [(3, 9), (5, 25)])
def test_square_creation_positive_area(square_side, expected_result):
    square = Square(square_side)
    assert square.area == expected_result


@pytest.mark.parametrize("square_side, expected_result",
                         [(3, 12), (5, 20)])
def test_square_creation_positive_perimetr(square_side, expected_result):
    square = Square(square_side)
    assert square.perimetr == expected_result


@pytest.mark.parametrize("square_side", [-1])
def test_square_creation_negative_with_num_less_zero(square_side):
    with pytest.raises(AssertionError):
        Square(square_side)


@pytest.mark.parametrize("square_side", ["q", ""])
def test_square_creation_negative_with_srt(square_side):
    with pytest.raises(TypeError):
        Square(square_side)


@pytest.mark.parametrize(
    "circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a, rectangle_side_b, square_side", [
        (1, 2, 2, 2, 2, 4, 3),
        (3, 2, 3, 4, 2, 3, 9),
        (7, 5, 6, 9, 6, 5, 11)])
def test_square_add_area_positive(circle_side, triangle_side_a, triangle_side_b, triangle_side_c, rectangle_side_a,
                                  rectangle_side_b, square_side):
    circle = Circle(circle_side)
    triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
    rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
    square = Square(square_side)
    square.add_area(triangle)
    square.add_area(circle)
    square.add_area(rectangle)


def test_square_add_area_negative(square_side=3):
    with pytest.raises(ValueError):
        square = Square(square_side)

        class Rhombus:
            pass

        rhombus = Rhombus()
        square.add_area(rhombus)
