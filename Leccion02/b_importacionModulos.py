#  para importar modulos uso import
import Leccion02.a_moduloBasico

print(Leccion02.a_moduloBasico.sqrt, Leccion02.a_moduloBasico.sqrt(4))

import math
print(math.sqrt, math.sqrt(4))


"""
importar solo algunas funciones del modulo
"""

from math import sqrt, sin

print(sqrt(4))
print(sin(0))

from Leccion02.a_moduloBasico import sqrt

print(sqrt(4))

#  Para importar todas las funciones
from math import *
print("cos(4)=", cos(4))

import math as mt
print("cos(90)=", mt.cos(radians(90)))
