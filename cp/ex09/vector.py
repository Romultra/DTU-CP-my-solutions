"""This file contains all the exercises relating to the Vector Exercises (9.4-9.7)."""

class Vector:
    """A class that represents a Vector, defined by the endpoint :math:`(x,y)`.""" 

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, Vector):
        return self.x * Vector.x + self.y * Vector.y
    
    def scale(self, s):
        return Vector(self.x * s, self.y * s)

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)