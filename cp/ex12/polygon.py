"""Exercises 12.2-12.4.: Polygon."""

import matplotlib.pyplot as plt
import numpy as np

class Polygon:
    """A class to represent a polygon.""" 
    

    def __init__(self, points):

        self.x = np.array([])
        self.y = np.array([])

        for coord in points:
            self.x = np.append(self.x, coord[0])
            self.y = np.append(self.y, coord[1])

    def plot_polygon(self):
        plt.plot(np.append(self.x, self.x[0]), np.append(self.y, self.y[0]))
        plt.show()

    def get_area(self):
        A = ( np.dot(self.x, np.roll(self.y, 1)) - np.dot(np.roll(self.x, 1), self.y) ) / 2
        return abs(A)
    
    def get_perimeter(self):
        return sqrt((self.x[:len(self.x)-1] - np.roll(self.x, -1)[:len(self.x)-1])**2 + (self.y[:len(self.y)-1] - np.roll(self.y, -1)[:len(self.y)-1])**2)