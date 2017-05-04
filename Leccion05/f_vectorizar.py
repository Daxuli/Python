"""
Otra tecnica para evitar bucles, (y habrá alguna mas que me haya dejado

Es vectorizar la funcion (numpy) o utilizar las funciones map, reduce, filter,... (alguna estaba deprecada ya)
"""
milista = list(range(0, 11))  # [0, 10]
tupla = (1, 2, 3)
mifun = lambda x: x**2

# -------------------------------------------------------------------------------- map()
valores = map(mifun, milista)  # aplica la funcion mifun a milista

print(type(valores), valores)  # no sacamos los valores asi.
for elem in valores:  # tenemos que iterar para sacarlo
    print(elem, end=", ")
print()

print(list(valores))  # tampoco podemos sacarlo asi
mapa = list(map(mifun, milista))
print(mapa)  # una vez en lista ya podemos usar print directamente
print("-------------------------------------------")

# -------------------------------------------------------------------------------- filter()
filtro = list(filter(lambda x: x % 3 == 0, milista))  # guarda los argumentos de milista que cumplan la funcion
print("Filter:", filtro)
print("-------------------------------------------")

# -------------------------------------------------------------------------------- reduce()
from functools import reduce  # hay que hacer una importacion

print("Reduce:", reduce(lambda x, y: x + y, milista))  # aplica de forma recursiva la misma operacion, deprecado
print("-------------------------------------------")

# -------------------------------------------------------------------------------- reduce()
import numpy as np

mifun_vec = np.vectorize(mifun)  # "vectoriza" una funcion para que pueda aplicarse a un array
valores2 = mifun_vec(milista)
print(type(valores2), valores2)

