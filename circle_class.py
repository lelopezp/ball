class Circle:
    def __init__(self, x, y, r, v):
        self._x = x
        self._y = y
        self._radius = r
        self._velocity = v

    def x(self):
        return self._x

    def y(self):
        return self._y

    def radius(self):
        return self._radius

    def velocity(self):
        return self._velocity

    def go_right(self):
        self._x += self._velocity

    def go_left(self):
        self._x -= self._velocity

    def fall(self):
        self._y += self._velocity

    def pushed(self, y):
        self._y = y - self._radius