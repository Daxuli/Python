"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2,
                 label='Dashes set retroactively')
line1.set_dashes(dashes)

line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],
                 label='Dashes set proactively')

ax.legend(loc='lower right')


class RepresentadorPuntos(object):
    def __init__(self, punto):
        self.fig_init()
        self.pointplotter(punto)

    def fig_init(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def pointplotter(self, punto):
        self.ax.plot(punto.x, punto.y, "o")

class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt1 = Punto(1, 2)
pt2 = Punto(2, 3)
miRepresentacion = RepresentadorPuntos(pt1)
miRepresentacion = RepresentadorPuntos(pt2)

plt.show()
