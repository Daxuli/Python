"""

"""
from matplotlib.pyplot import figure, show
from matplotlib.figure import Figure

class Punto(object):
    def __init__(self, x, y):
        """
        Inicializador de la clase punto
        :param x: Coordenada x
        :param y: Coordenada y
        """
        self.x = x
        self.y = y


class RepresentadorPuntos(Figure):
    def __init__(self, listaPuntos):
        """
        Clase propia para representar instancias de la clase punto
        """
        self.fig_init()

        if isinstance(listaPuntos, list):
            self.plot_pointlist(listaPuntos)
        elif isinstance(listaPuntos, Punto):
            self.plot_point(listaPuntos)
        else:
            raise TypeError

    def fig_init(self):
        self.fig = figure()
        self.ax = self.fig.add_subplot(111)
        show(block=False)

    def plot_pointlist(self, listaPuntos):
        for elemento in listaPuntos:
            self.plot_point(elemento)

    def plot_point(self, punto):
        self.ax.plot(punto.x, punto.y, 'o', color='black')


pt1 = Punto(0, 1)
pt2 = Punto(1, 2)
listaPuntos = list([pt1, pt2])
listaPuntos.append(Punto(3, 4))


fig1 = RepresentadorPuntos(listaPuntos)


"""
Esta linea es necesara para que se represente la grafica
"""
show()