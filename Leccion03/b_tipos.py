"""

Datos simples
1 - Numeric
2 - Strings / caracteres
3 - Booleans

Colecciones de datos
4 - List
5 - Tuples (son inmutables)
6 - Sets (conjunto unico de elementos)
7 - Dictionary (llave-valor)
-----------
8 - Clases
9 - Ficheros

"""

#  1 - Datos numericos
miVar = 2
miVar2 = 2.

print(type(miVar), miVar)
print(type(miVar2), miVar2)

print(1 / 2)
print(int(1 / 2))
print(1.0 // 2.0)

print("--------")

# 2 - Strings
myString = "my string"
myString2 = 'my other string'

print(type(myString), myString)  # comentario en linea
print(myString2)
print("valor 1" + str(miVar))
print("valor 1", miVar)
print("--------")

# 3 - Booleans
mistring = """estoy dejando
    un
espacio"""  # lo coge literal
mistring2 = "otra manera seria \n    asi"
mistring3 = r"si queremos que salga \n literalmente ponemos r'-----'"

if miVar:  # esto es True si miVar es diferente de "", 0, 0., no se que mas
    print(mistring)
    print(mistring2)
nada = 0
if not nada:
    print(mistring3)
