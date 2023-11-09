"""The code for vector operator overloading."""
from typing import Any


class Vector:
    r"""A class that represents a Vector, defined by the endpoint :math:`(x,y)`.""" 

    def __init__(self, x, y):
        """Construct a new Vector-object.

        :param x: The x-component of the vector
        :param y: The y-component of the vector
        """
        self.x = x
        self.y = y
    
    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)
    
    def __sub__(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)
    
    def __mul__(self, v2):
        return self.x * v2.x + self.y * v2.y
