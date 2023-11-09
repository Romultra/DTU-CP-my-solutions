"""The Rectangle-exercises 9.1-9.3."""
import matplotlib.pyplot as plt
from cp.ex09.vector import Vector

class Rectangle:
    """A class that represents a Rectangle."""

    def __init__(self, width, height, x_c, y_c) -> None:
        self.width = width
        self.height = height
        self.x_c = x_c
        self.y_c = y_c
    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * (self.height + self.width)
    
    def get_corners(self):
        list_x = []
        list_y = []

        list_x.append(self.x_c - self.width/2)
        list_x.append(self.x_c - self.width/2)
        list_x.append(self.x_c + self.width/2)
        list_x.append(self.x_c + self.width/2)

        list_y.append(self.y_c - self.height/2)
        list_y.append(self.y_c + self.height/2)
        list_y.append(self.y_c + self.height/2)
        list_y.append(self.y_c - self.height/2)

        return (list_x, list_y)
    
    def plot_rectangle(self, color):
        corners = self.get_corners()
        corners[0].append(corners[0][0])
        corners[1].append(corners[1][0])
        plt.plot(corners[0], corners[1], color=color)
        plt.show()

    def translate(self, v):
        self.x_c += v.x
        self.y_c += v.y