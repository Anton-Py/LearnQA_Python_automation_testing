from src.Figure import Figure


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        if not isinstance(side_a or side_b, (int, float)):
            raise TypeError()
        if (side_a or side_b) <= 0:
            raise AssertionError("value must be greater than 0")

    @property
    def area(self):
        area = self.side_a * self.side_b
        return area

    @property
    def perimetr(self):
        perimetr = (self.side_a + self.side_b) * 2
        return perimetr
