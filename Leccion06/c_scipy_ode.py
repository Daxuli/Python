"""
    https://en.wikipedia.org/wiki/Van_der_Pol_oscillator

https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/035-SciPy-EcuacionesDiferencialesOrdinarias.ipynb
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

"""
Oscilador de Van der Pol

d2x/dt2 - mu(1-x**2)dx/dt + x = 0, aunque usamos la forma bidimensional de y=x'
"""


def oscilador(vec, mu1, t1):  # vec = [x, y], el tiempo t tiene que ser explicito
    A = np.array([[0, 1], [-1, mu1*(1 - vec[0]**2)]])
    B = np.array([0, 0])
    return np.dot(A, vec) + B  # A*vec + B

y0 = [0, 1]
t = np.linspace(0, 3, 100)
plt.figure()
for mu in np.linspace(0, 1, 3):
    sol = integrate.odeint(lambda x, t1: oscilador(x, mu, t1), y0, t)

    plt.plot(t, sol[:, 0], label="mu = %s" % mu)

plt.legend(loc=1)

"Puedo no bloquear si quiero guardar la figura"
plt.show(block=False)


plt.show(block=True)
