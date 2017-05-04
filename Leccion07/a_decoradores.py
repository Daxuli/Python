#  decoradores, como en Leccion02/d_DeclaracionCirculo.py
def decorador(funcion_a_decorar):
    def funcion_definida_dentro_del_decorador(*args, **kwargs):
        print("decorador: aqui podriamos introducir las instrucciones del decorador")
        funcion_a_decorar(args[0] + 1, args[1] + 1)
        print("seguimos en el decorador")

    return funcion_definida_dentro_del_decorador


@decorador
def a_decorar(x, y):
    print(x + y)


a_decorar(1, 2)
print("*****************************************************")

# ********************************************************************************************************************
def avisar(f):
    def inner(*args, **kwargs):  # * argumentos opcionales pasados en listas  ** argumentos opcionales en diccionarios
        f(args[0])
        print("Se ha ejecutado", f.__name__)

    return inner


def abrir_puerta(alguien="alguien"):
    print(alguien, "esta abriendo la puerta")


def cerrar_puerta():
    print("esta cerrando la puerta")


def wrapper(f):
    def imprime(*args):
        print("/----------------------------------------------\ ")
        f(args[0])
        print("\----------------------------------------------/ ")
    return imprime


@wrapper  # los decoradores con como las envolturas de un caramelo. Se van ejecutando de fuera a dentro
@avisar  # segunda capa
def abrir_ventana(alguien="alguien"):  # caramelo
    print(alguien, "esta abriendo la ventana")


# ------------------------------------------------------------------------------------
abrir_puerta()
cerrar_puerta()
print("-----------------------------------------------")

print("usando 'avisar(abrir_puerta)'")
mistr = lambda x: "%s:" % (type(x))
abrir_puerta1 = avisar(abrir_puerta)
print(mistr(abrir_puerta1))
abrir_puerta1("Daniel")
print("-----------------------------------------------")

print("usando 'abrir_ventana' con decorador 'avisar':")
abrir_ventana("Alberto")  # ruido llama a avisar, y avisar a abrir_ventana
