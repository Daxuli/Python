
"""

http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html#numpy.save


http://docs.scipy.org/doc/numpy/reference/generated/numpy.load.html#numpy.load

"""
import numpy as np
from tempfile import TemporaryFile
import matplotlib.pyplot as plt

outfile = TemporaryFile()  # se elimina una ver cerrado

x = np.arange(10)
np.save(outfile, x)
del x  # lo eliminamos

outfile.seek(0)  # Only needed here to simulate closing & reopening file
x = np.load(outfile)
print(x)
print("--------------------------------------")

# ------------------------------------------------- loadtxt
perfil = np.loadtxt("n0012.txt", skiprows=3)

print(type(perfil), perfil)

plt.figure(1)
plt.plot(perfil[0:66, 0], perfil[0:66, 1])  # extrados
plt.plot(perfil[66:132, 0], perfil[66:132, 1])  # intrados
plt.ylim(-0.5, 0.5)
plt.show()
print("--------------------------------------")

# ------------------------------------------------- savetxt
np.savetxt("naca0012_mod.txt", perfil, fmt="%.10f", delimiter="**")
