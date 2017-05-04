"""
Mas tutoriales, informacion de numpy, scipy, matplotlib,...

http://pybonacci.org/tag/aeropython/

http://pybonacci.org/2015/10/15/curso-de-python-en-la-etsiae-4a-edicion/#more-3491
https://github.com/AeroPython/Curso_AeroPython

"""

# from __future__ import print_function, division  # Como ya estamos en 3.6 no tendria que hacer falta

import numpy as np

"""
Numpy da acceso a una serie de librerias matematicas

TODO: comprobar como mejorar la precision
"""
print("%.20f" % (1/3,))
print("%.20f" % (np.float64(np.float64(1) / np.float64(3))))  # no he conseguir aumentar la precision
print("sqrt(2)=%s, cos(90)=%s (OJO, RADIANES)" % (np.sqrt(2), np.cos(90),))
print("Pi=%.20f, e=%.20f" % (np.pi, np.e,))
print("----------------------------------------------")

# -------------------------------------------------------------------------------------------------------------
"""
Tambien me permite trabajar con arrays
Esto habilitara vectorizar funciones, y evitar bucles (no siempre) con operaciones algebraicas

"""
# Un array se inicializa como una lista

miarray = np.array([1, 2, 3])
print(id(miarray), type(miarray[0]), miarray)
miarray = np.float64(miarray)
print(id(miarray), type(miarray[0]), miarray)
print("----------------------------------------------")

# -------------------------------------------------------------------------------------------------------------
# Importo el modulo time para hacer un pequeño profile de dos funciones
import time
N = M = 100  # Si, puedo inicializar dos variables iguales asi

a = np.empty(N*M).reshape(N, M)  # Hay que tener cuidado sando la funcion empty porque no son realmente ceros
print("Array 'vacio':\n", a[0:2, 0:2])
b = np.random.rand(N*M).reshape(N, M)
c = np.random.rand(N*M).reshape(N, M)

# suma de dos matrices elemento a elemento mediante bucle
start = time.time()
for i in range(N):
    for j in range(M):
        a[i, j] = b[i, j] + c[i, j]
print("Nuestro bucle tardó %.3e" % (time.time() - start,))

start = time.time()
a = b + c
print("La suma matricial tardó %.3e" % (time.time() - start,))  # funciones ya definidas suelen ser mas rapidas
print("----------------------------------------------")

# -------------------------------------------------------------------------------------------------------------
"""Si quiero un bucle con numeros consecutivos,...
Evito bucles
"""
arr1 = np.arange(10)  # va de 0 a 9
print(type(arr1), arr1)
arr2 = np.arange(10, 3, -1)
# arr2 = np.arange(3, 10, -1)
print(type(arr2), arr2)

print()
print("Espaciado lineal:", np.linspace(0, 7.3, 5))  # divide [0, 7.3] en 5 valores equiespaciados
print("Espaciado logaritmico:", np.logspace(0, 3, 4))  # lo mismo en el intervalo [1e0, 1e3]


"""Importacion de datos
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/012-NumPy-Importacion.ipynb
"""