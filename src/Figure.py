class Figure:
    name = None

    @property
    # TODO: Нужно обозначить как абстрактный метод
    def area(self):
        return True

    @property
    # TODO: Нужно обозначить как абстрактный метод
    def perimetr(self):
        return True

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area
