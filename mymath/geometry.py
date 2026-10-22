from .base import my_sqrt, my_pow, get_PI
from .exceptions import NonNumericError, DegenerateShapeError, InvalidShapeError

my_PI = get_PI()

class Point:
    def __init__(self, x, y):
        try:
            self.x = x
            self.y = y
        except ValueError:
            raise NonNumericError("Input numbers must be numeric!")


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
        try:
            self.p1 = p1
            self.p2 = p2
        except NonNumericError:
            raise


    def length(self):
        l = self.p1.distance_to(p2)
        if l == 0:
            raise DegenerateShapeError("Line segment length is zero!")
        return l

    
    def midpoint(self):
        return Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)


class Circle:
    def __init__(self, center, radius):
        try:
            self.center = center
        except NonNumericError:
            raise
        try:
            self.radius = radius
        except (ValueError, DegenerateShapeError) as e:
            error_text = f"Failed to create the circle due to invalid radius!\n{e.args[0]}"
            raise InvalidShapeError(error_text)


    @property
    def radius(self):
        return self._radius


    @r.setter
    def radius(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Circle radius must be positive!")
        if value == 0:
            raise DegenerateShapeError("Circle radius mustn't be zero!")

        self._radius = value


    def area(self):
        return my_PI * my_pow(self.radius, 2)


    def perimeter(self):
        return 2 * my_PI * self.radius


    def contains(self, point):
        return self.center.distance_to(point) <= self.radius


class Triangle:
    def __init__(self, a, b, c):
        try:
            self.a = a
            self.b = b
            self.c = c
        except NonNumericError:
            raise

        self.ab = a.distance_to(b)
        self.ac = a.distance_to(c)
        self.bc = b.distance_to(c)
        if 0 in (self.ab, self.bc, self.ac):
            raise DegenerateShapeError("Triangle can't contain a side equal to zero!")
        if self.ab + self.ac <= self.bc or self.ac + self.bc <= self.ab or self.ab + self.bc <= self.ac:
            raise InvalidShapeError("Violation of the triangle inequality theorem!")


    def perimeter(self):
        return self.ab + self.ac + self.bc


    def area(self):
        p = self.perimeter() / 2.0
        return my_sqrt(p * (p - self.ab) * (p - self.ac) * (p - self.bc))


    def contains(self, point):
        s1 = Triangle(self.a, self.b, point).area()
        s2 = Triangle(self.b, self.c, point).area()
        s3 = Triangle(self.a, self.c, point).area()

        return s1 + s2 + s3 == self.area()


class Rectangle:
    def __init__(self, a, b, c, d):
        try:
            self.a, self.b, self.c, self.d = a, b, c, d
        except NonNumericError:
            raise
        
        self.a, self.b, self.c, self.d = sorted([a, b, c, d], key=lambda p: (p.x, p.y))
        if not is_rectangle(a, b, c, d):
            raise InvalidShapeError("Invalid sides for rectangle!")

    
    @classmethod
    def is_rectangle(cls, p1, p2, p3, p4):
        a, b, c, d = sorted([p1, p2, p3, p4], key=lambda p: (p.x, p.y))

        if (a.x == b.x and a.y == b.y) or (c.x == d.x and c.y == d.y):
            return False
    
        if a.x == b.x and b.y == c.y and c.x == d.x and d.y == a.y:
            return True

        mid_ad_x = (a.x + d.x) / 2
        mid_ad_y = (a.y + d.y) / 2
        mid_bc_x = (b.x + c.x) / 2
        mid_bc_y = (b.y + c.y) / 2

        centers_match = mid_ad_x == mid_bc_x and mid_ad_y == mid_bc_y
        length_match = a.distance_to(d) == b.distance_to(c)

        return centers_match and length_match


    def perimeter(self):
        ab = self.a.distance_to(b)
        bc = self.b.distance_to(c)
        return 2 * (ab + bc)


    def area(self):
        ab = self.a.distance_to(b)
        bc = self.b.distance_to(c)
        return ab * bc


    def contains(self, point):
        s1 = Triangle(point, self.a, self.b).area()
        s2 = Triangle(point, self.b, self.c).area()
        s3 = Triangle(point, self.c, self.d).area()
        s4 = Triangle(point, self.a, self.d).area()

        return s1 + s2 + s3 + s4 == self.area()
