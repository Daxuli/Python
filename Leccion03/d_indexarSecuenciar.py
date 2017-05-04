
milista   = ["a", "b", "c", "d", "e"]
# indice  = [ 0 ,  1 ,  2 ,  3 ,  4 ]  # indices de las listas
# indiceinv=[-5 , -4 , -3 , -2 , -1 ]  # indices inversos de las listas
longitud = len(milista)

print("longitud de milista:", longitud)
print(milista[1])
print(milista[1:12])  # no ocurre nada si nos pasamos por exceso
print("------------------")

#  si queremos imprimir los elementos bcd
print(milista[1:3])  # esta forma es erronea: empieza con el indice 1 pero acaba con el indice anterior al 3
print(milista[1:4])  # tendriamos que escribir esto
print("------------------")

#  si queremos imprimir los elementos b y d
print(milista[1:4:2])
print(milista[1:longitud-1:2])
print(milista[1:longitud:2])  # no pasa nada aunque no termine de cuadrar
print(milista[-2:0:-2])  # usando indices inversos sale tambien invertido
print("------------------")
# --------------------------------------


def hablaralreves(vector):  # lo que se me ocurrio en clase
    vectoreves = ""
    for elem in reversed(vector):
        vectoreves += elem
    print(vectoreves)


def hablaralreves2(vector):  # solucion que dimos en clase
    for elem in reversed(vector):
        print(elem, end="")
    print("")  # meti esto porque si no lo hacemos el proximo print sigue en la misma linea

mistring = "unafrase"

hablaralreves(milista)
hablaralreves2(mistring)
print("------------------")
# --------------------------------------
milista2 = ["a", ["b", "c"], "d", "e"]  # lista dentro de otra lista
print(milista2[1][1])  # para sacar c
