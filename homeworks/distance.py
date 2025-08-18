class Distance:
    FACT = {'m': 1, 'km': 1000, 'cm': 0.01}

    def __init__(self, value, unit ='m'):
        if unit not in self.FACT:
            raise ValueError('Unit must be one of: m, km, cm')
        self.value = float(value)
        self.unit = unit

    def __str__(self):
        return f'{self.value:g} {self.unit}'

    def _to_m(self):
        return self.value * self.FACT[self.unit]

    def __add__(self, other):
        res_m = self._to_m() + other._to_m()
        return Distance(res_m / self.FACT[self.unit], self.unit)

    def __sub__(self, other):
        res_m = self._to_m() - other._to_m()
        if res_m < 0:
            raise ValueError("Результат не может быть отрицательным")
        return Distance(res_m / self.FACT[self.unit], self.unit)

    def __eq__(self, other):
        return self._to_m() == other._to_m()

    def __lt__(self, other):
        return self._to_m() < other._to_m()

    def __le__(self, other):
        return self._to_m() <= other._to_m()

    def __gt__(self, other):
        return self._to_m() > other._to_m()

    def __ge__(self, other):
        return self._to_m() >= other._to_m()