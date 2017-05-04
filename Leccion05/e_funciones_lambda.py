"""
La funcion lambda es una forma particular de crear funciones en una linea,...

Me salto la declaracion,... el archivo adicional,...

Puede resultar util cuando vectoricemos operaciones (es decir, aplicar la misma funcion a elementos de un array)
"""
import numpy
"""Si desconozco la función lambda"""


def g2(x, y):
    return x*y

print(type(g2), g2(2, 3))

""" Con una funcion lambda"""
g1 = lambda x, y: x*y  # lambda *argumentos*: *return*
print(type(g1), g1(2, 3))
print("-------------------------------------------")

# --------------------------------------------------------------------------------

"""Otro uso,... algo parecido (no tanto) a lo que haremos con los decoradores
Hacer que una funcion devuelva otra funcion

No es el mejor ejemplo (aqui yo sacaria el string, y usaria diccionarios)

Donde lo aplicaria,... para resolver un sistema de ecuaciones, lo resulvo en base a una variable
"solver",... que me permito ir variando para ver el cambio (lo veremos en scipy)
"""


def saludo_es():
    return "Hola, buenos dias"


def saludo(idioma):
    """
    Otra forma de usar los condicionales,... si un elemento esta en una lista
    :param idioma:
    :return:
    """
    if idioma in ["español", "es"]:
        return saludo_es

    elif idioma in ["english", "us", "en"]:
        return lambda: "Hello, Good Morning"

    else:
        return lambda: "No reconozco el idioma"

print(saludo_es)
print(saludo_es())
print(saludo("es"))
print(saludo("es")())

misaludo = saludo("en")
print(misaludo())

print(saludo("sdlfgsdfklgh")())
print("-------------------------------------------")

# --------------------------------------------------------------------------------
# numpy.power(*base*, *exponente*)  p.e. numpy.power(2,3) = 2**3
mipow = lambda x: numpy.power(x, 3)  # si por ejemplo vamos a usar siempre con exponente 3
print(mipow(range(7)))
