"""
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/014-NumPy-AlgerbraLineal.ipynb

"""
import numpy as np

M = np.array([
    [1, 2],
    [3, 4]
])
v = np.array([1, -1])

print("M:\n", M)
print("v:\n", v)
print("-------------------------------------------")

# --------------------------------------------------------------------------------
u = np.dot(M, v)  # v como vector columna, u tambien
print("M.v=", u)

print("Determinante(M)=", np.linalg.det(M))
print("Inversa(M):\n", np.linalg.inv(M))
print("-------------------------------------------")

# --------------------------------------------------------------------------------
print("Autovectores(M):")
print(type(np.linalg.eig(M)), np.linalg.eig(M))  # salen dos arrays en la tupla

print("\nDescomprimo la tupla de salida con otra tupla")  # para que quede mas ordenado
(autovalor, autovector) = np.linalg.eig(M)
print("autovalor:", autovalor)
print("autovector:", autovector)
