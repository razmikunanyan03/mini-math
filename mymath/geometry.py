from base import my_sqrt, my_pow

class Point:
    def __init__(self, x, y):
        try:
            self.x = x
            self.y = y
        except ValueError:
            pass


    @property
    def x(self):
        return _x


    @x.setter
    def x(self, value):
        value = float(value)
        self._x = value


    @property
    def y(self):
        return _y

    
    @y.setter
    def y(self, value):
        value = float(value)
        self._y = value


    def distance_to(self, other):
        return my_sqrt(my_pow(self.x - other.x, 2) + my_pow(self.y - other.y, 2))
