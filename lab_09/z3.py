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
    
p = Point(2,1)
x = p*2
print(x)