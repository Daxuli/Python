import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
from scipy import optimize as opt


# ------------------------------------------------- funciones
def f1(a):
    return np.log(a) - a * np.sin(a)


def f2(p):
    a, b = p
    return a * np.cos(b)


def g1(p):  # con tupla
    a, b = p  # los parentesis son opcionales
    return np.log(a) - a * np.sin(a), a * np.cos(b)


def g2(p):  # con lista
    a = p[0]
    b = p[1]
    """
    a, b = p
    asi tambien vale
    """
    return np.log(a) - a * np.sin(a), a * np.cos(b)
# ------------------------------------------------- cambios de signo
x = np.linspace(.1, 10, num=100)  # con 100 obtenemos intervalos de .1
x1 = x[0:len(x)-1]  # [------------x]
x2 = x[1:len(x)]  # [x------------]

signos = np.sign(f1(x1) * f1(x2))  # sign: + -> 1; - -> -1; 0 -> 0
plt.figure(1)
plt.plot(x1, signos)

indices = np.where(signos == -1)
print(indices[0], x1[indices[0]])
print(indices[0], x2[indices[0]])

intervalos = []
for _ in indices[0]:
    intervalos.append([x1[_], x2[_]])
print("intervalos con cambio de signo:", intervalos)

# print(np.log(0)/np.log(0))  para sacar un nan
print("--------------------------------------")

# ------------------------------------------------- optimización de f1
cerob = opt.brentq(f1, .1, 3)
cerof = opt.fsolve(f1, np.array([10]))
print("brentq:", cerob)
print("fsolve:", cerof[0])

plt.figure(2)
plt.plot(x, f1(x), 'k', lw=2, label="$F(x)$")
plt.plot(x, np.log(x), label="$\log{x}$")
plt.plot(x, x * np.sin(x), label="$\sin{x}$")
plt.plot(x, np.zeros_like(x), 'k--')

ceros = []
for _ in intervalos:  # como ya sabemos los intervalos con cambio de signo, automatizamos para sacar todos los ceros
    ceros.append(opt.brentq(f1, _[0], _[1]))

for _ in ceros:  # con los ceros, automatizamos para que los represente en plot
    if ceros.index(_) == 0:
        plt.plot(_, 0, "o", color="C2", label="zeros")
    else:
        plt.plot(_, 0, "o", color="C2")  # color en la posición 2 (empezando con el 0) del ciclo de colores

plt.legend(loc=4)
print("--------------------------------------")

# ------------------------------------------------- optimización de g1/g2
print("Resolución de sistema de ecuaciones")
print("con tuplas", opt.fsolve(g1, np.array((2, 2))))
print("con listas", opt.fsolve(g2, np.array([2, 2])))

plt.show()
