from test_figure.src.Figure import Figure


class Circle(Figure):
    name = "circle"

    def __init__(self, side):
        self.side = side
        if not isinstance(side, (int, float)):
            raise TypeError()
        if side <= 0:
            raise AssertionError("value must be greater than 0")

    @property
    def area(self):
        p = 3.14
        area = p * (self.side ** 2)
        return area

    @property
    def perimetr(self):
        p = 3.14
        perimetr = 2 * p * self.side
        return perimetr
