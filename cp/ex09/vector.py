"""This file contains all the exercises relating to the Vector Exercises (9.4-9.7)."""

class Vector:
    """A class that represents a Vector, defined by the endpoint :math:`(x,y)`.""" 

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dot(self, Vector):
        return self.x * Vector.x + self.y * Vector.y
