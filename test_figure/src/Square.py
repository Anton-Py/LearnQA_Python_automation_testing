from test_figure.src.Figure import Figure


class Square(Figure):
    name = "square"

    def __init__(self, side):
        self.side = side
        if not isinstance(side, (int, float)):
            raise TypeError()
        if side <= 0:
            raise AssertionError("value must be greater than 0")

    @property
    def area(self):
        area = self.side ** 2
        return area

    @property
    def perimetr(self):
        perimetr = self.side * 4
        return perimetr
