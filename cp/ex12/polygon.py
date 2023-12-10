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
        return np.sum(np.sqrt((self.x - np.roll(self.x, -1))**2 + (self.y - np.roll(self.y, -1))**2))

    def smooth_polygon(self, alpha):
        self.x[1:len(self.x)-1] = (1-alpha) * self.x[1:len(self.x)-1] + (1/2)*alpha*(np.roll(self.x[1:len(self.x)-1], -1) + np.roll(self.x, 1))
        self.y[1:len(self.y)-1] = (1-alpha) * self.y[1:len(self.y)-1] + (1/2)*alpha*(np.roll(self.y[1:len(self.y)-1], -1) + np.roll(self.y, 1))

        self.x[0] = (1-alpha) * self.x[0] + (1/2)*alpha*(self.x[-1] + self.x[1])
        self.y[0] = (1-alpha) * self.y[0] + (1/2)*alpha*(self.y[-1] + self.y[1])
        
        self.x[-1] = (1-alpha) * self.x[-1] + (1/2)*alpha*(self.x[-2] + self.x[0])
        self.y[-1] = (1-alpha) * self.y[-1] + (1/2)*alpha*(self.y[-2] + self.y[0])

P = Polygon([(24, 12), (40, 16), (36, 8), (44, 4), (28, 0), (18, 4), (12, 0), (0,4), (8, 12), (4, 16)])
P.plot_polygon()
P.smooth_polygon(0.5)
P.plot_polygon()