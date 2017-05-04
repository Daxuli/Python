import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wid


def coger(ubicacion, lineasalta):
    return np.loadtxt(ubicacion, skiprows=lineasalta)


def trasladar(v0):
    for punto in range(v0.shape[0]):
        v0[punto] -= np.array([.25, 0])
    return v0


def rotar(v0, theta):
    t = np.radians(theta)
    def matrot(t1):
        c, s = np.cos(t1), np.sin(t1)
        R = np.matrix('{} {}; {} {}'.format(c, s, -s, c))
        return R
    R = matrot(t)
    v1 = np.zeros(v0.shape)
    for punto in range(v0.shape[0]):
        v1[punto] = np.dot(R, v0[punto])
    return v1


def distancia(v0, v1):
    d = v1 - v0
    return np.sqrt(d[0] ** 2 + d[1] ** 2)


perfil0 = coger("n0012.txt", 3)
perfilt = trasladar(perfil0)


axis_color = 'white'
fig = plt.figure()
theta0 = 0

perfilr = rotar(perfilt, theta0)
# ax = plt.subplot2grid((16, 16), (1, 1), colspan=14, rowspan=14, aspect="equal")  ya no hace falta, pero da mas control
ax = fig.add_subplot(111, aspect="equal")
fig.subplots_adjust(bottom=0.12)  # ya no distorsiona la imagen una vez que esta aspect="equal"
[line1] = ax.plot(perfilr[0:66, 0], perfilr[0:66, 1], color="C0")  # extrados
[line2] = ax.plot(perfilr[66:132, 0], perfilr[66:132, 1], color="C0")  # intrados
ax.set_xlim(-.8, .8)
ax.set_ylim(-.8, .8)

theta_slider_ax = fig.add_axes([0.1, 0.03, 0.8, 0.03], facecolor=axis_color)
theta_slider = wid.Slider(theta_slider_ax, 'Theta', -180, 180, valinit=0, facecolor="C1")

def slider_on_changed(val):
    theta_s = theta_slider.val
    v1 = rotar(perfilt, theta_s)
    line1.set_xdata(v1[0:66, 0])
    line1.set_ydata(v1[0:66, 1])
    line2.set_xdata(v1[66:132, 0])
    line2.set_ydata(v1[66:132, 1])
    fig.canvas.draw()
#   print(distancia(v1[55], v1[87]))  para comprobar que se mantenia la distancia entre 2 ptos

theta_slider.on_changed(slider_on_changed)


plt.show()



# falta fijar axis, cambiar a -90
