class Point:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 

    def __str__(self):
        return f"Point({self.x},{self.y})"
    
p = Point(2,1)

print(p)