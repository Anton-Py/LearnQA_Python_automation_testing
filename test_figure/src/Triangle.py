import math

from test_figure.src.Figure import Figure


class Triangle(Figure):
    name = "triangle"

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        if not isinstance(side_a or side_b or side_c, (int, float)):
            raise TypeError()
        elif (side_a or side_b or side_c) <= 0:
            raise AssertionError("value must be greater than 0")
        c = max(side_a, side_b, side_c)
        b = min(side_a, side_b, side_c)
        a = sum([side_a, side_b, side_c]) - min(side_a, side_b, side_c) - max(side_a, side_b, side_c)
        if c >= a + b:
            raise ValueError("impossible")

    @property
    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        area = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return math.ceil(area)

    @property
    def perimetr(self):
        perimetr = self.side_a + self.side_b + self.side_c
        return perimetr
