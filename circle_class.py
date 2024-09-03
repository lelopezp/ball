class Circle:
    def __init__(self, x, y, r, v):
        self._x = x
        self._y = y
        self._radius = r
        self._velocity = v
        self._horizontal_velocity = 4 * v

    def x(self):
        return self._x

    def y(self):
        return self._y

    def radius(self):
        return self._radius

    def velocity(self):
        return self._velocity

    def go_right(self):
        self._x += self._horizontal_velocity

    def go_left(self):
        self._x -= self._horizontal_velocity

    def fall(self):
        self._y += 2 * self._velocity

    def stuck(self):
        self._y -= self._velocity