from base import my_sqrt, my_pow, get_PI

my_PI = get_PI()

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


class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def length(self):
        return self.p1.distance_to(p2)

    
    def midpoint(self):
        return Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


    @property
    def radius(self):
        return self._radius


    @r.setter
    def radius(self, value):
        value = float(value)
        if value < 0:
            raise ValueError

        self._radius = value


    def area(self):
        return my_PI * my_pow(self.radius, 2)


    def perimeter(self):
        return 2 * my_PI * self.radius


    def contains(self, point):
        return self.center.distance_to(point) <= self.radius
