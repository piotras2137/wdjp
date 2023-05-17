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


a = Point()
b = Point(1, 2)
c = Point(0, 0)

print(a == b)
print(a == c)
