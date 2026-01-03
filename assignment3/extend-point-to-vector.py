import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("Distance to expects a Point")
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Vector(Point):
    def __str__(self):
        return f"Vector <{self.x}, {self.y}>"
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)

    print(p1)
    print(p2)
    print("Distance:", p1.distance_to(p2))
    print("Equality:", p1 == Point(1, 2))

    v1 = Vector(3, 5)
    v2 = Vector(-1, 7)

    print(v1)
    print(v2)
    print("Vector sum: v1 + v2 =", v1 + v2)
