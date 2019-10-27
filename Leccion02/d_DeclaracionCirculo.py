"""
Some additional resources for the new concepts:
https://realpython.com/python-super/
https://www.programiz.com/python-programming/property
"""
import math
import Leccion02.c_DeclaracionPunto


class Circulo(Leccion02.c_DeclaracionPunto.Punto):
    def __init__(self, x, y, radio):
        super(Circulo, self).__init__(x, y)
        self.radio = radio  # calls to the @radius.setter and saves the variable at _radius

    @property  # the first time is for the getter
    def area(self):  # we want to know the area of the circle, which was defined with its radius
        self._area = math.pi*self.radio**2  # calls to the @radius.getter and takes the value from _radius
        return self._area  # private variable

    @area.setter  # defining its setter function
    def area(self, area):  # we are setting the area, so the radius must change
        self.radio = math.sqrt(area/math.pi)  # calls to the @radius.setter and saves the variable at _radius

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio < 0:
            self._radio = 0
            print("El radio era negativo")
        else:
            self._radio = radio

c1 = Circulo(2, 3, -5)
print(c1.area)

c1.radio = 3
print(c1.area)

c1.area = 20  # vemos que con 20 no asigna con total precision 20.0
print(c1.area, c1.radio)

c1.area = 19
print(c1.area, c1.radio)

"""
Let's see which attributes c1 has
"""
print("-----")
print(c1.__dict__)  # _radius and _area are its actual attributes
