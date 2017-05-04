"""
este es un modulo de ejemplo
Voy a utilizar para romper otra funcion
"""


def sqrt(x):
    """
    No me he dado cuenta, y defino la raiz como el cuadrado
    :param x:
    :return:
    """
    return x**2

print("ejecutado desde el modulo: sqrt(3)=", sqrt(3))

if __name__ == "__main__":
    a = 4
    print(sqrt(a))
