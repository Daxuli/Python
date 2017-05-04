from matplotlib.pyplot import figure, show
from matplotlib.figure import Figure


class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RepresentadorPuntos(object):
    def __init__(self, listaPuntos):
        """
        Clase propia para representar instancias
         de la clase Punto
        """
        self.fig_init()

        if isinstance(listaPuntos, list):
            self.plot_pointlist(listaPuntos)
        elif isinstance(listaPuntos, Punto):
            self.plot_point(listaPuntos)
        else:
            print("No se pintarlo")

    def fig_init(self):
        self.fig = figure()
        self.ax = list(["", ""])
        self.ax[0] = self.fig.add_subplot(211)
        self.ax[1] = self.fig.add_subplot(234)
        """
        matriz de 2x3, coge la posicion 4
        [1][2][3]
        [4][5][6]
        """
        show(block=False)# Puede ser util para guardar sin bloquear el hilo

    def plot_pointlist(self, listaPuntos):
        for elemento in listaPuntos:
            self.plot_point(elemento)

    def plot_point(self, punto):
        self.ax[0].plot(punto.x, punto.y, "o", color="orange")


pt1 = Punto(0, 0)
pt2 = Punto(1, 2)

listaPuntos = list([pt1, pt2])
listaPuntos.append(Punto(2, 3))
fig1 = RepresentadorPuntos(listaPuntos)

pt3 = Punto(2, 1)
fig2 = RepresentadorPuntos(pt3)

#  show es necesario en matplotlib

show()