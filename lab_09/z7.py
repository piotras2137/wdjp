class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __mul__(self, scalar):
        if isinstance(scalar, int):
            return Point(self.x * scalar, self.y * scalar)
        else:
            raise ValueError("Scalar must be integer")

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

        return False

    def __repr__(self) -> str:
        return str(self)


class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        points_str = ", ".join(str(point) for point in self.points)
        return f"Polygon[{points_str}]"

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return self.points[item.start:item.stop:item.step]
        else:
            raise TypeError("invalid arguemnt type. expected int or slice")


a = Point()
b = Point(2, 1)
c = Point(3, 7)
poly = Polygon()
poly.add_point(a)
poly.add_point(b)
poly.add_point(c)
print(poly[0])
print(poly[2])
