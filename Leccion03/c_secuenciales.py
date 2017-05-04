"""
Colecciones de datos
4 - List
5 - Tuples (son inmutables)
6 - Sets (conjunto unico de elementos)
7 - Dictionary (llave-valor)

(tb se puede iterar en las llaves/valores de los diccionarios y los sets)
"""

miLista = list()
miLista2 = list([1, "uno", "1"])  # list es una funcion que coge solo un argumento: list(algo)
miLista3 = list((1, "uno", "2"))
miLista4 = [1, "uno", "1"]

print(id(miLista), type(miLista), miLista)
print(id(miLista2), type(miLista2), miLista2)
print(id(miLista3), type(miLista3), miLista3)
print(id(miLista4), type(miLista4), miLista4)
print("-------------")
# ----------------------------------------------
miLista4.append("el quinto elemento")
print(id(miLista4), type(miLista4), miLista4)
miLista5 = miLista4  # ambos tienen el mismo id, por eso si modificamos miLista5 tambien lo hacemos en miLista4
mielem = miLista5.pop()
print(mielem)
print(id(miLista4), type(miLista4), miLista4)
print("-------------")
# ----------------------------------------------
import copy

miLista6 = copy.deepcopy(miLista4)  # con esta funcion ya cambiamos a una nueva id para miLista6
miLista6.extend([1, 2, 3])
print(id(miLista6), type(miLista6), miLista6)
miLista6.append(["a", "b", "c"])
print(id(miLista6), type(miLista6), miLista6)
print(miLista6[6])
print(miLista6[6][1])
