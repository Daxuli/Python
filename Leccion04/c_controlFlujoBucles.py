""" Ya habiamos visto la iteracion en un tipo secuencial o un iterable"""
lista = [1, 2, 'hola']
for elem in lista:
    print(elem, end=" | ")
print("\n---------------------------")

""" si necesito iterar con un indice, me genero el iterador con range"""
print(type(range(3)), range(3))
for i in range(3):
    print("índice %s:" % i, lista[i], end=" | ")
else:
    print("la sentencia else se ejecuta al agotar el bucle"
          " sin romperle")
print("---------------------------")


def buscarPrimos(y):
    for n in range(2, y):  # ejecuta hasta y-1
        # nested loop
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:  # if this runs, loop has fallen through without finding a factor
                """
                else clause;
                it is executed when the loop terminates through exhaustion of the list (with for)
                or when the condition becomes false (with while),
                but not when the loop is terminated by a break statement.
                """
                """
                else dentro (a la misma altura) de for: se ejecuta si se agotan todas las iteraciones (no hay break)
                for -----

                else  # está vinculado con el for
                """
                print(n, 'is a prime number')


buscarPrimos(10)
print("---------------------------")

lista = list(range(10))
lista = ["", 0, False, False, 3, "d", "ultimo"]
while lista:  # el bucle continúa hasta que la lista se quede vacía
    x = lista.pop()
    print(x, end=" | ")
else:
    print("\nterminó")
