"""
Otras alternativas de generar arrays
"""
import numpy as np

print("Array de varias dimensiones,.... lista de listas de ...")
miarray = np.array([[0, 1, 2], [3, 4, 5]])
print(type(miarray), "\n", miarray)
print("----------------------------------------------")

# -------------------------------------------------------------------------------------------------------------
"""
Puedo indexar como una lista de una lista,...
O como si fuese una matrix (matlab)
"""
print("Indexacion")
print("Cuidado,... que estoy pidiendo cosas distintas")
print(miarray[:][0])  # ojo, [:] no hace nada. estamos imprimiendo el primer elemento de miarray: [0, 1, 2]
print([i[0] for i in miarray])  # sin usar numpy, esto es una solucion para imprimir la primera columna

print("Con numpy")
print(miarray[:, 0])  # coge de cada fila la columna 1 (indice 0)
print(miarray[:, 1:3])  # coge de cada fila las columnas 2 y 3 (indices 1 y 2)
print("----------------------------------------------")

# -------------------------------------------------------------------------------------------------------------
"""
Tambien puedo inicializarlo con ciertos valoes,...
"casi identidad": eye, identity
Ceros, vacia

Ojo,... vacia no es vacia,... es casi vacia
"""
miarray1 = np.empty((2, 2))
miarray2 = np.identity(2)
miarray3 = np.eye(2, 3)
print("Vacia:\n", miarray1)
print("Vacia: %.3e\n" % (miarray1[0, 0],))

print("Identidad:\n", miarray2)
print("Determinante:", np.linalg.det(miarray2), "\n")

print("Diagonal de unos:\n", miarray3)
print("----------------------------------------------")

# -------------------------------------------------------------------------------------------------------------
"""
Puedo hacer comparaciones de matrices, evitando bucles,

Os dejo buscar como hacer intersecciones, uniones, diferencias de conjuntos de elementos,...
"""

miarray1 = np.empty((2, 2))
miarray2 = np.zeros((2, 2))
miarray3 = np.zeros((2, 2)) + np.float16(2e-7)*np.random.rand(2, 2)

print(miarray1 == miarray2)  # los compara elemento por elemento y da un boolean para cada uno
print(np.all(miarray1 == miarray2))  # con all solo va a salir uno para el conjunto
print(np.all(miarray2 == miarray3))  # va a salir False
print(np.isclose(miarray2, miarray3, atol=1e-7))  # si la diferencia esta por debajo de atol saldra True
print("----------------------------------------------")

# -------------------------------------------------------------------------------------------------------------
print(np.divide(1, 1e-6))  # ojo con divisones de numeros pequeños
